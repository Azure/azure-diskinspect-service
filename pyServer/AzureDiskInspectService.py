#!/usr/bin/python3

import http.server
import urllib
import sys
import os
import cgi
import socketserver
import subprocess
import threading
import logging
import logging.handlers
import traceback
from datetime import datetime
from GuestFishWrapper import GuestFishWrapper
from GuestFishWrapper import DiskInspectionMetadata  #ensure telemetry is logged properly
from GuestFS import InvalidSasException, InvalidVhdNotFoundException, InvalidStorageAccountException
from KeepAliveThread import KeepAliveThread
from applicationinsights import TelemetryClient
from applicationinsights.logging import LoggingHandler
import json

from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions,
    BlobPermissions,
    PublicAccess,
)
from azure.storage.common import (
    AccessPolicy,
    ResourceTypes,
    AccountPermissions,
)

OUTPUTDIRNAME = '/output'
DEFAULT_TIMEOUT_IN_MINS = 19
DEFAULT_ARCHIVING_OVERHEAD_IN_MINS = 1
EXTENDED_ARCHIVING_OVERHEAD_IN_MINS = 4

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
    command = ["curl", "-H", "Metadata:true", "-A", "DiskInspectionService", "http://169.254.169.254/metadata/instance/compute?api-version=2017-08-01"]
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


class ResponseHeaderMetadata:
    KEEPALIVETHREAD_TIMEOUT_IN_MINS = "KeepAliveThread-Timeout-In-Mins"

"""
Threading server to handle multiple web requests.
"""
class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

class InvalidBlobSasUrlException(Exception):
   """Raised when an invalid Blob Sas Url is received as parameter input"""
   pass

