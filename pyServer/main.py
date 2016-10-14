#!/usr/bin/python3

import http.server
import urllib
import subprocess
import shutil
import sys
import os
import time
import socketserver
import logging
import logging.handlers
import io
import threading
import csv
import glob
from threading import Thread
from datetime import datetime

"""
Globals
"""
IP_ADDRESS = '127.0.0.1'
PORT = 8081
OUTPUTDIRNAME = '/output'
LOG_FILE = "/var/log/azureDiskInspectSvc.log"

"""
Logger Initialization
"""
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-7.7s]: %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=(1048576*5), backupCount=7)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

"""
Health Metrics 
"""
class ServiceMetrics:

    TotalRequests = None
    SuccessRequests = None
    TotalSuccessServiceTime = None
    ActiveRequests = None

    def __init__(self):
        self.TotalRequests = 0
        self.SuccessRequests = 0
        self.TotalSuccessServiceTime = 0
        self.ActiveRequests = 0

    def getMetrics(self):
        if (self.SuccessRequests > 0):
            avgSuccessServiceTime = self.TotalSuccessServiceTime / self.SuccessRequests
        else:
            avgSuccessServiceTime = 0

        resultStr = 'Total Requests: ' + str(self.TotalRequests) + \
                    ', Success Requests: ' + str(self.SuccessRequests) + \
                    ', Avg Success Service Time: ' + str(avgSuccessServiceTime) + 's' \
                    ', Active Requests: ' + str(self.ActiveRequests)
        return resultStr

# global service metrics 
serviceMetrics = ServiceMetrics()

