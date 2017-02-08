#!/usr/bin/python3

import shutil
import os
from GuestFS import GuestFS
from GuestFS_registry import GuestFS_Registry
from datetime import datetime
import zipfile
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
    osType = None

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
        self.osType = "unknown"
        self.operationOutFilename = self.outputDirName + os.sep + 'results.txt'
        self.registryFilename= self.outputDirName + os.sep + 'registry.json'
        # The registry object has a small cache, try to persist across calls to the same VM partition
        self.guest_registry = None
        self.has_registry_file = False

    def __enter__(self):
        self.outputFileName = self.execute(self.storageUrl)        
        return self

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

    def CreateArchive(self, zipFilename, targetDir):
        with zipfile.ZipFile(zipFilename, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            base_path = os.path.normpath(targetDir)
            for dirpath, dirnames, filenames in os.walk(targetDir):
                for name in sorted(dirnames):
                    path = os.path.normpath(os.path.join(dirpath, name))
                    zf.write(path, os.path.relpath(path, base_path))
                for name in filenames:
                    path = os.path.normpath(os.path.join(dirpath, name))
                    if os.path.isfile(path):
                        zf.write(path, os.path.relpath(path, base_path))        
        return zipFilename

    def execute(self, storageUrl):
        requestDir = self.outputDirName
        os.makedirs(requestDir)

        lastGoodOperationMajorStep = 1
        lastGoodOperationMinorStep = 1

        with open(self.operationOutFilename, "w", newline="\n") as operationOutFile:
            with GuestFS(self.rootLogger, storageUrl) as guestfish:
                self.kpThread.guestfishPid = guestfish.pid
                self.guest_registry = GuestFS_Registry(guestfish, self.rootLogger)
                execution_start_time = datetime.now()
                self.WriteToResultFile(operationOutFile, "Execution start time: " + execution_start_time.strftime('%H:%M:%S') + ".\r\n")

                # Initialize
                guestfish.launch()

                # Enumerate file systems
                fsList = guestfish.list_filesystems()
                fsDetailsArr = list()
                ufs_partitions = list()
                for eachDevice in fsList:
                    uuid = guestfish.get_uuid(eachDevice[0])
                    fsDetailsArr.append(str(eachDevice[0]) + ': ' + str(eachDevice[1]) + ' [uuid=' + str(uuid) + ']')
                    # track if any are ufs
                    if ( str(eachDevice[1]) == "ufs" ):
                        ufs_partitions.append(str(eachDevice[0]))
                        
                self.WriteToResultFileWithHeader(operationOutFile, "Filesystem Status:", fsDetailsArr)

                defaultOsType = None
                skipInspect = False
                # special case a single ntfs device as 'windows'
                if (len(fsList) == 1):
                    eachDevice = fsList[0]
                    if (eachDevice[1] == "ntfs"):
                        defaultOsType="windows"
                        skipInspect = True 

                if (not skipInspect):
                    # Enumerate devices identified as OS disks
                    inspectList = guestfish.inspect_os()
                    self.WriteToResultFileWithHeader(operationOutFile, "Inspection Status:", inspectList)
                else:
                    inspectList = [fsList[0][0]]

                deviceNumber = 0
                for device in inspectList:
                    if (self.kpThread.wasTimeout == True):
                        break

                    self.rootLogger.info('GuestFish:Examining Device> %s', device)

                    if (not skipInspect):
                        # Gather and Write Inspect Metadata about the Device
                        (osType, osDistribution, osProductName, osMountpoints) = self.GetInspectMetadata(guestfish, device)
                        self.WriteInspectMetadataToResultFile(operationOutFile, device, osType, osDistribution, osProductName, osMountpoints)
                    else:
                        osType = defaultOsType
                        osMountpoints = [ ["/", fsList[0][0]] ]
                    self.osType = str(osType)

                    try:
                        # Mount all identified mount points
                        canProceedAfterMount = False
                                                
                        for mount in osMountpoints:
                            mountpoint = mount[0]
                            mountdevice = mount[1]
                            
                            # special case ufs on FreeBSD
                            if (osType == "freebsd" and ufs_partitions.count(mountdevice)>0):
                                self.WriteToResultFile(operationOutFile, "Attempting to mount ufs on FreeBSD...")
                                wasMounted = guestfish.mount_bsd(mountpoint, mountdevice)
                            else:
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

                                operation_start_time = datetime.now()
                                strMsg = operation_start_time.strftime('%H:%M:%S') + "  Executing Operation [" + str(operationNumber) + "/" + str(totalOperations) + "]: " + str(operation)
                                self.WriteToResultFile(operationOutFile, strMsg)
                                self.rootLogger.info(strMsg)

                                opList = operation.split(',')

                                if len(opList) < 2:
                                    continue
                                
                                opCommand = str(opList[0]).lower().strip()
                                opParam1 = opList[1].strip()

                                if opCommand=="echo":
                                    self.WriteToResultFile(operationOutFile, opParam1)
                                elif opCommand=="ll":
                                    self.do_opcommand_list_directory(guestfish, opParam1, operationOutFile)
                          
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
                                                step_result = " SUCCEEDED."
                                            else:
                                                step_result = " FAILED."
                                                
                                            step_end_time = datetime.now()
                                            duration_seconds = (step_end_time - operation_start_time).seconds
                                            strMsg = step_end_time.strftime('%H:%M:%S') + "  Copying Step [" + strStepDescription + "] File: " + actualFileName + step_result + "  [Operation duration: " + str(duration_seconds) + " seconds]"
                                            self.WriteToResultFile(operationOutFile, strMsg)
                                elif opCommand=="diskinfo":  
                                    diskInfoOutFilename = requestDir + os.sep + 'diskinfo.txt'  
                                    with open(diskInfoOutFilename, "a", newline="\r\n") as diskInfoOutFile:                                    
                                        # get drive letters if we ran inspection
                                        if (osType == "windows"):
                                            if (not skipInspect):  
                                                driveMappings = guestfish.get_drive_letters(device)
                                                self.WriteToResultFileWithHeader(diskInfoOutFile, "Windows drive letter mappings:", driveMappings)
                                            else:
                                                self.WriteToResultFileWithHeader(diskInfoOutFile, "Windows drive letter mappings [Inspect skipped]:", "C: " + device)
                                        #df-h
                                        diskInfo = guestfish.df()
                                        self.WriteToResultFile(diskInfoOutFile, diskInfo)
                                        #statvfs                                       
                                        self.WriteToResultFile(diskInfoOutFile, "\r\nFor decoder ring for data below see: http://man.he.net/man2/statvfs \r\n")
                                        for mount in osMountpoints:
                                            mountpoint = mount[0]
                                            mountdevice = mount[1]
                                            diskstats=guestfish.statvfs(mountpoint)
                                            self.WriteToResultFileWithHeader(diskInfoOutFile, "[Device: " + mountdevice + ", mountpoint: " + mountpoint + " ]", diskstats)
                                    step_end_time = datetime.now() 
                                    duration_seconds = (step_end_time - operation_start_time).seconds                                    
                                    strMsg = step_end_time.strftime('%H:%M:%S') + "  DiskInfo gathered and written to diskinfo.txt. [Operation duration: " + str(duration_seconds) + " seconds]"
                                    self.WriteToResultFile(operationOutFile, strMsg)

                                elif opCommand=="reg":
                                     self.do_opcommand_registry(guestfish, opParam1, operationOutFile)

                            # done processing the manifest for this partition, check to see if we need to close
                            self.registry_close() 
        

                    finally:                        
                        # Unmount all mountpoints
                        guestfish.unmount_all()

                    deviceNumber = deviceNumber + 1

                execution_end_time = datetime.now()
                duration_seconds = (execution_end_time - execution_start_time).seconds
                self.WriteToResultFile(operationOutFile, "Execution end time: " + execution_end_time.strftime('%H:%M:%S') + "  [Execution duration: " + str(duration_seconds) + " seconds]\r\n")

            self.kpThread.guestfishPid = None
            if (self.kpThread.wasTimeout):
                strLastGoodStep = str(lastGoodOperationMajorStep) + "." + str(lastGoodOperationMinorStep)
                self.WriteToResultFile(operationOutFile, "\r\n##### WARNING: Partial results were collected as the operation was taking too long to complete. Consider retrying the operation specifying skip to step " + strLastGoodStep + " to continue gathering from last succesfully executed data collection step. #####")

        self.rootLogger.info("Current working directory: " + str(os.getcwd()))

        # Build the result output archive
        zipFileName = requestDir + ".zip"
        archiveFile = self.CreateArchive(zipFileName, requestDir)
        return archiveFile


    def do_opcommand_registry(self, guestfish, registry_path, operationOutFile): 
        with open(self.registryFilename, "a", newline="\n") as registryOutFile:
            registryValue = self.guest_registry.reg_read(registry_path)
            if (registryValue != None):
                if (not self.has_registry_file):
                    self.has_registry_file = True
                    self.WriteToResultFile(registryOutFile,'{')
                    self.WriteToResultFile(registryOutFile,'"' + registry_path.replace("\\","\\\\") + '": "' + registryValue.replace("\\","\\\\") + '"')
                else:
                    #prefix line with comma seperator
                    self.WriteToResultFile(registryOutFile,',"' + registry_path.replace("\\","\\\\") + '": "' + registryValue.replace("\\","\\\\") + '"')
            else:
                self.WriteToResultFile(operationOutFile, registry_path + " could not be read")  

    def registry_close(self):      
        if (self.has_registry_file):
            with open(self.registryFilename, "a", newline="\r\n") as registryOutFile:
                self.WriteToResultFile(registryOutFile,'}')
            self.guest_registry.clean_up()
            self.has_registry_file = False

    def do_opcommand_list_directory(self, guestfish, directory, operationOutFile):
        dirList = []
        if directory:
            dirList = guestfish.ll(directory)
        if dirList:
            step_end_time = datetime.now()
            strMsg = step_end_time.strftime('%H:%M:%S') + "  Listing contents of " + directory + ":"                          
            self.WriteToResultFileWithHeader(operationOutFile, strMsg, dirList)
        else:
            self.WriteToResultFile(operationOutFile, "Directory " + directory + " is not valid.")
