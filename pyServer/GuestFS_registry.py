#!/usr/bin/python3

import shutil
import os
import subprocess
from GuestFS import GuestFS
from enum import IntEnum

# libguestFS enum
class hive_type(IntEnum):
   #/* Just a key without a value */
   hive_t_REG_NONE = 0,
   #/* A Windows string (encoding is unknown, but often UTF16-LE) */
   hive_t_REG_SZ = 1,
   #/* A Windows string that contains %env% (environment variable expansion) */
   hive_t_REG_EXPAND_SZ = 2,
   #/* A blob of binary */
   hive_t_REG_BINARY = 3,
   #/* DWORD (32 bit integer), little endian */
   hive_t_REG_DWORD = 4,
   #/* DWORD (32 bit integer), big endian */
   hive_t_REG_DWORD_BIG_ENDIAN = 5,
   #/* Symbolic link to another part of the registry tree */
   hive_t_REG_LINK = 6,
   #/* Multiple Windows strings.  See http://blogs.msdn.com/oldnewthing/archive/2009/10/08/9904646.aspx */
   hive_t_REG_MULTI_SZ = 7,
   #/* Resource list */
   hive_t_REG_RESOURCE_LIST = 8,
   #/* Resource descriptor */
   hive_t_REG_FULL_RESOURCE_DESCRIPTOR = 9,
   #/* Resouce requirements list */
   hive_t_REG_RESOURCE_REQUIREMENTS_LIST = 10,
   #/* QWORD (64 bit integer), unspecified endianness but usually little endian */
   hive_t_REG_QWORD = 11


