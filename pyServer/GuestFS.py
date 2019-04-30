#!/usr/bin/python3

import subprocess
import os
import glob
from datetime import datetime
import http.client
import urllib
import socket

"""
LibGuestFS Wrapper

This class is responsible for extracting the required logs and configuration
files from the specified Blob Uri by interacting with the LibGuestFS 
tool that can open disk images and run introspection commands on it.
"""
class GuestFS:
    storageUrl = None
    pid = None
    environment = None

    def __init__(self, rootLogger, storageUrl):
        self.storageUrl = storageUrl
        self.environment = os.environ.copy()
        self.rootLogger = rootLogger

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.exit()

    def buildGFArgs(self, args):
        retArgs = ['/libguestfs/run', 'guestfish', '--remote']
        retArgs.extend(args)
        return retArgs

    def callGF(self, echoStr, commands, continueOnError=False, returnRawResults=False):
        start_time = datetime.now()
        retValue = [None, None]
        try:
            retArgs = self.buildGFArgs(commands)
            self.rootLogger.info('GuestFish:' + echoStr + ':Remote> ' + ' '.join(retArgs))
            
            if returnRawResults:
                result = subprocess.check_output(retArgs,
                    env=self.environment,
                    stderr=subprocess.PIPE,
                    universal_newlines=False)
               
                # avoid doing any kind of str() on data since we can encounder encode/decode errors on binary data
                if result:
                    retValue = [result, None]  #check_output will throw() if there is an error
                    resultStr = "".join("%02x " % b for b in result)
                    self.rootLogger.info('GuestFish:' + echoStr + ':Result> ' + resultStr)
            else:
                proc = subprocess.Popen(
                    retArgs,
                    env=self.environment,
                    stderr=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    universal_newlines=True)
                (result, err) = proc.communicate()  

                resultAsArray = str(result).splitlines()
                retValue = [resultAsArray, err]
                if result:
                    resultStr = '\r\n'.join(resultAsArray)
                    if len(resultAsArray) > 1:
                        resultStr = '\r\n' + resultStr
                        self.rootLogger.info('GuestFish:' + echoStr + ':Result> ' + resultStr)
                if err:
                    if continueOnError:
                        self.rootLogger.warning('GuestFish:' + echoStr + ':Error> \r\n' + err)
                    else:
                        retValue = [None, err]
                        self.rootLogger.error('GuestFish:' + echoStr + ':Error> \r\n' + err)
            return retValue
        except subprocess.CalledProcessError as e:
            if not continueOnError:
                self.rootLogger.error('GuestFish:' + echoStr + ':FAILED')
                raise(e)
            else:
                self.rootLogger.warning('GuestFish:' + echoStr + ':WARNING')
        finally:
            elapsedTime = datetime.now() - start_time
            self.rootLogger.info('GuestFish:' + echoStr + ':Remote> ExecutionTime=' + str(elapsedTime.total_seconds()) + "s.")

    def start(self):
        # Run guestfish in remote mode and then send it a command
        # at a time since the programming environment inside guestfish
        # is very limited (no variables, etc.)

        args = ['/libguestfs/run', 'guestfish', '--listen', '-a', self.storageUrl, '--ro']
        redactedArgs = ['/libguestfs/run', 'guestfish', '--listen', '-a', self.storageUrl.split('?')[0]+'?[saskey]', '--ro']
        self.rootLogger.info('GuestFish:Create:Local> ' + ' '.join(redactedArgs))

        try:
            output = subprocess.check_output(args, env=self.environment, universal_newlines=True)
        except subprocess.CalledProcessError as ex:
            self.rootLogger.error("GuestFish failed to start using the previous sas url, trying to diagnose...")
            self.rootLogger.error("GuestFishStdout: " + str(ex.output))
            output = self.diagnoseStartFailureOrRetry(args)  # this will raise an exception that will be caught in HTTP handler

        # Guestfish server mode returns a string of the form
        #   GUESTFISH_PID=pid; export GUESTFISH_PID
        # We need to parse this and extract out the GUESTFISH_PID
        # environment variable and inserting it into the subsequent env
        try:
            self.pid = int(output.split(';')[0].split('=')[1])
        except Exception as e:
            raise Exception('Cannot find GUESTFISH_PID')

        self.environment['GUESTFISH_PID'] = str(self.pid)
        self.rootLogger.info('GuestFish:PID=' + str(self.pid))

    def launch(self):
        return self.callGF('Launching', ['launch'])
    
    def list_filesystems(self):
        (out, err) = self.callGF('Listing Filesystems', ['list-filesystems'], True)
        devicesArr = list()
        # typically these are name/values delimited by :  
        # some filesystems have a moniker (e.g. btrfsvol:/dev/sda2/root: btrfs ) but the delimeter
        # will be a colon with space ': '. This should be consistent based upon a review of 
        # guestfish code: /fish/fish.c - print_table()
        for eachDevice in out:    
            eachDeviceArr = eachDevice.split(': ')
            device = str(eachDeviceArr[0])
            devicefs = str(eachDeviceArr[1]).strip()
            devicesArr.append( [ device, devicefs ] )        
        return devicesArr

    def get_uuid(self, device):
        (out, err) = self.callGF('Get UUID [' + device + ']', ['--', 'get-uuid', device], True)
        return self.get_first_list_item(out)

    def inspect_os(self):
        (out, err) = self.callGF('Inspecting OS Metadata', ['inspect-os'], True)
        return out

    def inspect_get_type(self, device):
        (out, err) = self.callGF('Get OS Type', ['--', '-inspect-get-type', device], True)
        return out
 
    def inspect_get_distro(self, device):
        (out, err) = self.callGF('Get OS Distribution', ['--', '-inspect-get-distro', device], True)
        return out

    def inspect_get_product_name(self, device):
        (out, err) = self.callGF('Get Product Name', ['--', '-inspect-get-product-name', device], True)
        return out

    def inspect_get_mountpoints(self, device):
        (out, err) = self.callGF('Get Device Mountpoints', ['--', '-inspect-get-mountpoints', device], True)
        mountpointsArr = list()
        for eachMountPoint in out:   
            # delimiter will be a colon with space ': '. This should be consistent based upon  
            # a review of guestfish code: /fish/fish.c - print_table()        
            eachMountPointArr = eachMountPoint.split(': ')
            mountpoint = str(eachMountPointArr[0])
            mountdevice = str(eachMountPointArr[1]).strip()
            mountpointsArr.append( [ mountpoint, mountdevice ] )
        
        def getKey(item):
            return len(item[0])

        mountpointsArrSorted = sorted(mountpointsArr, key=getKey)

        return mountpointsArrSorted

    def unmount(self, mountpoint):
        try:
            (out, err) = self.callGF('Unmount [' + mountpoint + ']', ['--', '-unmount', mountpoint], True)
        except subprocess.CalledProcessError:
            pass

    def unmount_all(self):
        try:
            (out, err) = self.callGF('Unmount All', ['--', '-unmount-all'], True)
        except subprocess.CalledProcessError:
            pass

    def mount_ro(self, mountpoint, device):
        try:
            (out, err) = self.callGF('Mount [' + mountpoint + ',' + device + ']', ['--', '-mount-ro', device, mountpoint], True)
            # guestfish doesn't seem to return anything here... check to see if it is in mounts
            (out, err) = self.callGF('Mount [' + mountpoint + ',' + device + ']', ['--', '-mounts'], True)
            return device in out
        except subprocess.CalledProcessError:
            return False
        return True
        
    """
    Used to mount ufs filesystems on VMs    
    LibGuestFS doesn't automatically determine how to mount; given the prevelance in Azure, we try 5xbsd first (common in FreeBSD images) and then 
        attempt 44bsd which is used in some OpenBSD images
    """
    def mount_ufs(self, mountpoint, device):
        bsd_options = ['ro,ufstype=5xbsd','ro,ufstype=44bsd']
        for current_option in bsd_options:
            try:
                (out, err) = self.callGF('Mount [' + mountpoint + ',' + device + ']', ['--', '-mount-options', current_option, device, mountpoint], True)
                # guestfish doesn't seem to return anything here... check to see if it is in mounts
                (out, err) = self.callGF('Mount [' + mountpoint + ',' + device + ']', ['--', '-mounts'], True)
                if device in out:
                        return True                    
                else:
                        continue
            except subprocess.CalledProcessError:
                return False
        return False

    def ll(self, directory):
        try:
            (out, err) = self.callGF('List(verbose) [' + directory + ']', ['--', '-ll', directory], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return out

    def glob_expand(self, tgtPattern):
        (out, err) = self.callGF('Expanding Pattern [' + tgtPattern + ']', ['--', '-glob-expand', tgtPattern], True)
        if len(out) < 1:
            self.rootLogger.warning('GuestFish:Expanding Pattern [' + tgtPattern + ']:Result> No files found.')
        return out

    def case_sensitive_path(self, path):
        (out, err) = self.callGF('Finding Case Sensitive Path [' + path + ']', ['--', '-case-sensitive-path', path], True)
        return self.get_first_list_item(out)
        

    def copy_out(self, sourceFiles, targetDir):
        try:
            (out, err) = self.callGF('Copy [' + sourceFiles + ']', ['--', '-copy-out', sourceFiles, targetDir], True)
            if err:
                return False
            targetFiles = targetDir + os.sep + os.path.basename(sourceFiles)
            list = glob.glob(targetFiles)
            if len(list) < 1:
                self.rootLogger.warning('GuestFish:Copy [' + sourceFiles + ']:Result> No files copied.')
                return False
        except subprocess.CalledProcessError:
            return False
        return True

    def exit(self):
        return self.callGF('Exiting', ['--', '-exit'])

    
    def df(self):
        try:
            (out, err) = self.callGF('DiskInfo (df -h)', ['--', '-df-h'], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return out

    def statvfs(self, mountpoint):
        try:
            (out, err) = self.callGF('DiskInfo (statvfs)', ['--', '-statvfs', mountpoint], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return out 
        
    def get_drive_letters(self, device):
        try:
            (out, err) = self.callGF('Windows drive letter mappings', ['--', '-inspect-get-drive-mappings', device], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return out
    
    # check the list before we dereference
    def get_first_list_item(self, list_obj):
        if len(list_obj) == 1:
            return list_obj[0]
        else:
            return None

    def is_dir(self, path):
        try:
            (out, err) = self.callGF('Looking for directory', ['--', '-is-dir', path], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return 'true' in out

    def libguestfs_version(self):
        try:
            (out, err) = self.callGF('Getting guestfish/libguestFS version', ['--', '-version'], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None

        def returnValue(s):
            return s.split(':')[1].strip()

        return ".".join(map(returnValue, out))

    '''
    Function attempts to gain better insight into why libGuestFS could not start when targeting a particular sas url
    The resulting diagnosis is used in the HTTP handler to determine which errors indicative of the service being 
    unhealthy and which should not 
    '''
    def diagnoseStartFailureOrRetry(self, args):
        urlObj = urllib.parse.urlparse(self.storageUrl)
        if urlObj.scheme != 'https':
            raise InvalidStorageAccountException("HTTPS connection is required!")
        # Split the host portion from url path & sas
        storageAccountHost = urlObj.netloc
        pathAndSas = urlObj.path + "?" + urlObj.query
        try:
            conn = http.client.HTTPSConnection(storageAccountHost)
            conn.request("GET", pathAndSas)
            resp = conn.getresponse()
            if resp.status == 200:
                # transient failure or issue with libGuestFS. retry, repeat error will throw exception
                self.rootLogger.info("diagnoseStartFailureOrRetry: HTTP check of Sas url returned 200. Retrying GuestFish start...")
                output = subprocess.check_output(args, env=self.environment, universal_newlines=True)
                return output
            else:
                self.rootLogger.warning("diagnoseStartFailureOrRetry: HTTP check of Sas url returned status: " + str(resp.status))
                if resp.status == 404:
                    raise InvalidVhdNotFoundException(resp.reason)
                elif resp.status == 403:
                    raise InvalidSasException(resp.reason)
                else:
                    raise HTTPException("HTTP GET for SaS url returned %s: %s" % (resp.status, resp.reason))
        except socket.gaierror:
            self.rootLogger.error("diagnoseStartFailureOrRetry: HTTP connection to storage account url failed! Account may be invalid.")
            raise InvalidStorageAccountException(storageAccountHost)
        except subprocess.CalledProcessError as ex:
            self.rootLogger.error("GuestFishStdoutAfterRetry: " + str(ex.output))
            # the retry failed, we need to make sure that any sas uri are redacted under error
            for i in range(0, len(ex.cmd) -1):
                location = ex.cmd[i].find('?')
                if location > 0:
                    ex.cmd[i] =ex.cmd[i][0:location] + '?[saskey]'
            raise ex from None # throw the redacted exception which is caught in do_POST() and ends the web request
        finally:
            conn.close()

class InvalidSasException(Exception):
    pass

class InvalidVhdNotFoundException(Exception):
    pass

class InvalidStorageAccountException(Exception):
    pass