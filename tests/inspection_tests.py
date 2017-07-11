#!/usr/bin/python3

import shutil
import os
import sys
import datetime
import time
import json
import urllib.request 
import urllib.parse 
import uuid
import zipfile
import socket
import inspect
import re

def test_headers(header_to_json_mappings, inspection_test):
	#validate headers with test values
	for test_setting in header_to_json_mappings:
		print(" == test setting: '{0}'".format(test_setting) )
		if test_setting in inspection_test and len(inspection_test[test_setting]) >0:  #if there is a value in the json 
			test_value = inspection_test[test_setting]  
			mapped_value = header_to_json_mappings[test_setting] #get the mapped value from the http reseponse header_to_json_mappings
			found_header = False
			for (header_name, header_value) in response_headers: 
				if mapped_value == header_name:
					found_header = True
					print("INFO: json config setting[{0}]: '{1}' => response header[{2}]:'{3}'".format( test_setting, test_value, mapped_value, header_value) )
					if test_value.lower().strip() != header_value.lower().strip():
						return False
			if not found_header: 
				print( "ERROR: Test failed... did not find header: {0} in http response.".format(mapped_value) )
				return False
					
	return True

summary_file = "results.txt"
def test_files(inspection_test, extracted_base):
	print("Extracted base directory for this test: " + extracted_base)
	if "files_present" in inspection_test:
		filelist = inspection_test["files_present"]
		# we should always have a summary file
		filelist.append(summary_file)
		# validate test file paths with extracted contents
		for test_filepath in filelist:
			test_filepath = test_filepath.strip('/')  # we will add the delimiter back in
			full_test_path = "{0}/{1}".format(extracted_base, test_filepath)  # can't use os.path.join() because it only works on leaf nodes
			if not os.path.exists(full_test_path) or not os.path.getsize(full_test_path) > 0:
				print("ERROR: Missing downloaded test file: "+ full_test_path)
				return False
			else:
				print("INFO: Found test file: "+ full_test_path)
			
	return True

def file_get_contents(filename):
	with open(filename) as f:
		return f.read()

def test_content(inspection_test, extracted_base):
	if "file_content" in inspection_test:
		filecontent = inspection_test["file_content"]
		# validate file content
		for test_filepath in filecontent:
			stripped_filepath = test_filepath.strip('/')  # we will add the delimiter back in
			full_test_path = "{0}/{1}".format(extracted_base, stripped_filepath)  # can't use os.path.join() because it only works on leaf nodes
			if not os.path.exists(full_test_path):
				print("ERROR: Missing downloaded test file: "+ full_test_path)
				return False
			else:
				# read the content and apply a regex
				content = file_get_contents(full_test_path)
				pattern = filecontent[test_filepath]
				searchObj= re.search( pattern, content, re.M|re.I)
				if not searchObj:
					print("ERROR: No match for regex '{0}' in file ".format( pattern, full_test_path) )
					return False
				else:
					print("INFO: Found regex pattern '{0}' in file ".format( pattern, full_test_path) )
	return True
			
			
def extract_zip(zipFilename, basename):
	os.makedirs(basename)
	zf = zipfile.ZipFile(zipFilename) 
	zf.extractall(basename)

		
header_to_json_mappings = {"os":"InspectionMetadata-Operating-System",
				"os_distribution":"InspectionMetadata-OS-Distribution", 
				"os_product_name":"InspectionMetadata-Product-Name",
				"os_disk_configuration":"InspectionMetadata-Disk-Configuration"}
						

relative_subdirectory = "TestDownloads"
download_directory = current_directory = os.path.split( inspect.getfile(inspect.currentframe() ) )[0]
service_host = "http://localhost:8080"
storage_sas = os.environ.get('LIBGUESTFS_SAS_KEY')
if len(sys.argv) > 1:
	download_directory  = sys.argv[1]
if len(sys.argv) > 2:
	service_host = sys.argv[2]
if len(sys.argv) > 3:
	storage_sas = sys.argv[3]


if storage_sas is None:
	print("ERROR: Unable to get SAS key from environment variable! Exiting...")
	sys.exit(1)

script_start_time = datetime.datetime.now()

subdirectory=os.path.join(download_directory, relative_subdirectory)
shutil.rmtree(subdirectory, True)  #wipe any prior data
time.sleep(1) # some kind of async issue with the rmtree causes the mkdir below to fail...

os.mkdir(subdirectory)
print("Downloading zip files to '{0}'".format(subdirectory) )
passed_tests = []
failed_tests = []


# get json configuration
with open(os.path.join(current_directory,'test_config.json'), "r") as json_config_file:

	json_root = json.load(json_config_file)
	storage_acct = json_root["storage_account_name"]
	storage_sas = storage_sas.strip('?')  #remove any initial '?' since the urlencoding will add it
	max_duration = json_root["max_duration_seconds"]  
	
	for inspection_test in json_root["tests"]:
		test_start_time = datetime.datetime.now()
		test_passed = True
		operation_id = uuid.uuid4().hex[0:12]  #generate a unique id
		print("==============================================")
		print(inspection_test["title"] + " : " + inspection_test["description"])
		uri = "{0}/{1}/{2}/{3}{4}".format(service_host, operation_id, inspection_test["manifest"], storage_acct,inspection_test["vhd_relative_path"]) 
		print(uri)
		DATA = urllib.parse.urlencode({"saskey":storage_sas})
		DATA = DATA.encode('ascii')
		req = urllib.request.Request(url=uri,data=DATA,method='POST')
		try:
			user_home = os.environ.get('HOME')
			if os.path.exists(user_home+'/azdis_ssl/azdis_public.crt'):					
				cafile= user_home+'/azdis_ssl/azdis_public.crt'
			else:
				cafile=None
			res = urllib.request.urlopen(req, timeout=max_duration,cafile=cafile)
		except urllib.error.HTTPError as e:
			print("Error requesting service: " + str(e))    #not catch
			test_passed = False
			
		except socket.timeout as e:
			print("Test exceeded time duration.. failing..")
			test_passed = False
		if test_passed: 
			folder_name = "{0}_{1}".format( uri.split('/')[-1].split('.')[0],  inspection_test["manifest"])  # e.g. Centos7_normal	
			folder_path = os.path.join( subdirectory, folder_name)
			file_path = folder_path+".zip"
			print('INFO: Saving file to: ' + file_path )
			with open(file_path, "wb") as f:
				f.write(res.read())
			
			response_headers = res.getheaders()
			print(response_headers)
			extract_zip(file_path, folder_path)

		if test_passed and test_headers(header_to_json_mappings, inspection_test) and test_files(inspection_test, folder_path ) and test_content(inspection_test, folder_path ):
			passed_tests.append(inspection_test["title"])
			test_result = "PASSED"
		else:
			failed_tests.append(inspection_test["title"])
			test_result = "FAILED"
		test_end_time = datetime.datetime.now()
		print("Test '{1}' {2}. Test duration {0} minutes".format( str( (test_end_time - test_start_time).total_seconds()/60 ), inspection_test["title"],test_result  ) )

	print("***************************************************")
	print("Passing tests")
	print("=============")
	print(passed_tests)
	print("***************************************************")
	print("Failing tests")
	print("=============")
	print(failed_tests)
	print("***************************************************")	
	script_end_time = datetime.datetime.now()
	print("Ran {1} tests. Script duration {0} minutes".format( str( (script_end_time - script_start_time).total_seconds()/60 ), len(json_root["tests"])  ) )
	
sys.exit( len(failed_tests) ) #zero indicates success 
			
		
