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

MAX_TIMEOUT = 60*25

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

    def __init__(self, rootLogger, handler, threadId):
        Thread.__init__(self)
        self.httpRequestHandler = handler
        self.doWork = True
        self.exit_flag = threading.Event()
        self.forThread = threadId
        self.rootLogger = rootLogger
        self.rootLogger.info('Starting KeepAliveWorkerThread for thread [' +
                     str(self.forThread) + '].')

    def __enter__(self):
        self.start()
    
    def __exit__(self, type, value, traceback):
        self.complete()
        self.join()

    def run(self):        
        totalWait = 0        
        while True:
            if self.doWork:
                self.rootLogger.info(
                    'Sending CONTINUE response to keep thread [' + str(self.forThread) + '] alive.')
                self.httpRequestHandler.send_response_only(100)
                self.httpRequestHandler.end_headers()
            else:
                self.rootLogger.info(
                    'Exiting KeepAliveWorkerThread for thread [' + str(self.forThread) + '].')
                return
            if self.exit_flag.wait(timeout=120):
                break
            totalWait = totalWait + 120
            if totalWait > MAX_TIMEOUT:
                self.rootLogger.info('Thread [' + str(self.forThread) +'] waited for too long. Terminating.')
                self.complete()
        self.rootLogger.info('Exiting KeepAliveWorkerThread for thread [' +
                     str(self.forThread) + '].')

    def complete(self):
        self.doWork = False
        self.exit_flag.set()