class BlobUploadException(Exception):
   """Raised when an error is encountered during uploading result to Blob via Sas Url"""
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

    def __init__(self, request, client_address, server ):    
        self.hostMetadata = getHostMetadata()
        self.containerId = getContainerId() 
        if 'CONTAINER_VERSION' in os.environ:
            self.containerVersion = os.environ['CONTAINER_VERSION']
        else:
            self.containerVersion = 'not set'
        if 'RELEASENAME' in os.environ:
            self.releaseName=os.environ['RELEASENAME']
        else:
            self.releaseName="AzureDiskInspect-Release-MANUAL"
        self.InitializeAppInsights() 
        super().__init__(request, client_address, server) # invoke the base class constructor

    def InitializeAppInsights(self):
        # AppInsights initialization
        cur_thread = threading.current_thread()
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-7.7s]: %(message)s")
        appInsightsKey = os.environ['APPINSIGHTS_KEY']
        self.rootLogger.info("AppInsights key: '" + appInsightsKey + "'")   # log locally

        # create a child logger per thread so that we can set the SessionId without collision during concurrent execution
        #  by default logging will propagate to the parent rootLogger
        self.telemetryLogger = self.rootLogger.getChild('AppInsights.{0}'.format(cur_thread) )
        telemetryhandler = LoggingHandler(appInsightsKey)
        telemetryhandler.setFormatter(logFormatter)
        telemetryhandler.client.context.application.id = "DiskInspect-Service"
        telemetryhandler.client.context.application.ver = self.containerVersion
        telemetryhandler.client.context.properties['releaseName'] = self.releaseName
        self.telemetryLogger.addHandler(telemetryhandler)

        self.telemetryClient = telemetryhandler.client

    """
    Retrieve the name of the host from the Azure metadata
    """
    def getInstanceNameFromMetadata(self):
        if (len(self.hostMetadata) > 1 and "name" in self.hostMetadata):
            try:
                roleInstance = json.loads(self.hostMetadata)["name"]
                self.telemetryLogger.info("Request executing on instance: " + roleInstance)
            except json.decoder.JSONDecodeError as ex:
                self.telemetryLogger.error("Unexpected metadata: " + self.hostMetadata) 
                roleInstance = "Unknown"
        return roleInstance

    '''
    The Application Insights libary hooks Logger.exception() but it does not allow for the passing of 
    custom properties when doing so.  Hence we have a help function to log to the console only, then
    send an exception object to telemetry with the desired dimensions
    '''
    
    def logException(self, ex, properties=None):
        customProperties =  {"HOSTNAME": os.environ['HOSTNAME'] if 'HOSTNAME' in os.environ  else ""}
        if properties:
            customProperties.update(properties)  # combine with any passed in
        self.telemetryLogger.error(traceback.format_exc())
        self.rootLogger.exception(str(ex))  # note this is rootLogger not the child telemetryLogger
        self.telemetryClient.track_exception(*sys.exc_info(), properties=customProperties)

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
    Validate and parse the given destination Blob Sas Url.

    A Blob Sas Url has these components:

        https://<a. Account_Name>.<b. Blob_endpoint_suffix>/<c. Container_Name>/<d. Blob_Name>?<e. Sas_Token>

    For example:

        https://myaccount.blob.core.windows.net/mycontainer/outputfile.zip?some_sas_token

    These can be parsed using the Python urllib.parse.urlparse tool by looking up:

        urlparse(blobSasUrl).netloc = <a. Account_Name>.<b. Blob_endpoint_suffix>
        urlparse(blobSasUrl).path = <c. Container_Name>/<d. Blob_Name>
        urlparse(blobSasUrl).query: = <e. Sas_Token>

    The following validating and parsing logic is based on the pattern described.
    """
    def ValidateAndParseBlobSasUrl(self, blobSasUrl):
        self.telemetryLogger.info("Validating input destination Blob Sas Url.")

        urlParts = urllib.parse.urlparse(blobSasUrl)

        if not urlParts.path or len(urlParts.path) == 0:
            raise InvalidBlobSasUrlException('Input Blob SAS Url for upload is missing Container and Blob info.')
        if not urlParts.query or len(urlParts.query) == 0:
            raise InvalidBlobSasUrlException('Input Blob SAS url for upload is missing SAS token.')

        if urlParts.path[0] == '/':
            blob_storage_path = urlParts.path[1:]
        else:
            blob_storage_path = urlParts.path

        if 'blob' not in urlParts.netloc:
            raise InvalidBlobSasUrlException('Input Blob SAS url for upload is not pointing to a valid Azure Blob endpoint.')

        self.destination_storage_account = urlParts.netloc.split('.')[0]

        if not self.destination_storage_account:
            raise InvalidBlobSasUrlException('Input Blob SAS url for upload does not contain storage account.')

        urlSplit = blob_storage_path.split('/')

        if not len(urlSplit) == 2 or not urlSplit[0] or not urlSplit[1]:
            raise InvalidBlobSasUrlException('Input Blob SAS Url is not in the right format.')
        
        self.destination_container_name = urlSplit[0]
        self.destination_blob_name = urlSplit[1]
        self.destination_sas_token = urlParts.query

        self.telemetryLogger.info("Destination Blob Storage Account: " + self.destination_storage_account)
        self.telemetryLogger.info("Container Name: " + self.destination_container_name)
        self.telemetryLogger.info("Blob Name: " + self.destination_blob_name)

    """
    Upload the given file to destination Blob storage using the given Sas Url.
    """
    def uploadFileWithBlobSasUrl(self, file_name_full_path):
        retryRemaining = 3
        while retryRemaining > 0:
            try:
                sas_service = BlockBlobService(account_name=self.destination_storage_account, sas_token=self.destination_sas_token)
                self.telemetryLogger.info('Uploading to Blob starting.')
                start_time = datetime.now()
                sas_service.create_blob_from_path(self.destination_container_name, self.destination_blob_name, file_name_full_path)
                self.telemetryLogger.info('Uploading to Blob completed. Time take: ' + str((datetime.now() - start_time).total_seconds() * 1000) + ' ms')
                break
            except Exception as ex:
                retryRemaining -= 1
                if retryRemaining <= 0:
                    self.telemetryLogger.error('Encountered error during blob upload multiple times after exhausting all retry attempts')
                    raise BlobUploadException(ex)
                exMessage = str(ex)
                self.telemetryLogger.warning('Encountered error during blob upload: ' + exMessage)
                self.telemetryLogger.warning('Retrying. ' + str(retryRemaining) + ' attempt(s) remaining.')

    """
    Upload a local file either as a HTTP binary response or upload to a given destination blob storage.
    """
    def uploadFile(self, http_headers, outputFileName, isPartial, osType, blobSasUrl):

        if blobSasUrl:
            self.telemetryLogger.info('Uploading result to Blob storage.')
            self.uploadFileWithBlobSasUrl(file_name_full_path=outputFileName)
            self.PrepareHttpResponseHeaders(http_headers)
            self.wfile.write(bytes('Content-Type: text/plain\r\n', 'utf-8'))
            statinfo = os.stat(outputFileName)
            self.wfile.write(bytes('Content-Length: 0\r\n', 'utf-8'))
            self.wfile.write(bytes('\r\n', 'utf-8'))
            self.wfile.flush()
        else:
            self.telemetryLogger.info('Writing result to Http reponse.')
            self.PrepareHttpResponseHeaders(http_headers)
            self.wfile.write(bytes('Content-Type: application/zip\r\n', 'utf-8'))
            
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
            
            self.telemetryLogger.info('Finished writing output Http response.')

    def PrepareHttpResponseHeaders(self, http_headers):
        # Set the HTTP headers, including extended content from GuestFishWrapper
        self.wfile.write(bytes('HTTP/1.1 200 OK\r\n', 'utf-8'))

        for header in http_headers:
            header_value = str(http_headers[header])
            if len( header_value ) > 0:
                self.wfile.write(bytes( '{0}: {1}\r\n'.format( header,header_value ), 'utf-8' ))
                self.telemetryLogger.info('GuestFishWrapper Header "' + header + '" = "' + header_value +'"')

    """
    GET request handler
    """
    def do_GET(self):
        try:
            start_time = datetime.now()

            if ("error" in self.hostMetadata):
                self.hostMetadata = getHostMetadata()

            customProperties = { 
                        "HOSTNAME": os.environ['HOSTNAME'] if 'HOSTNAME' in os.environ  else "",
                        'containerName' : self.containerId,
                        'containerVersion' : self.containerVersion,
                        'HostMetadata' : self.hostMetadata,
                        'HttpMethod':'GET'
                        }

            roleInstance = self.getInstanceNameFromMetadata()
            # Hack: we cram this data into a global context available in the Python AppInsights SDK 
            # which will be sent by the logger in a field that the Geneva connector will pickup, and we post-process during cook
            self.telemetryClient.context.user.id = os.environ['HOSTNAME'] + "/" + roleInstance

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
                self.telemetryLogger.info('Health query requested by ' + str(self.client_address) + ' and responded with ' + response)
                self.telemetryClient.track_request('Health query', self.path, True, start_time.isoformat(), (datetime.now() - start_time).total_seconds() * 1000, 200, 'GET', customProperties)
                self.telemetryClient.track_metric("HttpResponseCode", 200,count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':'OK', 'Method':'GET'})
            else:
                self.telemetryLogger.info('Invalid GET query path requested by ' + str(self.client_address) + ' for path ' + self.path) 
                self.send_error(400)
                self.telemetryClient.track_metric("HttpResponseCode", 400, count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':'BAD_REQUEST', 'Method':'GET'})
                self.telemetryClient.track_request('Invalid GET', self.path, False, start_time.isoformat(), (datetime.now() - start_time).total_seconds() * 1000, 400, 'GET', customProperties)
        except Exception as ex:
            self.logException(ex, customProperties)
            self.send_error(500, str(ex)) 
            self.telemetryClient.track_metric("HttpResponseCode", 500, count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':'INTERNAL_SERVER_ERROR', 'Method':'GET'})
            self.telemetryClient.track_request('GET Exception', self.path, False, start_time.isoformat(), (datetime.now() - start_time).total_seconds() * 1000, 500, 'GET', customProperties)
        finally:
            # Make sure the telemetry is flushed into its channels
            self.telemetryClient.flush()
            for h in self.telemetryLogger.handlers:
                if h.__class__.__name__ == 'LoggingHandler':
                    h.flush()
                    h.client.context.session.id = None
            self.telemetryClient.context.session.id = None

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
        unexpectedError = False  # certain exception should not affect view of server health
        failureResultCode = 500
        telemetryException = None
        failureStatusText = None
        fatal_exit = False

        try:
            self.serviceMetrics.TotalRequests = self.serviceMetrics.TotalRequests + 1
            self.telemetryLogger.info('<<STATS>> ' + self.serviceMetrics.getMetrics())

            sasKeyStr = str(postvars[b'saskey'][0], encoding='UTF-8')
            operationId, mode, modeMajorSkipTo, modeMinorSkipTo, storageAcctName, container_blob_name, storageUrl = self.ParseUrlArguments(self.path, sasKeyStr)                

            if b'credscan' in postvars:
                credscanStr = str(postvars[b'credscan'][0], encoding='UTF-8')
                runWithCredscan = (credscanStr == "true")
            else:
                runWithCredscan = False

            timeoutInMinsStr = str(DEFAULT_TIMEOUT_IN_MINS)

            if b'timeout' in postvars:
                timeoutInputStr = str(postvars[b'timeout'][0], encoding='UTF-8')
                if timeoutInputStr.isdecimal() and int(timeoutInputStr) > 0 and int(timeoutInputStr) < 120 :
                    timeoutInMinsStr = timeoutInputStr
                else:
                    self.telemetryLogger.info('WARNING: Received timeout override is invalid: {0}. Default will be used.'.format(timeoutInMinsStr))

            timeoutInMins = int(timeoutInMinsStr)

            self.telemetryLogger.info('Received timeout value: ' + str(timeoutInMins)+ ' min(s)')

            if timeoutInMins <= DEFAULT_TIMEOUT_IN_MINS:
                zipFileHandlingOverhead = DEFAULT_ARCHIVING_OVERHEAD_IN_MINS # If customized timeout is low, inspection result will likely be small. Zip archive creation will be faster.
            else:
                zipFileHandlingOverhead = EXTENDED_ARCHIVING_OVERHEAD_IN_MINS  # if customized timeout is high, inspection result will likely be large and zip archiving time will take longer.

            self.telemetryLogger.info('Trimming timeout value by ' + str(zipFileHandlingOverhead)+ ' min(s) to reserve overhead time for inspection file archiving.')
            timeoutInMins -= zipFileHandlingOverhead
            self.telemetryLogger.info('Using timeout value: ' + str(timeoutInMins)+ ' min(s)')

            if b'blobsasurl' in postvars:
                blobSasUrl = str(postvars[b'blobsasurl'][0], encoding='UTF-8')
                self.ValidateAndParseBlobSasUrl(blobSasUrl)
                self.telemetryLogger.info('Received a valid Blob Sas url for upload. Result will be uploaded to Blob directly instead of Http response.')
            else:
                blobSasUrl = ""

            # update the fields in the telemetry client
            for h in self.telemetryLogger.handlers:
                if h.__class__.__name__ == 'LoggingHandler':
                    h.client.context.session.id = operationId                   
            self.telemetryClient.context.session.id = operationId
            self.telemetryLogger.info('Starting service request for <Operation Id=' + operationId + ', Mode=' + mode + ', Url=' + self.path + '>')

            if ("error" in self.hostMetadata):
                self.hostMetadata = getHostMetadata()

            customProperties = {"HOSTNAME": os.environ['HOSTNAME'] if 'HOSTNAME' in os.environ  else "",
                                'mode' : mode,
                                'operationId': operationId,
                                'MajorSkipTo' : modeMajorSkipTo,
                                'MinorSkipTo' : modeMinorSkipTo,
                                'containerName' : self.containerId,
                                'containerVersion' : self.containerVersion,
                                'HostMetadata' : self.hostMetadata,
                                'HttpMethod':'POST'
                                }

            roleInstance = self.getInstanceNameFromMetadata()
            # Hack: we cram this data into a global context available in the Python AppInsights SDK 
            # which will be sent by the logger in a field that the Geneva connector will pickup, and we post-process during cook
            self.telemetryClient.context.user.id = os.environ['HOSTNAME'] + "/" + roleInstance

            # Invoke LibGuestFS Wrapper for prorcessing
            with KeepAliveThread(self.telemetryLogger, self, threading.current_thread().getName(), timeoutInMins) as kpThread:
                with GuestFishWrapper(self.telemetryLogger, self, storageUrl, OUTPUTDIRNAME, operationId, mode, modeMajorSkipTo, modeMinorSkipTo, kpThread, runWithCredscan) as gfWrapper:
                    gfWrapper.start()
                    # Upload the ZIP file
                    if gfWrapper.outputFileName:
                        if not blobSasUrl:
                            self.telemetryLogger.info('Turning off KeepAlive messages before writing result to response.')
                            kpThread.avoidSendingKeepAlive = True  # stop KeepAlive if we send the zip in response to avoid corruption issue
                        outputFileName = gfWrapper.outputFileName            
                        outputFileSize = round(os.path.getsize(outputFileName) / 1024, 2)
                        self.telemetryLogger.info('Uploading: ' + outputFileName + ' (' + str(outputFileSize) + 'kb)')
                        gfWrapper.metadata_pairs[ResponseHeaderMetadata.KEEPALIVETHREAD_TIMEOUT_IN_MINS] = timeoutInMins
                        self.uploadFile(gfWrapper.metadata_pairs, outputFileName, kpThread.wasTimeout, gfWrapper.osType, blobSasUrl)

                        successElapsed = datetime.now() - start_time
                        self.serviceMetrics.SuccessRequests = self.serviceMetrics.SuccessRequests + 1
                        self.serviceMetrics.TotalSuccessServiceTime = self.serviceMetrics.TotalSuccessServiceTime + successElapsed.total_seconds()
                        self.serviceMetrics.ConsecutiveErrors = 0
                        requestSucceeded = True                        

                        self.telemetryLogger.info('Request completed succesfully in ' + str(successElapsed.total_seconds()) + "s.")
                        # Capture info discovered about the VHD for telemetry
                        for metadata in gfWrapper.metadata_pairs:
                            metadata_value = str(gfWrapper.metadata_pairs[metadata])
                            if len( metadata_value ) > 0:
                                customProperties[metadata] = metadata_value 
                        # track request and metrics
                        self.telemetryClient.track_request('Request Success', self.path, requestSucceeded, start_time.isoformat(), successElapsed.total_seconds() * 1000, 200, 'POST', customProperties)
                        self.telemetryClient.track_metric("HttpResponseCode", 200, count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':'OK', 'Method':'POST'})
                        self.telemetryClient.track_metric("Request Success Duration", successElapsed.total_seconds(), count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':'OK', 'Method':'POST'})
                    else:
                        error_string = 'Failed to create zip package.'
                        self.telemetryLogger.error(error_string)
                        self.send_error(500, error_string)
                        self.telemetryClient.track_metric("HttpResponseCode", 500, count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':'INTERNAL_SERVER_ERROR', 'Method':'POST'})
                        self.telemetryClient.track_request(error_string, self.path, requestSucceeded, start_time.isoformat(), successElapsed.total_seconds() * 1000, 500, 'POST', customProperties)                        

        except InvalidVhdNotFoundException as ex:
            unexpectedError = False
            failureResultCode = 404
            telemetryException = ex
            failureStatusText = 'Vhd not found'
            self.telemetryLogger.error(failureStatusText)  # don't raise exception            
        except InvalidStorageAccountException as ex:
            unexpectedError = False
            failureResultCode = 400
            telemetryException = ex
            failureStatusText = 'Invalid storage account'
            self.telemetryLogger.error(failureStatusText)  # don't raise exception  
        except InvalidSasException as ex:
            unexpectedError = False
            failureResultCode = 400
            telemetryException = ex
            failureStatusText = 'Invalid SAS uri'
            self.telemetryLogger.error(failureStatusText)  # don't raise exception  
        except InvalidBlobSasUrlException as ex:
            unexpectedError = False
            failureResultCode = 400
            telemetryException = ex
            failureStatusText = 'Invalid Blob SAS uri for upload'
            self.telemetryLogger.error(failureStatusText)
        except BlobUploadException as ex:
            unexpectedError = False
            failureResultCode = 500
            telemetryException = ex
            failureStatusText = 'Error encountered during blob upload'
            self.telemetryLogger.error(failureStatusText)
        except ValueError as ex:
            unexpectedError = True
            telemetryException = ex
            self.logException(ex, customProperties)
            failureStatusText = 'ValueError'
        except (IndexError, FileNotFoundError) as ex:
            unexpectedError = True
            failureResultCode = 404
            telemetryException = ex
            self.logException(ex, customProperties)
            failureStatusText = 'Not Found'
        except BrokenPipeError as ex:
            unexpectedError = False
            telemetryException = ex
            self.logException(ex, customProperties)
            failureStatusText = 'BrokenPipe error'
        except Exception as ex:
            unexpectedError = True
            telemetryException = ex
            self.logException(ex, customProperties)
            failureStatusText = 'Server Error'
        except:
            exc_value = sys.exc_info()[1]
            unexpectedError = True
            telemetryException = exc_value
            self.logException(exc_value, customProperties)
            failureStatusText = 'Server Error'
        finally:
            if (not requestSucceeded):
                self.send_error(failureResultCode, "%s: %s" % (failureStatusText, str(telemetryException)))
                self.telemetryClient.track_metric("HttpResponseCode", failureResultCode, count=1, properties={"HOSTNAME": os.environ['HOSTNAME'], 'StatusText':failureStatusText, 'Method':'POST'})
                self.telemetryClient.track_request('POST ' + failureStatusText, self.path, requestSucceeded, start_time.isoformat(), (datetime.now() - start_time).total_seconds() * 1000, 500, 'POST', customProperties)
                failedElapsed = datetime.now() - start_time
                self.telemetryClient.track_metric("Request Failure Duration", failedElapsed.total_seconds())
                if unexpectedError:
                    self.serviceMetrics.ConsecutiveErrors = self.serviceMetrics.ConsecutiveErrors + 1
                    if (self.serviceMetrics.ConsecutiveErrors > 10):
                        self.telemetryLogger.error('FATAL FAILURE: More than 10 consecutive requests failed to be serviced. Shutting down.')
                        self.telemetryClient.track_metric("Fatal Failure", 1)
                        fatal_exit = True       # set a flag so that the telemetry clients are flushed prior to exit

            self.telemetryLogger.info('Ending service request.')
            self.telemetryLogger.info('<<STATS>> ' + self.serviceMetrics.getMetrics())
            # Make sure the telemetry is flushed into its channels
            self.telemetryClient.flush()
            for h in self.telemetryLogger.handlers:
                if h.__class__.__name__ == 'LoggingHandler':
                    h.flush()
                    h.client.context.session.id = None
            self.telemetryClient.context.session.id = None
            if (fatal_exit):
                os._exit(1)