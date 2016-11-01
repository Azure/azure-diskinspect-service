#!/usr/bin/python3

import os
import signal
import threading
from threading import Thread

TIME_PERIOD = 60
MAX_TIMEOUT = TIME_PERIOD * 19

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
    guestfishPid = None
    wasTimeout = False

    def __init__(self, rootLogger, handler, threadId):
        Thread.__init__(self)
        self.httpRequestHandler = handler
        self.doWork = True
        self.exit_flag = threading.Event()
        self.forThread = threadId
        self.rootLogger = rootLogger
        self.guestfishPid = None
        self.wasTimeout = False
        self.rootLogger.info('Starting KeepAliveWorkerThread for thread [' +
                     str(self.forThread) + '].')

    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, type, value, traceback):
        self.complete()
        self.join()

    def run(self):
        try:
            totalWait = 0        
            while True:
                if self.doWork:
                    self.rootLogger.info(
                        'Sending CONTINUE response to keep thread [' + str(self.forThread) + '] alive.')
                    self.httpRequestHandler.send_response_only(100)
                    self.httpRequestHandler.end_headers()
                else:
                    break
                if self.exit_flag.wait(timeout=TIME_PERIOD):
                    break
                totalWait = totalWait + TIME_PERIOD
                if totalWait >= MAX_TIMEOUT:
                    self.wasTimeout = True
                    self.rootLogger.info('Thread [' + str(self.forThread) +'] waited for too long. Terminating.')
                    self.complete()
        except Exception as ex:
            self.rootLogger.exception('Exception: ' + str(ex))

        finally:
            self.rootLogger.info('Exiting KeepAliveWorkerThread for thread [' +
                        str(self.forThread) + '].')

            if self.guestfishPid:
                self.rootLogger.info('Killing GuestFish PID ' + str(self.guestfishPid))
                os.kill(self.guestfishPid, signal.SIGTERM)

    def complete(self):
        self.doWork = False
        self.exit_flag.set()
