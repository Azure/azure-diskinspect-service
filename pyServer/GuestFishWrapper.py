#!/usr/bin/python3

import shutil
import os
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
    kpThread = None

    def __init__(self, rootLogger, handler, storageUrl, outputDirName, operationId, mode, modeMajorSkipTo, modeMinorSkipTo, kpThread):
        self.environment = None
        self.httpRequestHandler = handler
        self.storageUrl = storageUrl
        self.outputDirName = outputDirName + os.sep + operationId
        self.rootLogger = rootLogger
        self.mode = mode 
        self.modeMajorSkipTo = modeMajorSkipTo
        self.modeMinorSkipTo = modeMinorSkipTo
        self.kpThread = kpThread

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

        lastGoodOperationMajorStep = 1
        lastGoodOperationMinorStep = 1

        with open(operationOutFilename, "w", newline="\r\n") as operationOutFile:
            with GuestFS(self.rootLogger, storageUrl) as guestfish:
                self.kpThread.guestfishPid = guestfish.pid
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
                    if (self.kpThread.wasTimeout == True):
                        break

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

                        manifestFile = "/etc/azdis/" + osType + os.sep + self.mode.lower()
                        if not os.path.isfile(manifestFile):
                            self.rootLogger.warning("Manifest file " + manifestFile + " could not be located.")
                            self.WriteToResultFile(operationOutFile, "No manifest exists for " + osType.lower() + " " + self.mode.lower() + " mode data collection.")
                            continue
                        self.WriteToResultFile(operationOutFile, "Using manifest: " + self.mode.lower())
                        operationNumber = 0
                        with open(manifestFile) as operationManifest:
                            contents = operationManifest.read().splitlines()
                            totalOperations = len(contents)
                            timedOut = False
                            self.rootLogger.info("Reading manifest file from " + manifestFile + " with " + str(totalOperations) + " operation entries.")
                            for operation in contents:
                                if (self.kpThread.wasTimeout == True):
                                    if timedOut:
                                        break;
                                    lastGoodOperationMajorStep = operationNumber
                                    lastGoodOperationMinorStep = 1
                                    break

                                operationNumber = operationNumber + 1
                                if (operationNumber < self.modeMajorSkipTo):
                                    strMsg = "Skipping Operation [" + str(operationNumber) + "/" + str(totalOperations) + "]: " + str(operation)
                                    self.rootLogger.warning(strMsg)
                                    self.WriteToResultFile(operationOutFile, strMsg)
                                    continue

                                strMsg = "Executing Operation [" + str(operationNumber) + "/" + str(totalOperations) + "]: " + str(operation)
                                self.WriteToResultFile(operationOutFile, strMsg)
                                self.rootLogger.info(strMsg)

                                opList = operation.split(',')

                                if len(opList) < 2:
                                    continue
                                
                                opCommand = str(opList[0]).lower()
                                opParam1 = opList[1]

                                if opCommand=="echo":
                                    self.WriteToResultFile(operationOutFile, opParam1)
                                elif opCommand=="ll":
                                    directory = opParam1
                                        
                                    dirList = []
                                    if directory:
                                        dirList = guestfish.ll(directory)
                                    if dirList:
                                        self.WriteToResultFileWithHeader(operationOutFile, "Listing contents of " + directory + ":", dirList)
                                    else:
                                        self.WriteToResultFile(operationOutFile, "Directory " + directory + " is not valid.")
                                elif opCommand=="copy":
                                    gatherItem = opParam1
                                    origGatherItem = gatherItem

                                    fileList = []
                                    if gatherItem:
                                        fileList = guestfish.glob_expand(gatherItem)
                                    if len(fileList) < 1:
                                        self.WriteToResultFile(operationOutFile, "Copying " + origGatherItem + " FAILED as no files were located.")
                                    else:
                                        fileNumber = 0
                                        for eachFile in fileList:
                                            if (self.kpThread.wasTimeout == True):
                                                lastGoodOperationMajorStep = operationNumber
                                                lastGoodOperationMinorStep = fileNumber
                                                timedOut = True
                                                break
                                            fileNumber = fileNumber + 1
                                            strStepDescription = str(operationNumber) + "." + str(fileNumber)
                                            if (operationNumber == self.modeMajorSkipTo):
                                                if (fileNumber < self.modeMinorSkipTo):
                                                    strMsg = "Skipping Copy Step [" + str(strStepDescription) + "]"
                                                    self.rootLogger.warning(strMsg)
                                                    self.WriteToResultFile(operationOutFile, strMsg)
                                                    continue

                                            actualFileName = eachFile

                                            # Determine Output Folder
                                            dirPrefix = os.path.dirname(actualFileName)
                                            targetDir = requestDir + os.sep + 'device_' + str(deviceNumber) + dirPrefix

   
                                            # Create Output Folder if needed
                                            if not (os.path.exists(targetDir)):
                                                os.makedirs(targetDir)

                                            # Copy 
                                            wasCopied = guestfish.copy_out(actualFileName, targetDir)
                                            
                                            if wasCopied:
                                                self.WriteToResultFile(operationOutFile, "Copying Step [" + strStepDescription + "] File: " + actualFileName + " SUCCEEDED.")
                                            else:
                                                self.WriteToResultFile(operationOutFile, "Copying Step [" + strStepDescription + "] File: " + actualFileName + " FAILED.")
                    finally:
                        # Unmount all mountpoints
                        guestfish.unmount_all()

                    deviceNumber = deviceNumber + 1
            self.kpThread.guestfishPid = None
            if (self.kpThread.wasTimeout):
                strLastGoodStep = str(lastGoodOperationMajorStep) + "." + str(lastGoodOperationMinorStep)
                self.WriteToResultFile(operationOutFile, "\r\n##### WARNING: Partial results were collected as the operation was taking too long to complete. Consider retrying the operation specifying skip to step " + strLastGoodStep + " to continue gathering from last succesfully executed data collection step. #####")

        archiveName = shutil.make_archive(requestDir, 'zip', requestDir)
        return archiveName
