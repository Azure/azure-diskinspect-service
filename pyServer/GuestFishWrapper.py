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
from GuestFS import GuestFS

"""
LibGuestFS Wrapper for Disk Information Extraction 

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

    def __init__(self, rootLogger, handler, storageUrl, outputDirName, operationId, mode):
        self.environment = None
        self.httpRequestHandler = handler
        self.storageUrl = storageUrl
        self.outputDirName = outputDirName + os.sep + operationId
        self.rootLogger = rootLogger
        self.mode = mode 

    def __enter__(self):
        self.outputFileName = self.execute(self.storageUrl)
        return self.outputFileName

    def __exit__(self, type, value, traceback):
        if (os.path.exists(self.outputDirName)):
            self.rootLogger.info('Removing: ' + self.outputDirName)
            shutil.rmtree(self.outputDirName)

        if (os.path.exists(self.outputFileName)):
            self.rootLogger.info('Removing: ' + self.outputFileName)
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

        osMountpointsStrArr = list()
        for mp in osMountpoints:
            osMountpointsStrArr.append(str(mp[0]) + ": " + str(mp[1]))
        self.WriteToResultFileWithHeader(operationOutFile, "Mount Points:", osMountpointsStrArr)

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
            with GuestFS(self.rootLogger, storageUrl) as guestfish:
                
                # Initialize
                guestfish.launch()

                # Enumerate file systems
                fsList = guestfish.list_filesystems()
                fsDetailsArr = list()
                for eachDevice in fsList:
                    uuid = guestfish.get_uuid(eachDevice[0])
                    fsDetailsArr.append(str(eachDevice[0]) + ': ' + str(eachDevice[1]) + ' [uuid=' + str(uuid) + ']')
                self.WriteToResultFileWithHeader(operationOutFile, "Filesystem Status:", fsDetailsArr)

                # Enumerate devices identified as OS disks
                inspectList = guestfish.inspect_os()
                self.WriteToResultFileWithHeader(operationOutFile, "Inspection Status:", inspectList)

                deviceNumber = 0
                for device in inspectList:
                    self.rootLogger.info('GuestFish:Examining Device> %s', device)

                    # Gather and Write Inspect Metadata about the Device
                    (osType, osDistribution, osProductName, osMountpoints) = self.GetInspectMetadata(guestfish, device)
                    self.WriteInspectMetadataToResultFile(operationOutFile, device, osType, osDistribution, osProductName, osMountpoints)

                    try:
                        # Mount all identified mount points
                        canProceedAfterMount = False
                                                
                        for mount in osMountpoints:
                            mountpoint = mount[0]
                            mountdevice = mount[1]
                            wasMounted = guestfish.mount_ro(mountpoint, mountdevice)

                            if not wasMounted:
                                self.WriteToResultFile(operationOutFile, "Mounting " + mountdevice + " on " + mountpoint + " FAILED.")

                                # Ignore and continue to next device
                                continue
                            else:
                                canProceedAfterMount = True
                                self.WriteToResultFile(operationOutFile, "Mounting " + mountdevice + " on " + mountpoint + " SUCCEEDED.")

                        if not canProceedAfterMount:
                            self.WriteToResultFile(operationOutFile, "No mount points can be mounted on this device.\r\n")
                            continue
                        else:
                            self.WriteToResultFile(operationOutFile, "\r\n")

                        manifestFile = "/etc/azdis/" + self.mode.lower()
                        operationNumber = 0
                        with open(manifestFile) as operationManifest:
                            contents = operationManifest.read().splitlines()
                            totalOperations = len(contents)
                            self.rootLogger.info("Reading manifest file from " + manifestFile + " with " + str(totalOperations) + " operation entries.")
                            for operation in contents:
                                operationNumber = operationNumber + 1
                                self.rootLogger.info("Executing Operation [" + str(operationNumber) + "/" + str(totalOperations) + "]: " + str(operation))                            
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

                                    fileList = guestfish.glob_expand(gatherItem)
                                    if len(fileList) < 1:
                                        self.WriteToResultFile(operationOutFile, "Copying " + gatherItem + " FAILED as no files were located.")
                                    else:
                                        for eachFile in fileList:
                                            # Determine Output Folder
                                            dirPrefix = os.path.dirname(eachFile)
                                            targetDir = requestDir + os.sep + 'device_' + str(deviceNumber) + dirPrefix

                                            # Create Output Folder if needed
                                            if not (os.path.exists(targetDir)):
                                                os.makedirs(targetDir)

                                            # Copy 
                                            wasCopied = guestfish.copy_out(eachFile, targetDir)
                                            if wasCopied:
                                                self.WriteToResultFile(operationOutFile, "Copying " + eachFile + " SUCCEEDED.")
                                            else:
                                                self.WriteToResultFile(operationOutFile, "Copying " + eachFile + " FAILED.")
                    finally:
                        # Unmount all mountpoints
                        guestfish.unmount_all()

                deviceNumber = deviceNumber + 1

        archiveName = shutil.make_archive(requestDir, 'zip', requestDir)
        return archiveName