"""
Helper to print progress
"""
def printProgress(iteration, total, prefix='',
                  suffix='', decimals=1, barLength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percents = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = 'X' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' %
                     (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

"""
Helper KeepAlive worker thread that attempts to
keep a HTTP/HTTPS connection alive by sending 
CONTINUE requests every 2 minutes to prevent
the client from disconnecting.
"""
class KeepAliveThread(Thread):

    httpRequestHandler = None
    exit_flag = None
    doWork = True
    forThread = None

    def __init__(self, handler, threadId):
        Thread.__init__(self)
        self.httpRequestHandler = handler
        self.doWork = True
        self.exit_flag = threading.Event()
        self.forThread = threadId
        rootLogger.info('Starting KeepAliveWorkerThread for thread [' +
                     str(self.forThread) + '].')

    def __enter__(self):
        self.start()
    
    def __exit__(self, type, value, traceback):
        self.complete()
        self.join()

    def run(self):                
        while True:
            if self.doWork:
                rootLogger.info(
                    'Sending CONTINUE response to keep thread [' + str(self.forThread) + '] alive.')
                self.httpRequestHandler.send_response_only(100)
                self.httpRequestHandler.end_headers()
            else:
                rootLogger.info(
                    'Exiting KeepAliveWorkerThread for thread [' + str(self.forThread) + '].')
                return
            if self.exit_flag.wait(timeout=120):
                break
        rootLogger.info('Exiting KeepAliveWorkerThread for thread [' +
                     str(self.forThread) + '].')

    def complete(self):
        self.doWork = False
        self.exit_flag.set()

"""
LibGuestFS Wrapper

This class is responsible for extracting the required logs and configuration
files from the specified Blob Uri by interacting with the LibGuestFS 
tool that can open disk images and run introspection commands on it.
"""
class GuestFS:
    storageUrl = None
    pid = None
    environment = None

    def __init__(self, storageUrl):
        self.storageUrl = storageUrl
        self.environment = os.environ.copy()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.exit()

    def buildGFArgs(self, args):
        retArgs = ['/libguestfs/run', 'guestfish', '--remote']
        retArgs.extend(args)
        return retArgs

    def callGF(self, echoStr, commands, continueOnError=False):
        start_time = datetime.now()
        try:
            retArgs = self.buildGFArgs(commands)
            rootLogger.info('GuestFish:' + echoStr + ':Remote> ' + ' '.join(retArgs))

            proc = subprocess.Popen(
                retArgs,
                env=self.environment,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True)
            (result, err) = proc.communicate()
            resultAsArray = str(result).splitlines()
            retValue = [resultAsArray, err]
            if result:
                resultStr = '\r\n'.join(resultAsArray)
                if len(resultAsArray) > 1:
                    resultStr = '\r\n' + resultStr
                rootLogger.info('GuestFish:' + echoStr + ':Result> ' + resultStr)
            if err:
                if continueOnError:
                    rootLogger.warning('GuestFish:' + echoStr + ':Error> \r\n' + err)
                else:
                    rootLogger.error('GuestFish:' + echoStr + ':Error> \r\n' + err)
            return retValue
        except subprocess.CalledProcessError as e:
            if not continueOnError:
                rootLogger.error('GuestFish:' + echoStr + ':FAILED')
                raise(e)
            else:
                rootLogger.warning('GuestFish:' + echoStr + ':WARNING')
        finally:
            elapsedTime = datetime.now() - start_time
            rootLogger.info('GuestFish:' + echoStr + ':Remote> ExecutionTime=' + str(elapsedTime.total_seconds()) + "s.")
            
    def start(self):
        # Run guestfish in remote mode and then send it a command
        # at a time since the programming environment inside guestfish
        # is very limited (no variables, etc.)

        args = ['/libguestfs/run', 'guestfish', '--listen', '-a', self.storageUrl, '--ro']
        rootLogger.info('GuestFish:Create:Local> ' + ' '.join(args))

        # Guestfish server mode returns a string of the form
        #   GUESTFISH_PID=pid; export GUESTFISH_PID
        # We need to parse this and extract out the GUESTFISH_PID
        # environment variable and inserting it into the subsequent env
        
        output = subprocess.check_output(args, env=self.environment, universal_newlines=True)

        try:
            self.pid = int(output.split(';')[0].split('=')[1])
        except Exception as e:
            raise Exception('Cannot find GUESTFISH_PID')

        self.environment['GUESTFISH_PID'] = str(self.pid)
        rootLogger.info('GuestFish:PID=' + str(self.pid))

    def launch(self):
        return self.callGF('Launching', ['launch'])
    
    def list_filesystems(self):
        (out, err) = self.callGF('Listing Filesystems', ['list-filesystems'], True)
        return out

    def inspect_os(self):
        (out, err) = self.callGF('Inspecting OS Metadata', ['inspect-os'], True)
        return out

    def inspect_get_type(self, device):
        (out, err) = self.callGF('Get OS Type', ['--', '-inspect-get-type', device], True)
        return out
 
    def inspect_get_distro(self, device):
        (out, err) = self.callGF('Get OS Distribution', ['--', '-inspect-get-distro', device], True)
        return out

    def inspect_get_product_name(self, device):
        (out, err) = self.callGF('Get Product Name', ['--', '-inspect-get-product-name', device], True)
        return out

    def inspect_get_mountpoints(self, device):
        (out, err) = self.callGF('Get Device Mountpoints', ['--', '-inspect-get-mountpoints', device], True)
        return out

    def unmount(self, mountpoint):
        try:
            (out, err) = self.callGF('Unmount [' + mountpoint + ']', ['--', '-unmount', mountpoint], True)
        except subprocess.CalledProcessError:
            pass

    def mount(self, mountpoint, device):
        try:
            (out, err) = self.callGF('Mount [' + mountpoint + ',' + device + ']', ['--', '-mount-ro', device, mountpoint], True)
            if err:
                return False
        except subprocess.CalledProcessError:
            return False
        return True

    def ll(self, directory):
        try:
            (out, err) = self.callGF('List(verbose) [' + directory + ']', ['--', '-ll', directory], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return out

    def copy_out(self, sourceFiles, targetDir):
        try:
            (out, err) = self.callGF('Copy [' + sourceFiles + ']', ['--', '-glob', 'copy-out', sourceFiles, targetDir], True)
            if err:
                return False
            targetFiles = targetDir + os.sep + os.path.basename(sourceFiles)
            list = glob.glob(targetFiles)
            if len(list) < 1:
                rootLogger.warning('GuestFish:Copy [' + sourceFiles + ']:Result> No files copied.')
                return False
        except subprocess.CalledProcessError:
            return False
        return True

    def exit(self):
        return self.callGF('Exiting', ['--', '-exit'])

"""
LibGuestFS Wrapper

This class is responsible for extracting the required logs and configuration
files from the specified Blob Uri by interacting with the LibGuestFS 
tool that can open disk images and run introspection commands on it.
"""
class GuestFishWrapper:
    environment = None
    httpRequestHandler = None
    storageUrl = None
    outputDirName = None
    outputFileName = None
    mode = None

    def __init__(self, handler, storageUrl, outputDirName, operationId, mode):
        self.environment = None
        self.httpRequestHandler = handler
        self.storageUrl = storageUrl
        self.outputDirName = outputDirName + os.sep + operationId
        self.mode = mode 

    def __enter__(self):
        self.outputFileName = self.execute(self.storageUrl)
        return self.outputFileName

    def __exit__(self, type, value, traceback):
        if (os.path.exists(self.outputDirName)):
            rootLogger.info('Removing: ' + self.outputDirName)
            shutil.rmtree(self.outputDirName)

        if (os.path.exists(self.outputFileName)):
            rootLogger.info('Removing: ' + self.outputFileName)
            os.remove(self.outputFileName)

    def WriteToResultFileWithHeader(self, operationOutFile, headerString, data):
        operationOutFile.write(headerString + '\r\n')
        if (isinstance(data, list)):
            operationOutFile.write("\r\n".join(data))            
        else:
            operationOutFile.write(str(data))      
        operationOutFile.write('\r\n')  
        operationOutFile.write('\r\n')
        operationOutFile.flush()
    
    def WriteToResultFile(self, operationOutFile, data):
        if (isinstance(data, list)):
            operationOutFile.write("\r\n".join(data))            
        else:
            operationOutFile.write(str(data))
        operationOutFile.write('\r\n') 
        operationOutFile.flush()

    def WriteInspectMetadataToResultFile(self, operationOutFile, device, osType, osDistribution, osProductName, osMountpoints):
        self.WriteToResultFile(operationOutFile, "Inspection Metadata for " + device)
        self.WriteToResultFile(operationOutFile, "Type: " + osType)
        self.WriteToResultFile(operationOutFile, "Distribution: " + osDistribution)
        self.WriteToResultFile(operationOutFile, "Product Name: " + osProductName)
        self.WriteToResultFileWithHeader(operationOutFile, "Mount Points:", osMountpoints)

    def GetInspectMetadata(self, guestfish, device):
        osType = guestfish.inspect_get_type(device)
        osDistribution = guestfish.inspect_get_distro(device)
        osProductName = guestfish.inspect_get_product_name(device)
        osMountpoints = guestfish.inspect_get_mountpoints(device)
        return (osType[0], osDistribution[0], osProductName[0], osMountpoints)        

    def execute(self, storageUrl):

        requestDir = self.outputDirName
        os.makedirs(requestDir)

        operationOutFilename = requestDir + os.sep + 'results.txt'

        with open(operationOutFilename, "w", newline="\r\n") as operationOutFile:
            with GuestFS(storageUrl) as guestfish:
                
                # Initialize
                guestfish.launch()

                # Enumerate file systems
                fsList = guestfish.list_filesystems()
                self.WriteToResultFileWithHeader(operationOutFile, "Filesystem Status:", fsList)

                # Enumerate devices identified as OS disks
                inspectList = guestfish.inspect_os()
                self.WriteToResultFileWithHeader(operationOutFile, "Inspection Status:", inspectList)

                deviceNumber = 0
                for device in inspectList:
                    rootLogger.info('GuestFish:Examining Device> %s', device)

                    # Gather and Write Inspect Metadata about the Device
                    (osType, osDistribution, osProductName, osMountpoints) = self.GetInspectMetadata(guestfish, device)
                    self.WriteInspectMetadataToResultFile(operationOutFile, device, osType, osDistribution, osProductName, osMountpoints)

                    mountpoint = "/"
                    guestfish.unmount(mountpoint)
                    wasMounted = guestfish.mount(mountpoint, device)

                    if not wasMounted:
                        self.WriteToResultFile(operationOutFile, "Mounting " + device + " on " + mountpoint + " FAILED.\r\n")

                        # Ignore and continue to next device
                        continue
                    else:
                        self.WriteToResultFile(operationOutFile, "Mounting " + device + " on " + mountpoint + " SUCCEEDED.\r\n")

                    manifestFile = "/etc/azdis/" + self.mode.lower()
                    operationNumber = 0
                    with open(manifestFile) as operationManifest:
                        contents = operationManifest.read().splitlines()
                        totalOperations = len(contents)
                        rootLogger.info("Reading manifest file from " + manifestFile + " with " + str(totalOperations) + " operation entries.")
                        for operation in contents:
                            operationNumber = operationNumber + 1
                            rootLogger.info("Executing Operation [" + str(operationNumber) + "/" + str(totalOperations) + "]: " + str(operation))                            
                            opList = operation.split(',')

                            if len(opList) < 2:
                                continue
                            
                            opCommand = str(opList[0]).lower()
                            opParam1 = opList[1]

                            if opCommand=="echo":
                                self.WriteToResultFile(operationOutFile, opParam1)
                            elif opCommand=="ll":
                                directory = opParam1
                                dirList = guestfish.ll(directory)
                                if dirList:
                                    self.WriteToResultFileWithHeader(operationOutFile, "Listing contents of " + directory + ":", dirList)
                                else:
                                    self.WriteToResultFile(operationOutFile, "Directory " + directory + " is not valid.")
                            elif opCommand=="copy":
                                gatherItem = opParam1

                                # Determine Output Folder
                                dirPrefix = os.path.dirname(gatherItem)
                                targetDir = requestDir + os.sep + 'device_' + str(deviceNumber) + dirPrefix

                                # Create Output Folder if needed
                                if not (os.path.exists(targetDir)):
                                    os.makedirs(targetDir)

                                # Copy 
                                wasCopied = guestfish.copy_out(gatherItem, targetDir)
                                if wasCopied:
                                    self.WriteToResultFile(operationOutFile, "Copying " + gatherItem + " SUCCEEDED.")
                                else:
                                    self.WriteToResultFile(operationOutFile, "Copying " + gatherItem + " FAILED.")

                deviceNumber = deviceNumber + 1

        archiveName = shutil.make_archive(requestDir, 'zip', requestDir)
        return archiveName

"""
Threading server to handle multiple web requests.
"""
class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

"""
Request Handler for the Service.

Services URL GET requests of the form:
    /operationId/mode/storage_acct_name/container_name/blobname?saskey

where:
    operationId: 
        unique request identifier 
    mode: 
        a disk extraction mode specification
    storage_acct_name: 
        storage account 
    container_name: 
        container NameError
    blobname?saskey: 
        SAS uri

The handler is responsible for servicing the GET request by 
handing off the request with the correct initialization parameters
to the LibGuestFS wrapper and then packaging the results and sending 
out the response result as a binary content stream. 
"""
class AzureDiskInspectService(http.server.BaseHTTPRequestHandler):

    """
    Parse the URL GET parameters
    """
    def ParseUrlArguments(self, urlPath):
        urlObj = urllib.parse.urlparse(urlPath)
        urlSplit = urlObj.path.split('/')
        if not len(urlSplit) >= 5:
            raise ValueError('Request has insufficient number of GET parameter arguments.')
        
        operationId = urlSplit[1]
        mode = urlSplit[2]
        storageAcctName = urlSplit[3]
        container_blob_name = urlSplit[4] + '/' + urlSplit[5]
        storageUrl = urllib.parse.urlunparse(
                ('https', storageAcctName + '.blob.core.windows.net', container_blob_name, '', urlObj.query, None))
            
        return operationId, mode, storageAcctName, container_blob_name, storageUrl

    """
    Upload a local file as a HTTP binary response.
    """
    def uploadFile(self, outputFileName):
        self.wfile.write(bytes('HTTP/1.1 200 OK\r\n', 'utf-8'))
        self.wfile.write(bytes('Content-Type: application/zip\r\n', 'utf-8'))

        statinfo = os.stat(outputFileName)
        self.wfile.write(bytes('Content-Length: {0}\r\n'.format(
            str(statinfo.st_size)), 'utf-8'))
        self.wfile.write(bytes(
            'Content-Disposition: Attachment; filename={0}\r\n'.format(
                os.path.basename(outputFileName)), 'utf-8'))
        self.wfile.write(bytes('\r\n', 'utf-8'))
        self.wfile.flush()

        outputFileSize = os.path.getsize(outputFileName)
        readSize = 0
        with open(outputFileName, 'rb') as outputFileObj:
            buf = None
            while (True):
                buf = outputFileObj.read(64 * 1024)
                if (not buf):
                    break
                readSize = readSize + len(buf)
                printProgress(
                    readSize, outputFileSize, prefix='Progress:', suffix='Complete', barLength=50)
                self.wfile.write(buf)
        self.wfile.flush()

    """
    GET request handler
    """
    def do_GET(self):
        outputFileName = None
        start_time = datetime.now()
        keepAliveWorkerThread = None

        try:
            serviceMetrics.TotalRequests = serviceMetrics.TotalRequests + 1
            rootLogger.info('<<STATS>> ' + serviceMetrics.getMetrics())

            # Parse Input Parameters
            operationId, mode, storageAcctName, container_blob_name, storageUrl = self.ParseUrlArguments(self.path)                
            rootLogger.info('Starting service request for <Operation Id=' + operationId + ', Mode=' + mode + ', Url=' + self.path + '>')

            # Invoke LibGuestFS Wrapper for prorcessing
            with KeepAliveThread(self, threading.current_thread().getName()):
                with GuestFishWrapper(self, storageUrl, OUTPUTDIRNAME, operationId, mode) as outputFileName:

                    # Upload the ZIP file
                    if outputFileName:                
                        outputFileSize = round(os.path.getsize(outputFileName) / 1024, 2)
                        rootLogger.info('Uploading: ' + outputFileName + ' (' + str(outputFileSize) + 'kb)')
                        self.uploadFile(outputFileName)
                        rootLogger.info('Upload completed.')

                        successElapsed = datetime.now() - start_time
                        serviceMetrics.SuccessRequests = serviceMetrics.SuccessRequests + 1
                        serviceMetrics.TotalSuccessServiceTime = serviceMetrics.TotalSuccessServiceTime + successElapsed.total_seconds()

                        rootLogger.info('Request completed succesfully in ' + str(successElapsed.total_seconds()) + "s.")
                    else:
                        rootLogger.error('Failed to create zip package.')

        except ValueError as ex:
            rootLogger.error(str(ex))

            self.send_response(500)
            self.end_headers()
        except (IndexError, FileNotFoundError) as ex:
            rootLogger.exception('Exception: IndexError or FileNotFound error')

            self.send_response(404, 'Not Found')
            self.end_headers()
        except Exception as ex:
            rootLogger.exception('Exception: ' + str(ex))

            self.send_response(500)
            self.end_headers()
        finally:
            rootLogger.info('Ending service request.')
            rootLogger.info('<<STATS>> ' + serviceMetrics.getMetrics())

"""
Main Entrypoint
"""
if __name__ == '__main__':
    server_address = (IP_ADDRESS, PORT)
    AzureDiskInspectService.protocol_version = "HTTP/1.1"
    server = ThreadingServer(server_address, AzureDiskInspectService)
    rootLogger.info('Started AzureDiskInspectService on IP: ' + str(IP_ADDRESS) + ', Port: ' + str(PORT))

    try:
        while (True):
            sys.stdout.flush()
            server.handle_request()
    except KeyboardInterrupt:
        print("Done")
