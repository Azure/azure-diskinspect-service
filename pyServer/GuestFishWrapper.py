#!/usr/bin/python3

import shutil
import os
from GuestFS import GuestFS
from GuestFS_registry import GuestFS_Registry
from datetime import datetime
import zipfile
import urllib
import subprocess
import csv
from collections import defaultdict
import signal
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

    def __init__(self, rootLogger, handler, storageUrl, outputDirName, operationId, mode, modeMajorSkipTo, modeMinorSkipTo, kpThread, runWithCredscan):
        self.environment = None
        self.httpRequestHandler = handler
        self.storageUrl = storageUrl
        self.operationId = operationId
        self.outputDirName = outputDirName + os.sep + operationId
        self.rootLogger = rootLogger
        self.mode = mode 
        self.modeMajorSkipTo = modeMajorSkipTo
        self.modeMinorSkipTo = modeMinorSkipTo
        self.kpThread = kpThread
        self.runWithCredscan = runWithCredscan
        self.osType = "unknown"
        self.operationOutFilename = self.outputDirName + os.sep + 'results.txt'
        self.registryFilename= self.outputDirName + os.sep + 'registry.json'
        # The registry object has a small cache, try to persist across calls to the same VM partition
        self.guest_registry = None
        self.has_registry_file = False
        self.metadata_pairs = {}
        self.outputFileName = ""

    def __enter__(self):
        return self

    def start(self):
        self.outputFileName = self.execute(self.storageUrl)        

    def __exit__(self, type, value, traceback):
        if (os.path.exists(self.outputDirName)):
            self.rootLogger.info('Removing: ' + self.outputDirName)
            shutil.rmtree(self.outputDirName)

        if (os.path.exists(self.outputFileName)):
            self.rootLogger.info('Removing: ' + self.outputFileName)
            os.remove(self.outputFileName)

    def WriteToResultFileWithHeader(self, operationOutFile, headerString, data):
        operationOutFile.write(headerString + '\r\n')
        self.WriteToResultFile(operationOutFile, data)

    def WriteToResultFile(self, operationOutFile, data):
        if (isinstance(data, list)):
            tempStr = "\r\n".join(data)
        else:
            tempStr = str(data)
        operationOutFile.write(tempStr)
        if len(tempStr) > 0:
            self.rootLogger.info("OperationalLog: " + tempStr)  # ensure it is added to telemetry
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
        start_time = datetime.now()
        self.rootLogger.info("Starting zip archiving.")
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
        successElapsed = datetime.now() - start_time
        self.rootLogger.info('Zip archiving completed succesfully in ' + str(successElapsed.total_seconds()) + "s.")
        return zipFilename

    def RunCredentialScanner(self, targetDir, operationOutFile):
        if not os.path.exists("/CS_Latest/tools/CredentialScanner.exe"):
            strMsg = "CredentialScanner: Executable not found, skipping step."
            self.rootLogger.warning(strMsg)
            return
        
        # Get target directory size and count for statistics
        scanned_directory_size = 0
        scanned_files_count = 0
        try:
            for dirpath, dirnames, filenames in os.walk(targetDir):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    scanned_directory_size += os.path.getsize(filepath)
                    scanned_files_count += 1
        except:
            strMsg = "CredentialScanner: Could not get directory size or file count."
            self.rootLogger.warning(strMsg)

        step_start_time = datetime.now()
        output_file = targetDir + "/credscan"
        credscan_results_file = output_file + "-matches.tsv"
        try:
            # Check for timeout before starting process
            if self.kpThread.wasTimeout:
                strMsg = "CredentialScanner: Timed out as inspection processing time limit exceeded."
                self.rootLogger.warning(strMsg)
                return

            # Run credential scanner
            bash_command = ["mono", "--runtime=v4.0", "/CS_Latest/tools/CredentialScanner.exe", "-I", targetDir, "-S", "/CS_Latest/tools/Searchers/diskinspectsearchers.xml", "-O", output_file]
            strMsg = "CredentialScanner: START Scan, running: {}".format(' '.join(bash_command))
            self.WriteToResultFile(operationOutFile, strMsg)

            credscan_process = subprocess.Popen(bash_command)
            self.kpThread.credscanPid = credscan_process.pid
            credscan_process.wait(timeout=600)
            self.kpThread.credscanPid = None
        except subprocess.TimeoutExpired:
            strMsg = "CredentialScanner: Timed out as scanning step time limit exceeded."
            self.rootLogger.warning(strMsg)
            if not os.path.isfile(credscan_results_file):
                return
        except:
            strMsg = "CredentialScanner: Failed to run due to an unexpected exception."
            self.rootLogger.warning(strMsg)
            return
        else:
            # Check for errors
            exit_code = credscan_process.returncode
            step_end_time = datetime.now()
            duration_seconds = (step_end_time - step_start_time).seconds

            # Negative value indicates that child was terminated by signal
            if exit_code < 0:
                signal_name = signal.Signals(-1 * exit_code).name
                if signal_name == signal.SIGTERM.name:
                    strMsg = "CredentialScanner: Timed out as inspection processing time limit exceeded."
                    # Check if any secrets have been found
                    if not os.path.isfile(credscan_results_file):
                        strMsg += " [Operation duration {} seconds]".format(duration_seconds)
                        self.rootLogger.warning(strMsg)
                        return
                    else:
                        self.rootLogger.warning(strMsg)
                else:
                    # Replace code with signal_name for logging
                    exit_code = signal_name

            if exit_code != 0 and exit_code != signal.SIGTERM.name:
                # Check if any secrets have been found
                if not os.path.isfile(credscan_results_file):
                    strMsg = "CredentialScanner: Failed to run, returned exit code {}. [Operation duration {} seconds]".format(exit_code, duration_seconds)
                    self.rootLogger.warning(strMsg)
                    return
                else:
                    strMsg = "CredentialScanner: Returned exit code {}".format(exit_code)
                    self.rootLogger.warning(strMsg)

        # Remove found secrets from files
        self.rootLogger.info("OperationalLog: CredScan completed. Proceeding with redacting.")
        redacted_file_secrets = {}
        removed_file_secrets = {}
        with open(credscan_results_file, encoding='utf-8', errors='replace') as tsv:
            # Skip the first header line
            next(tsv)
            for line in csv.reader(tsv, delimiter='\t'):
                source_file = line[1]
                secret_found = line[2]
                line_number = line[4]
                is_redacted = False
                try:
                    # Remove secret - delete line for small files, entire file for large files
                    if os.path.isfile(source_file):
                        if os.path.getsize(source_file) < 1000000:
                            is_redacted = True
                            with open(source_file, "r+", encoding='utf-8') as f:
                                lines = f.readlines()
                                f.seek(0)
                                for i, line in enumerate(lines):
                                    if (i+1) != int(line_number):
                                        f.write(line)
                                    else:
                                        f.write("***REDACTED***")
                                f.truncate()
                        else:
                            os.remove(source_file)
                except Exception as e:
                    strMsg = "CredentialScanner: Failed to run due to {}".format(e)
                    self.rootLogger.warning(strMsg)
                # Strip out the common target dir for logging
                relative_source_file = source_file.replace(targetDir + "/", "")
                # Store additional details for logging
                if is_redacted:
                    if relative_source_file not in redacted_file_secrets:
                        redacted_file_secrets[relative_source_file] = defaultdict(int)
                    redacted_file_secrets[relative_source_file][secret_found] += 1
                else:
                    if relative_source_file not in removed_file_secrets:
                        removed_file_secrets[relative_source_file] = defaultdict(int)
                    removed_file_secrets[relative_source_file][secret_found] += 1

        num_secret_files = len(redacted_file_secrets.keys()) + len(removed_file_secrets.keys())
        num_removed_files = len(removed_file_secrets.keys())

        # No errors, include file removal in duration
        step_end_time = datetime.now()
        duration_seconds = (step_end_time - step_start_time).seconds

        strMsg = "CredentialScanner: Statistics - No. Scanned Files: {}, Scanned Directory Size: {}, Operation duration: {} seconds, No. Files Containing Secrets: {}, No. Files Removed: {}, Redacted File List: [{}], Removed File List: [{}]".format(scanned_files_count, scanned_directory_size, duration_seconds, num_secret_files, num_removed_files, ', '.join(redacted_file_secrets.keys()), ', '.join(removed_file_secrets.keys()))
        self.WriteToResultFile(operationOutFile, strMsg)
        if num_secret_files > 0:
            # Detailed output on secrets found
            for redacted_file, secret_dict in redacted_file_secrets.items():
                secrets_string = ["{} {}".format(secret, count) for secret, count in secret_dict.items()]
                strMsg = "CredentialScanner: Detailed - Redacted File: {}, Secrets: [{}]".format(redacted_file, ', '.join(secrets_string))
                self.rootLogger.info(strMsg)
            for removed_file, secret_dict in removed_file_secrets.items():
                secrets_string = ["{} {}".format(secret, count) for secret, count in secret_dict.items()]
                strMsg = "CredentialScanner: Detailed - Removed File: {}, Secrets: [{}]".format(removed_file, ', '.join(secrets_string))
                self.rootLogger.info(strMsg)
        else:
            # No files removed - delete output file
            os.remove(credscan_results_file)

    def execute(self, storageUrl):
        found_any_items= False
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
                self.output_request_metadata(operationOutFile, guestfish)
                # Initialize
                guestfish.launch()

                # Enumerate file systems
                fsList = guestfish.list_filesystems()
                fsDetailsArr = list()
                
                # create a dict with a list of values to track the filesystem types
                file_system_types = {}
                for eachDevice in fsList:
                    uuid = guestfish.get_uuid(eachDevice[0])
                    fsDetailsArr.append(str(eachDevice[0]) + ': ' + str(eachDevice[1]) + ' [uuid=' + str(uuid) + ']')
                    # track the type of file system
                    if ( eachDevice[1] in file_system_types):
                        file_system_types[ eachDevice[1] ].append(str(eachDevice[0]))  # append to existing list
                    else:
                        file_system_types[ eachDevice[1] ]= [ str(eachDevice[0]) ]      # create new list

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
                
                # if the inspectList is empty then libGuestFS could not determine the OS of the target, rather
                # than fail, lets try to make an educated guess for OS and try to gather data from the known filesystems using that manifest
                if ( len(inspectList)  == 0 ):
                    defaultOsType= self.guess_OS_by_filesystems(fsList)
                    skipInspect = True 
                    inspectList = [fs[0] for fs in fsList]
                    self.WriteToResultFile(operationOutFile, "Automatic detection of OS failed... guessing OS type of: " + defaultOsType)
        
                deviceNumber = 0
                for device in inspectList:
                    if (self.kpThread.wasTimeout == True):
                        break

                    osType = osDistribution = osProductName = None
                    self.rootLogger.info('GuestFish:Examining Device> %s', device)

                    if (not skipInspect):
                        # Gather and Write Inspect Metadata about the Device
                        (osType, osDistribution, osProductName, osMountpoints) = self.GetInspectMetadata(guestfish, device)
                        self.WriteInspectMetadataToResultFile(operationOutFile, device, osType, osDistribution, osProductName, osMountpoints)
                        # ensure that the device is actually in that list...
                        if not device in [ mp[1] for mp in osMountpoints ]  :
                            osMountpoints.append( ["/", device] )
                    else:
                        osType = defaultOsType
                        osMountpoints = [ ["/", device] ]
                    self.osType = str(osType)
                    
                    #set http headers
                    if (osType is not None):
                      self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_OPERATING_SYSTEM] = osType
                    if (osDistribution is not None):
                        self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_OS_DISTRIBUTION] = osDistribution
                    if (osProductName is not None):
                        self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_PRODUCT_NAME] = osProductName

                    self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_PARTIAL_RESULT] = "false"

                    try:
                        # Mount all identified mount points
                        canProceedAfterMount = False
                                                
                        for mount in osMountpoints:
                            mountpoint = mount[0]
                            mountdevice = mount[1]
                            
                            # special case ufs on FreeBSD
                            if ('ufs' in file_system_types and file_system_types['ufs'].count(mountdevice)>0):
                                # sometimes libguestFS detects FreeBSD as linux.  If we have ufs it likely is a *BSD
                                if (osType.lower() == 'linux'):
                                    self.WriteToResultFile(operationOutFile, "Found ufs filesystem, switching OS type to FreeBSD instead of Linux")
                                    osType = 'freebsd'
                                self.WriteToResultFile(operationOutFile, "Attempting to mount ufs...")
                                wasMounted = guestfish.mount_ufs(mountpoint, mountdevice)
                            else:
                                wasMounted = guestfish.mount_ro(mountpoint, mountdevice)

                            if not wasMounted:
                                self.WriteToResultFile(operationOutFile, "Mounting " + mountdevice + " on " + mountpoint + " FAILED.")

                                # Ignore and continue to next device
                                continue
                            else:
                                canProceedAfterMount = True
                                self.WriteToResultFile(operationOutFile, "Mounting " + mountdevice + " on " + mountpoint + " SUCCEEDED.")
                                self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_DISK_CONFIGURATION]="Standard"

                        if not canProceedAfterMount:
                            self.WriteToResultFile(operationOutFile, "No mount points can be mounted on this device.\r\n")
                            continue
                        else:
                            self.WriteToResultFile(operationOutFile, "\r\n")

                        # some Linux distros create an overlay from elsewhere. guestfish doesn't appear to have a chroot or mount -B option
                        pathPrefix = ""
                        if (osType.lower() == "linux"):
                            pathPrefix = self.get_file_path_prefix(guestfish)
                            if (len(pathPrefix) > 0) :
                                self.rootLogger.info("Adding prefix to path: " + pathPrefix )
                        
                        parentFolder = "/etc/azdis/"
                        manifestFile = parentFolder + osType + os.sep + self.mode.lower()
                        if not os.path.isfile(manifestFile):
                            self.rootLogger.warning("Manifest file " + manifestFile + " could not be located.")
                            if not os.path.isdir(parentFolder + osType):
                                # Can happen if libguestFS returns an OS we don't have manifests for (e.g. NetBSD or Solaris)
                                guessed_os= self.guess_OS_by_filesystems(fsList)
                                self.WriteToResultFile(operationOutFile, "No manifests for OS '{0}', trying '{1}'...".format(osType,guessed_os) )
                                manifestFile = parentFolder + osType + os.sep + self.mode.lower()
                            if not os.path.isfile(manifestFile):
                                # bad manifest, try normal
                                self.WriteToResultFile(operationOutFile, "No manifest exists for " + osType.lower() + " '" + self.mode.lower() + "' mode data collection. Trying 'normal' manifest...")
                                self.mode = "normal"
                                manifestFile = parentFolder + osType + os.sep + self.mode.lower()  #this should work...

                        self.WriteToResultFile(operationOutFile, "Using manifest: " + self.mode.lower() + "  [" + osType.lower() + "]" )
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
                                opParam1 = pathPrefix + opList[1].strip()

                                if (osType.lower() == "windows"):
                                    opParamWin = guestfish.case_sensitive_path(opParam1)
                                    if (opParamWin is not None):
                                        opParam1 = opParamWin

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
                                                found_any_items= True
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

                if not found_any_items:   # no items found
                    self.WriteToResultFile(operationOutFile, "No manifest items were found.")
                    self.check_for_disk_encryption(file_system_types, guestfish, operationOutFile)

                execution_end_time = datetime.now()
                duration_seconds = (execution_end_time - execution_start_time).seconds
                self.WriteToResultFile(operationOutFile, "Execution end time: " + execution_end_time.strftime('%H:%M:%S') + "  [Execution duration: " + str(duration_seconds) + " seconds]\r\n")

            self.kpThread.guestfishPid = None
            if (self.kpThread.wasTimeout):
                strLastGoodStep = str(lastGoodOperationMajorStep) + "." + str(lastGoodOperationMinorStep)
                self.WriteToResultFile(operationOutFile, "\r\n##### WARNING: Partial results were collected as the operation was taking too long to complete. Consider retrying the operation specifying skip to step " + strLastGoodStep + " to continue gathering from last succesfully executed data collection step. #####")
                self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_PARTIAL_RESULT] = "true"

            # Scan results for secrets
            if self.runWithCredscan:
                self.RunCredentialScanner(requestDir, operationOutFile)

        self.rootLogger.info("Current working directory: " + str(os.getcwd()))     

        # Build the result output archive
        zipFileName = requestDir + ".zip"
        archiveFile = self.CreateArchive(zipFileName, requestDir)
        return archiveFile


    def do_opcommand_registry(self, guestfish, registry_path, operationOutFile): 
        with open(self.registryFilename, "a", newline="\n") as registryOutFile:
            registryValue = self.guest_registry.reg_read(registry_path)
            if (registryValue != None):
                found_any_items= True
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
            found_any_items= True
        else:
            self.WriteToResultFile(operationOutFile, "Directory " + directory + " is not valid.")



    """
    Today, libguestFS has some support for Linux guests encrypted according to the Linux Unified Key Setup (LUKS) standard.  Currently only LVM-on-LUKS is supported
    The Azure disk encryption service for Linux is supported and non-LVM partitions as well as using Bitlocker on Windows.  Additionally, 3rd party Azure Marketplace publishers
    may choose other encryption schemas for their images (most common in appliances).  To provide more insight to the caller from the guest, we need to use a heuristic approach.

    For Windows: look for >0 unknown partitions & >0 ntfs partitions.  If a ntfs partition contains Boot, but none contain Windows, then this is likely encryption
    For Linux: look for >0 unknown partitions & >0 non-ntfs unencrypted.  If a non-ntfs unencrypted contains grub | kernel | vmlinuz; but none contain /var or /etc then this is likely encryption
    """
    def check_for_disk_encryption(self, file_system_types, guestfish, operationOutFile):
        found_linux_boot = False
        found_linux_OS = False
        found_windows_boot = False
        found_windows_OS = False
        if 'unknown' in file_system_types:  
                mountpoint = '/'
                # review all the non-unknown partitions
                for fs_type in file_system_types:
                    if fs_type == 'unknown':
                        continue
                    for partition in file_system_types[fs_type]:
                        wasMounted = guestfish.mount_ro(mountpoint, partition)
                        if wasMounted:
                            dirList = guestfish.ll(mountpoint)     # list the root
                            for line in dirList:
                                if fs_type == 'ntfs' and line.endswith("Boot"):
                                    found_windows_boot = True
                                if fs_type == 'ntfs' and line.endswith("Windows"):
                                     found_windows_OS = True
                                if fs_type != 'ntfs' and any( s in line for s in ['grub','vmlinuz','kernel'] ):
                                    found_linux_boot = True
                                if fs_type != 'ntfs' and any( s in line for s in ['etc','var'] ):
                                     found_linux_OS = True
                            guestfish.unmount(mountpoint)

                # put the logic together
                found_windows_encryption = False
                found_linux_encryption = False
                if found_windows_boot and not ( found_windows_OS or found_linux_boot or found_linux_OS): 
                    self.WriteToResultFile(operationOutFile, "Encryption found: This Windows operating system disk appears to be encrypted.")
                    found_windows_encryption = True
                    self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_OPERATING_SYSTEM] = "windows"

                if found_linux_boot and not ( found_linux_OS or found_windows_boot or found_windows_OS): 
                    self.WriteToResultFile(operationOutFile, "Encryption found: This Linux operating system disk appears to be encrypted.")
                    found_linux_encryption = True
                    self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_OPERATING_SYSTEM] = "linux"
    
                if found_windows_encryption or found_linux_encryption:
                    self.metadata_pairs[DiskInspectionMetadata.INSPECTION_METADATA_DISK_CONFIGURATION]="Encrypted"
                    self.WriteToResultFile(operationOutFile, "*** Disk inspection does not currently support disk encryption. Please work with customer to use another data collection method. ***")
    
    """
    LibGuestFS has filed to determine the OS.  If possible we'd still like to try to gather data.  Try to determine the OS so we know which manifest to run.
    Note: if a OS is returned from this function is it a requirement that it have at least a 'normal' manifest
    """
    def guess_OS_by_filesystems(self, file_systems_list):
        for fs_entry in file_systems_list:
            if "ntfs"in fs_entry:
                return "windows"       
            elif "ufs" in fs_entry:
                return "freebsd"
        
        # other fstypes running in Azure are likely Linux
        return "linux" 

    """
    Special case any overlay file systems
    """
    def get_file_path_prefix(self, guestfish):
        # UbuntuCore
        if ( guestfish.is_dir('/system-data') ):
            self.rootLogger.info('get_file_path_prefix: Found /system-data, this might be an UbuntuCore image...')
            return '/system-data'

        return ""

    """
    Add metadata about the request to the operational log
    """
    def output_request_metadata(self, operationOutFile, guestfish):
        self.WriteToResultFile(operationOutFile,"========== Request Info ==========")
        urlObj = urllib.parse.urlparse(self.storageUrl)
        self.WriteToResultFile(operationOutFile, "Storage Acct: " + urlObj[1] )
        self.WriteToResultFile(operationOutFile, "Container/Vhd: " + urlObj[2] )
        self.WriteToResultFile(operationOutFile, "Manifest requested: " + self.mode.lower() )
        self.WriteToResultFile(operationOutFile, "Inspect service Operational ID: " + self.operationId )
        self.WriteToResultFile(operationOutFile, "Guestfish version: " + guestfish.libguestfs_version() )
        self.WriteToResultFile(operationOutFile,"========== End Request Info ==========\r\n")


class DiskInspectionMetadata:
    INSPECTION_METADATA_OPERATING_SYSTEM = "InspectionMetadata-Operating-System"
    INSPECTION_METADATA_DISK_CONFIGURATION = "InspectionMetadata-Disk-Configuration"
    INSPECTION_METADATA_OS_DISTRIBUTION = "InspectionMetadata-OS-Distribution"
    INSPECTION_METADATA_PRODUCT_NAME = "InspectionMetadata-Product-Name"
    INSPECTION_METADATA_PARTIAL_RESULT = "InspectionMetadata-Partial-Result"