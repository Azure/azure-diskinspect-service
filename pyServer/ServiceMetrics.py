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