class GuestFS_Registry:
    def __init__(self, guestFS, rootLogger):
        self.guestFS = guestFS
        self.rootLogger = rootLogger
        self.regCache = dict()
        self.current_open_hive = None


    def clean_up(self):
        self.rootLogger.info('GuestFS_Registry::clean_up()')
        self.regCache.clear()
        self.close_hive()


    def open_hive(self, hiveName):
        try:
            regHivePath= self.guestFS.case_sensitive_path("/Windows/System32/config/"+hiveName)
            if len(regHivePath) == 0:
                return False;
            (out, err) = self.guestFS.callGF('Opening registry hive [' + regHivePath + ']', ['--', '-hivex-open', regHivePath], True)
            self.current_open_hive = hiveName
            if err:
                return False
        except subprocess.CalledProcessError:
            return False
        return True
        
    def close_hive(self):
        try:
            if self.current_open_hive != None:
                (out, err) = self.guestFS.callGF('Closing registry hive', ['--', '-hivex-close'], True)
                self.current_open_hive = None
                if err:
                    return False
        except subprocess.CalledProcessError:
            return False
        return True
    
    # Designed to work like the simple VBScript function: https://msdn.microsoft.com/en-us/library/x05fawxd(v=vs.84).aspx
    # Function should determine type of the registry value at runtime
    # Example reg_read("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Setup\State\ImageState")
    def reg_read(self, regpath):
        reg_nodes=regpath.split("\\")
        #only allow HKLM
        if (reg_nodes[0]!="HKEY_LOCAL_MACHINE" and reg_nodes[0]!="HKLM"):
            self.rootLogger.warning('Unsupported hive: ' + reg_nodes[0])
            return None
       
        current_key_path="HKEY_LOCAL_MACHINE"  #prevents cache misses with "HKLM" vs HKEY_LOCAL_MACHINE
        current_node_id = 0
        try:
            hiveName = reg_nodes[1]
            # Opening and closing hives is expensive, cache the info, keep them open after query and try to avoid if possible
            if self.current_open_hive == None or (hiveName.casefold() != self.current_open_hive.casefold()):  #case insensitive compare
                # if we have a different one open, close it
                if (self.current_open_hive != None):
                    self.rootLogger.info('Closing open hive: ' + self.current_open_hive)
                    self.close_hive()
                # open the specified hive
                if not self.open_hive(hiveName):  # e.g. SOFTWARE or SYSTEM
                    return None

            # walk to all but the end node
            for index in range(1, len(reg_nodes)-1):  
                current_key_path=str.format("{0}\\{1}",current_key_path,reg_nodes[index]).lower() #avoid case-sensitive cache misses
                if (not current_key_path in self.regCache):
                    if (index == 1):
                        # Hive root
                        (nodeid, err) = self.guestFS.callGF('Get registry root', ['--', '-hivex-root'], True)
                    else:                        
                        if ( current_key_path.casefold() == "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet".casefold() ):
                            #special case HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet
                            nodeid= self.determine_currentcontrolset(current_node_id)
                        else:
                            # standard key / node
                            node_name= reg_nodes[index]
                            # use the current nodeId and the name to get the child node id
                            (nodeid, err) = self.guestFS.callGF('Get registry child: [' + reg_nodes[index] + ']', ['--', '-hivex_node_get_child', current_node_id, reg_nodes[index]], True)
                    
                    # we have a nodeid: validate it and update cache
                    if err or (nodeid is None) or len(nodeid)== 0 or (nodeid[0] == 0):
                        self.rootLogger.error('Invalid registry path: ' + current_key_path)
                        return None
                    else:
                        current_node_id = nodeid[0]
                        # add it to the cache
                        self.regCache[current_key_path]= current_node_id
                else:
                    # node is already in the cache
                    current_node_id = self.regCache[current_key_path]

            # the final node is the registry value
            index=index+1
            outValue = self.get_string_value_by_name(current_node_id, reg_nodes[index])
                        
        except subprocess.CalledProcessError:
            outValue = None
        return outValue

    
    def get_string_value_by_name(self, node_id, value_name):
        # get the valueId for the value name 
        (valueid, err) = self.guestFS.callGF('Get registry value-id: [' + value_name + ']', ['--', '-hivex-node-get-value', node_id, value_name], True)
        if err or not valueid or valueid[0] == 0:
            return None
        # get the type for the value
        (valueType, err) = self.guestFS.callGF('Get registry value-type: [' + value_name + ']', ['--', '-hivex-value-type', valueid[0]], True)
        if err or not valueType or valueType[0]== 0:
            return None
        # get the value, as a string, by its type
        return self.get_string_value_by_type(valueid,valueType)


    # Retrieve the registry value and convert it from its native datatype into a string representation that is
    # both human and code readable
    def get_string_value_by_type(self, valueid, valueType):
        self.rootLogger.info('Registry type [get_value_by_type]: ' + hive_type( int(valueType[0]) ).name + ' = ' + str(valueType[0]))

        (out, err) = self.guestFS.callGF('Get registry value-value: ', ['--', '-hivex-value-value', valueid[0]] , False, True)  #raw results
        
        # try to convert based on type
        if (int(valueType[0]) == hive_type.hive_t_REG_SZ.value ) or (int(valueType[0]) == hive_type.hive_t_REG_EXPAND_SZ.value ):
            retVal = self.convert_to_ascii( out.decode("UTF-16LE")).replace('\0','') # remove trailing null termination
        elif (int(valueType[0]) == hive_type.hive_t_REG_MULTI_SZ.value ):
            retVal = self.convert_to_ascii(out.decode("UTF-16LE")).replace('\0',';') # make a semi-colon the delimeter between values
        elif (int(valueType[0]) == hive_type.hive_t_REG_DWORD.value ):
            intValue = int.from_bytes(bytes(out), byteorder='little' )
            #retVal = "%s (%d)" % ( hex(intValue),intValue ) 
            retVal = hex(intValue)  #easier to parse programatically, if needed
        elif (int(valueType[0]) == hive_type.hive_t_REG_QWORD.value ):
            retVal = "0x" + "".join("%02x" % out[b] for b in range(len(out)-1,-1,-1 ) )   #reverse the byte order
        elif (int(valueType[0]) == hive_type.hive_t_REG_BINARY.value ):
            retVal = "".join("%02x " % b for b in out)
        else:
            # No current use cases for REG_NONE or REG_RESOURCE_*
            retVal = "".join("%02x " % b for b in out)
        
        self.rootLogger.info('get_value_by_type returning:  ' + retVal )
        if err:
            return None 
        else:
            return retVal

    def determine_currentcontrolset(self, system_node_id):        
        # HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet is not an actual node hence the hive_xxx API does not work.  
        # The control set that appears in CurrentControlSet is selected by the system at startup and identified by the value of the Current entry in the Select subkey.
        # For more info see: https://technet.microsoft.com/en-us/library/cc976041.aspx 
        #  system_node_id parameter is for HKEY_LOCAL_MACHINE\SYSTEM        

        # Read:  \SYSTEM\Select\Current(DWORD)
        (nodeid, err) = self.guestFS.callGF('Get registry child: [determine_currentcontrolset()]: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Select', ['--', '-hivex_node_get_child', system_node_id, "Select"], True)
        if err or (nodeid is None) or len(nodeid)== 0 or (nodeid[0] == 0):
            self.rootLogger.error('Invalid registry path [determine_currentcontrolset()]: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Select')
            return None
        currentcontrol_value =  self.get_string_value_by_name(nodeid[0],"Current")
        if (currentcontrol_value is None):
            self.rootLogger.error('Invalid registry value [determine_currentcontrolset()]: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Select\Current')
            return None

        # Format like ControlSet001
        actual_controlset= "ControlSet00%d" % int(currentcontrol_value,16)

        # Return the nodeid for that node, eg. HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001; this will cause current and future requests
        # to redirect to the numeric controlset node, rather than CurrentControlSet
        (nodeid, err) = self.guestFS.callGF('Get registry child: [' + actual_controlset + ']', ['--', '-hivex_node_get_child', system_node_id, actual_controlset], True) 
        return nodeid

    # round trip through ascii decoding to strip anything unicode 
    def convert_to_ascii(self, string_to_convert):
        encoded = string_to_convert.encode('ascii',errors='replace')
        return encoded.decode('ascii')