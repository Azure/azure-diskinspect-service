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
from GuestFishWrapper import GuestFishWrapper
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
            self.serviceMetrics.TotalRequests = self.serviceMetrics.TotalRequests + 1
            self.rootLogger.info('<<STATS>> ' + self.serviceMetrics.getMetrics())

            # Parse Input Parameters
            operationId, mode, storageAcctName, container_blob_name, storageUrl = self.ParseUrlArguments(self.path)                
            self.rootLogger.info('Starting service request for <Operation Id=' + operationId + ', Mode=' + mode + ', Url=' + self.path + '>')

            # Invoke LibGuestFS Wrapper for prorcessing
            with KeepAliveThread(self.rootLogger, self, threading.current_thread().getName()):
                with GuestFishWrapper(self.rootLogger, self, storageUrl, OUTPUTDIRNAME, operationId, mode) as outputFileName:

                    # Upload the ZIP file
                    if outputFileName:                
                        outputFileSize = round(os.path.getsize(outputFileName) / 1024, 2)
                        self.rootLogger.info('Uploading: ' + outputFileName + ' (' + str(outputFileSize) + 'kb)')
                        self.uploadFile(outputFileName)
                        self.rootLogger.info('Upload completed.')

                        successElapsed = datetime.now() - start_time
                        self.serviceMetrics.SuccessRequests = self.serviceMetrics.SuccessRequests + 1
                        self.serviceMetrics.TotalSuccessServiceTime = self.serviceMetrics.TotalSuccessServiceTime + successElapsed.total_seconds()

                        self.rootLogger.info('Request completed succesfully in ' + str(successElapsed.total_seconds()) + "s.")
                    else:
                        self.rootLogger.error('Failed to create zip package.')

        except ValueError as ex:
            self.rootLogger.error(str(ex))

            self.send_response(500)
            self.end_headers()
        except (IndexError, FileNotFoundError) as ex:
            self.rootLogger.exception('Exception: IndexError or FileNotFound error')

            self.send_response(404, 'Not Found')
            self.end_headers()
        except Exception as ex:
            self.rootLogger.exception('Exception: ' + str(ex))

            self.send_response(500)
            self.end_headers()
        finally:
            self.rootLogger.info('Ending service request.')
            self.rootLogger.info('<<STATS>> ' + self.serviceMetrics.getMetrics())
