#!/usr/bin/python3

import http.server
import urllib
import sys
import os
import cgi
import socketserver
import subprocess
import threading
from datetime import datetime
from GuestFishWrapper import GuestFishWrapper
from GuestFishWrapper import DiskInspectionMetadata  #ensure telemetry is logged properly
from KeepAliveThread import KeepAliveThread

OUTPUTDIRNAME = '/output'

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
Get metadata about the host to aid in telemetry insight and troubleshooting scenarios
"""
def getHostMetadata():
    command = ["curl", "-H", "Metadata:true", "http://169.254.169.254/metadata/instance/compute?api-version=2017-08-01"]
    metadata = subprocess.check_output(command)
    return metadata.decode('utf-8')

"""
Get the container ID to aid in telemetry insight and troubleshooting scenarios
"""
def getContainerId():
    command = ['head', '/proc/1/cgroup', '-n 1']
    line = subprocess.check_output(command)
    longContainerId = subprocess.check_output(['basename', line])
    return longContainerId.decode('utf-8')[0:12]

"""
Threading server to handle multiple web requests.
"""
class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

"""
Request Handler for the Service.

Services URL POST requests of the form:
    /operationId/mode/storage_acct_name/container_name/blobname
with encoded data: saskey=<sasUrl>  

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

The handler is responsible for servicing the PUT request by 
handing off the request with the correct initialization parameters
to the LibGuestFS wrapper and then packaging the results and sending 
out the response result as a binary content stream. 
"""
class AzureDiskInspectService(http.server.BaseHTTPRequestHandler):

    """
    Parse the URL Query Parameters for Health Prefix
    """
    def IsHealthQuery(self, urlPath):
        urlObj = urllib.parse.urlparse(urlPath)
        urlSplit = urlObj.path.split('/')
        if not len(urlSplit) >= 1:
            raise ValueError('Request has insufficient number of query parameter arguments.')

        prefix = str(urlSplit[1])
        if (prefix.lower() == "health"):
            return True
        
        return False


    """
    Parse the URL POST parameters
    """
    def ParseUrlArguments(self, urlPath, sasKey):
        urlObj = urllib.parse.urlparse(urlPath)
        urlSplit = urlObj.path.split('/')
        if not len(urlSplit) >= 5:
            raise ValueError('Request has insufficient number of POST parameter arguments.')
        
        operationId = urlSplit[1]
        mode = str(urlSplit[2])
        modeMajorSkipTo = 1
        modeMinorSkipTo = 1
        modeSplit = str(mode).split(':')
        if len(modeSplit) > 1:
            mode = str(modeSplit[0])
            modeMajorSkipToStr = str(modeSplit[1])
            modeSkipSplitStr = str(modeMajorSkipToStr).split('.')
            if len(modeSkipSplitStr) > 1:
                modeMajorSkipTo = int(modeSkipSplitStr[0])
                modeMinorSkipTo = int(modeSkipSplitStr[1])
            else:
                modeMajorSkipTo = int(modeMajorSkipToStr)
            
        storageAcctName = urlSplit[3]
        container_blob_name = urlSplit[4]
        urlSplitIndex = 5
        while (urlSplitIndex < len(urlSplit)):
            container_blob_name = container_blob_name + '/' + urlSplit[urlSplitIndex]
            urlSplitIndex = urlSplitIndex + 1

        storageUrl = urllib.parse.urlunparse(
                ('https', storageAcctName + '.blob.core.windows.net', container_blob_name, '', sasKey, None))
            
        return operationId, mode, modeMajorSkipTo, modeMinorSkipTo, storageAcctName, container_blob_name, storageUrl

    """
    Upload a local file as a HTTP binary response.
    """
    def uploadFile(self, http_headers, outputFileName, isPartial, osType):
        # Set the HTTP headers, including extended content from GuestFishWrapper
        self.wfile.write(bytes('HTTP/1.1 200 OK\r\n', 'utf-8'))
        self.wfile.write(bytes('Content-Type: application/zip\r\n', 'utf-8'))
        for header in http_headers:
            header_value = str(http_headers[header])
            if len( header_value ) > 0:
                self.wfile.write(bytes( '{0}: {1}\r\n'.format( header,header_value ), 'utf-8' ))
                self.rootLogger.info('GuestFishWrapper Header "' + header + '" = "' + header_value +'"')

        statinfo = os.stat(outputFileName)
        self.wfile.write(bytes('Content-Length: {0}\r\n'.format(
            str(statinfo.st_size)), 'utf-8'))

        strOutputFileName = os.path.basename(outputFileName) + "-" + osType
        if isPartial:
            strOutputFileName = strOutputFileName + "-partial"
                        
        self.wfile.write(bytes(
            'Content-Disposition: Attachment; filename={0}\r\n'.format(
                os.path.basename(strOutputFileName)), 'utf-8'))
        self.wfile.write(bytes('\r\n', 'utf-8'))
        self.wfile.flush()

        # Write the zip file payload
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
        try:
            start_time = datetime.now()
            # Parse Input Parameters
            isHealthCheck = self.IsHealthQuery(self.path)
            if isHealthCheck:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                response = '<<STATS>>' + self.serviceMetrics.getMetrics()
                self.wfile.write(bytes("<html><head><title>InspectDisk Service Health Report</title></head>", "utf-8"))
                self.wfile.write(bytes("<body><p>", "utf-8"))
                self.wfile.write(bytes(response, "utf-8"))
                self.wfile.write(bytes("</p></body></html>", "utf-8"))
                self.wfile.flush()
                self.rootLogger.info('Health query requested by ' + str(self.client_address) + ' and responded with ' + response)
                self.telemetryClient.track_request('Health query', self.path, True, start_time.isoformat(), (datetime.now() - start_time).microseconds / 1000, 200, 'GET')
            else:
                self.rootLogger.info('Invalid GET query path requested by ' + self.client.address, ' for path ' + self.path) 
                self.telemetryClient.track_request('Invalid GET', self.path, False, start_time.isoformat(), (datetime.now() - start_time).microseconds / 1000, 200, 'GET')
        except Exception as ex:
            self.rootLogger.exception('Exception: ' + str(ex))
            self.send_error(500, str(ex)) 
            self.telemetryClient.track_request('GET Exception', self.path, False, start_time.isoformat(), (datetime.now() - start_time).microseconds / 1000, 500, 'GET')

    """
    POST request handler
    """
    def do_POST(self):

        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        
        outputFileName = None
        start_time = datetime.now()
        requestSucceeded = False
        fatal_exit = False
        try:
            self.serviceMetrics.TotalRequests = self.serviceMetrics.TotalRequests + 1
            self.rootLogger.info('<<STATS>> ' + self.serviceMetrics.getMetrics())

            sasKeyStr = str(postvars[b'saskey'][0], encoding='UTF-8')
            operationId, mode, modeMajorSkipTo, modeMinorSkipTo, storageAcctName, container_blob_name, storageUrl = self.ParseUrlArguments(self.path, sasKeyStr)                
            self.rootLogger.info('Starting service request for <Operation Id=' + operationId + ', Mode=' + mode + ', Url=' + self.path + '>')
            

            hostMetadata = getHostMetadata()
            # The Python AppInsight SDK does not expose User.StoreRegion, Cloud.* or ServerDevice.* contract fields at this time
            # # if hostMetadata and "location" in hostMetadata:
            #    region = hostMetadata["location"]
            if os.environ['CONTAINER_VERSION']:
                containerVersion = os.environ['CONTAINER_VERSION']
            else:
                containerVersion = 'not set'
            # update the fields in the telemetry client
            for h in self.rootLogger.handlers:
                if h.__class__.__name__ == 'LoggingHandler':
                    h.client.context.session.id = operationId
                    h.client.context.application.ver = containerVersion
                    telemetryClient = h.client

            customProperties = { 'mode' : mode,
                                 'operationId': operationId,
                                 'MajorSkipTo' : modeMajorSkipTo,
                                 'MinorSkipTo' : modeMinorSkipTo,
                                 'containerName' : getContainerId(),
                                 'containerVersion' : containerVersion,
                                 'HostMetadata' : hostMetadata
                                 }

            # Invoke LibGuestFS Wrapper for prorcessing
            with KeepAliveThread(self.rootLogger, self, threading.current_thread().getName()) as kpThread:
                with GuestFishWrapper(self.rootLogger, self, storageUrl, OUTPUTDIRNAME, operationId, mode, modeMajorSkipTo, modeMinorSkipTo, kpThread) as gfWrapper:

                    # Upload the ZIP file
                    if gfWrapper.outputFileName:    
                        outputFileName = gfWrapper.outputFileName            
                        outputFileSize = round(os.path.getsize(outputFileName) / 1024, 2)
                        self.rootLogger.info('Uploading: ' + outputFileName + ' (' + str(outputFileSize) + 'kb)')
                        self.uploadFile(gfWrapper.metadata_pairs, outputFileName, kpThread.wasTimeout, gfWrapper.osType)
                        self.rootLogger.info('Upload completed.')

                        successElapsed = datetime.now() - start_time
                        self.serviceMetrics.SuccessRequests = self.serviceMetrics.SuccessRequests + 1
                        self.serviceMetrics.TotalSuccessServiceTime = self.serviceMetrics.TotalSuccessServiceTime + successElapsed.total_seconds()
                        self.serviceMetrics.ConsecutiveErrors = 0
                        requestSucceeded = True                        
                        
                        self.rootLogger.info('Request completed succesfully in ' + str(successElapsed.total_seconds()) + "s.")
                        # Capture info discovered about the VHD for telemetry
                        for metadata in gfWrapper.metadata_pairs:
                            metadata_value = str(gfWrapper.metadata_pairs[metadata])
                            if len( metadata_value ) > 0:
                                customProperties[metadata] = metadata_value 
                        # track request and metrics
                        self.telemetryClient.track_request('Request Success', self.path, requestSucceeded, start_time.isoformat(), successElapsed.total_seconds() * 1000, 200, 'POST', customProperties)
                        self.telemetryClient.track_metric("Request Success", 1)
                        self.telemetryClient.track_metric("Request Success Duration", successElapsed.total_seconds())
                    else:
                        self.rootLogger.error('Failed to create zip package.')
                        self.telemetryClient.track_request('Failed to create zip', self.path, requestSucceeded, start_time.isoformat(), successElapsed.total_seconds() * 1000, 200, 'POST', customProperties)

        except ValueError as ex:
            self.rootLogger.error(str(ex))
            self.send_error(500, str(ex))
            self.telemetryClient.track_request('POST ValueError', self.path, requestSucceeded, start_time.isoformat(), (datetime.now() - start_time).microseconds / 1000, 500, 'POST', customProperties)
        except (IndexError, FileNotFoundError) as ex:
            self.rootLogger.exception('Exception: IndexError or FileNotFound error')
            self.send_error(404, 'Not Found')
            self.telemetryClient.track_request('POST Not Found', self.path, requestSucceeded, start_time.isoformat(), (datetime.now() - start_time).microseconds / 1000, 404, 'POST', customProperties)
        except Exception as ex:
            self.rootLogger.exception('Exception: ' + str(ex))
            self.send_error(500, str(ex))
            self.telemetryClient.track_request('POST Exception', self.path, requestSucceeded, start_time.isoformat(), (datetime.now() - start_time).microseconds / 1000, 500, 'POST', customProperties)
        finally:
            if (not requestSucceeded):
                self.serviceMetrics.ConsecutiveErrors = self.serviceMetrics.ConsecutiveErrors + 1
                self.telemetryClient.track_metric("Request Failure", 1)
                failedElapsed = datetime.now() - start_time
                self.telemetryClient.track_metric("Request Failure Duration", failedElapsed.total_seconds())
                if (self.serviceMetrics.ConsecutiveErrors > 10):
                    self.rootLogger.error('FATAL FAILURE: More than 10 consecutive requests failed to be serviced. Shutting down.')
                    self.telemetryClient.track_metric("Fatal Failure", 1)
                    fatal_exit = True       # set a flag so that the telemetry clients are flushed prior to exit

            self.rootLogger.info('Ending service request.')
            self.rootLogger.info('<<STATS>> ' + self.serviceMetrics.getMetrics())
            # Make sure the telemetry is flushed into its channels
            self.telemetryClient.flush()
            for h in self.rootLogger.handlers:
                if h.__class__.__name__ == 'LoggingHandler':
                    h.flush()
                    h.client.context.session.id = None
                    telemetryClient = h.client
            if (fatal_exit):
                os._exit(1)