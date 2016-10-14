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
import ServiceMetrics
import AzureDiskInspectService

"""
Globals
"""
IP_ADDRESS = '127.0.0.1'
PORT = 8081
OUTPUTDIRNAME = '/output'
LOG_FILE = "/var/log/azureDiskInspectSvc.log"
MAX_TIMEOUT = 60*25

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

# global service metrics 
serviceMetrics = ServiceMetrics()

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
