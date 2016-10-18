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

    def callGF(self, echoStr, commands, continueOnError=False):
        start_time = datetime.now()
        try:
            retArgs = self.buildGFArgs(commands)
            self.rootLogger.info('GuestFish:' + echoStr + ':Remote> ' + ' '.join(retArgs))

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
        self.rootLogger.info('GuestFish:Create:Local> ' + ' '.join(args))

        # Guestfish server mode returns a string of the form
        #   GUESTFISH_PID=pid; export GUESTFISH_PID
        # We need to parse this and extract out the GUESTFISH_PID
        # environment variable and inserting it into the subsequent env
        
        output = subprocess.check_output(args, env=self.environment, universal_newlines=True)

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
        for eachDevice in out:    
            eachDeviceArr = eachDevice.split(':')
            device = str(eachDeviceArr[0])
            devicefs = str(eachDeviceArr[1]).strip()
            devicesArr.append( [ device, devicefs ] )        
        return devicesArr

    def get_uuid(self, device):
        (out, err) = self.callGF('Get UUID [' + device + ']', ['--', 'get-uuid', device], True)
        return out[0]

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
            eachMountPointArr = eachMountPoint.split(':')
            mountpoint = str(eachMountPointArr[0])
            mountdevice = str(eachMountPointArr[1]).strip()
            mountpointsArr.append( [ mountpoint, mountdevice ] )
        
        def getKey(item):
            return len(item[0])

        mountpointsArrSorted = sorted(mountpointsArr, key=getKey)

        return mountpointsArr

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
            if err:
                return False
        except subprocess.CalledProcessError:
            return False
        return True

    def ll(self, directory):
        try:
            (out, err) = self.callGF('List(verbose) [' + directory + ']', ['--', '-ll', directory], True)
            if err:
                return None
        except subprocess.CalledProcessError:
            return None
        return out

    def copy_out(self, sourceFiles, targetDir):
        try:
            (out, err) = self.callGF('Copy [' + sourceFiles + ']', ['--', '-glob', 'copy-out', sourceFiles, targetDir], True)
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
