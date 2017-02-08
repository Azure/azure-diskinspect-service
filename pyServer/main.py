#!/usr/bin/python3

import sys
import logging
import logging.handlers
from ServiceMetrics import ServiceMetrics
from AzureDiskInspectService import AzureDiskInspectService
from AzureDiskInspectService import ThreadingServer

"""
Globals
"""
IP_ADDRESS = '127.0.0.1'
PORT = 8081
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

# global service metrics 
serviceMetrics = ServiceMetrics()

"""
Main Entrypoint
"""
if __name__ == '__main__':
    server_address = (IP_ADDRESS, PORT)
    AzureDiskInspectService.protocol_version = "HTTP/1.1"
    AzureDiskInspectService.rootLogger = rootLogger
    AzureDiskInspectService.serviceMetrics = serviceMetrics
    server = ThreadingServer(server_address, AzureDiskInspectService)
    rootLogger.info('Started AzureDiskInspectService on IP: ' + str(IP_ADDRESS) + ', Port: ' + str(PORT))

    try:
        while (True):
            sys.stdout.flush()
            server.handle_request()
    except KeyboardInterrupt:
        print("Done")
