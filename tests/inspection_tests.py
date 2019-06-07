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
import subprocess

from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions,
    BlobPermissions,
    PublicAccess,
)

class InvalidBlobSasUrlException(Exception):
   """Raised when an invalid Blob Sas Url is received as parameter input"""
   pass

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
                        print("ERROR: Comparison failed: test_value:[{0}] vs header_value:[{1}]".format( test_value.lower().strip(), header_value.lower().strip()) )
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
    if os.path.exists(basename):
        shutil.rmtree(basename)

    os.makedirs(basename)
    zf = zipfile.ZipFile(zipFilename) 
    zf.extractall(basename)

def parseHealthResponse(healthHTML):
    regex = '<<STATS>>Total Requests: (?P<total>\d+), Success Requests: (?P<success>\d+), Avg Success Service Time: (?P<avg_time>\S+)s, Active Requests: (?P<active>\d+), Consecutive Errors: (?P<consecutive_error>\d+)'
    m = re.search(regex, healthHTML)
    return m.groupdict()

def get_service_health(service_host):
    uri = "{0}/{1}/".format(service_host,"health")
    req = urllib.request.Request(url=uri,method='GET')
    try:
        res = urllib.request.urlopen(req, cafile=cafile)
        return parseHealthResponse(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return {}

def download_result_blob(blobSasUrl, local_file_path):
    urlParts = urllib.parse.urlparse(blobSasUrl)

    if not urlParts.path or len(urlParts.path) == 0:
        raise InvalidBlobSasUrlException('Input Blob SAS Url for upload is missing Container and Blob info.')
    if not urlParts.query or len(urlParts.query) == 0:
        raise InvalidBlobSasUrlException('Input Blob SAS url for upload is missing SAS token.')

    if urlParts.path[0] == '/':
        blob_storage_path = urlParts.path[1:]
    else:
        blob_storage_path = urlParts.path

    if 'blob' not in urlParts.netloc:
        raise InvalidBlobSasUrlException('Input Blob SAS url for upload is not pointing to a valid Azure Blob endpoint.')

    destination_storage_account = urlParts.netloc.split('.')[0]

    if not destination_storage_account:
        raise InvalidBlobSasUrlException('Input Blob SAS url for upload does not contain storage account.')

    urlSplit = blob_storage_path.split('/')

    if not len(urlSplit) == 2 or not urlSplit[0] or not urlSplit[1]:
        raise InvalidBlobSasUrlException('Input Blob SAS Url is not in the right format.')
    
    destination_container_name = urlSplit[0]
    destination_blob_name = urlSplit[1]
    destination_sas_token = urlParts.query

    blob_service = BlockBlobService(
        account_name = destination_storage_account,
        sas_token = destination_sas_token,
    )

    print("\nDownloading blob to " + local_file_path)
    blob_service.get_blob_to_path(destination_container_name, destination_blob_name, local_file_path)

        
header_to_json_mappings = {"os":"InspectionMetadata-Operating-System",
                "os_distribution":"InspectionMetadata-OS-Distribution", 
                "os_product_name":"InspectionMetadata-Product-Name",
                "os_disk_configuration":"InspectionMetadata-Disk-Configuration",
                "partial_result":"InspectionMetadata-Partial-Result",
                "expected_timeout":"KeepAliveThread-Timeout-In-Mins",
                "content_type":"Content-Type",
                "content_length":"Content-Length"}
                        

relative_subdirectory = "TestDownloads"
download_directory = current_directory = os.path.split( inspect.getfile(inspect.currentframe() ) )[0]
service_host = "https://localhost:8080"
storage_sas = os.environ.get('LIBGUESTFS_SAS_KEY')
blob_upload_sas_url = os.environ.get('BLOB_UPLOAD_SAS_URL')

if len(sys.argv) > 1:
    download_directory  = sys.argv[1]
if len(sys.argv) > 2:
    service_host = sys.argv[2]
if len(sys.argv) > 3:
    storage_sas = sys.argv[3]
if len(sys.argv) > 4:
    blob_upload_sas_url = sys.argv[4]

if storage_sas is None:
    print("ERROR: Unable to get SAS key from environment variable! Exiting...")
    sys.exit(1)
if blob_upload_sas_url is None:
    print("ERROR: Unable to get Blob upload SAS Url from environment variable! Exiting...")
    sys.exit(1)

script_start_time = datetime.datetime.now()

subdirectory=os.path.join(download_directory, relative_subdirectory)
shutil.rmtree(subdirectory, True)  #wipe any prior data
time.sleep(1) # some kind of async issue with the rmtree causes the mkdir below to fail...

os.mkdir(subdirectory)
print("Downloading zip files to '{0}'".format(subdirectory) )
passed_tests = []
failed_tests = []
should_fail_tests = []

user_home = os.environ.get('HOME')
if os.path.exists(user_home+'/azdis_ssl/azdis_public.crt'):
    cafile= user_home+'/azdis_ssl/azdis_public.crt'
else:
    print("ERROR: No certificate found!")
    cafile=None

initialServiceHealth = get_service_health(service_host)
print("Initial service health")
print(initialServiceHealth)

# get json configuration
with open(os.path.join(current_directory,'test_config.json'), "r") as json_config_file:

    json_root = json.load(json_config_file)
    storage_acct = json_root["storage_account_name"]
    storage_sas = storage_sas.strip('?')  #remove any initial '?' since the urlencoding will add it
    max_duration = json_root["max_duration_seconds"]  
    
    for inspection_test in json_root["tests"]:
        test_start_time = datetime.datetime.now()
        test_passed = True
        operation_id = str(uuid.uuid4())  #generate a unique id
        print("==============================================")
        print(inspection_test["title"] + " : " + inspection_test["description"])
        if inspection_test["title"] == "Invalid storage account":
            uri = "{0}/{1}/{2}/{3}{4}".format(service_host, operation_id, inspection_test["manifest"], "nosuchAccount",inspection_test["vhd_relative_path"]) 
        else:
            uri = "{0}/{1}/{2}/{3}{4}".format(service_host, operation_id, inspection_test["manifest"], storage_acct,inspection_test["vhd_relative_path"]) 

        print(uri)

        blob_sas_to_use = blob_upload_sas_url
        if "invalid_blob_token" in inspection_test:
            blob_sas_to_use  = blob_upload_sas_url.replace(urllib.parse.urlparse(blob_upload_sas_url).query, "")
            blob_sas_to_use  = blob_sas_to_use.replace("?", "")
        elif "no_container_blob" in inspection_test:
            blob_sas_to_use  = blob_upload_sas_url.replace(urllib.parse.urlparse(blob_upload_sas_url).path, "")
        elif "bad_blob_endpoint" in inspection_test:
            blob_sas_to_use  = blob_upload_sas_url.replace("blob", "foo")

        input_params = {"saskey":storage_sas}

        if inspection_test["title"] == "Invalid SAS":
            input_params.update({"saskey": "sv=2017-04-17&sr=c&sig=INVALIDSAS"})

        if "timeout_override" in inspection_test:
            input_params.update({"timeout":inspection_test["timeout_override"]})

        if "blob_upload" in inspection_test and inspection_test["blob_upload"] == True:
            input_params.update({"blobsasurl":blob_sas_to_use })

        DATA = urllib.parse.urlencode(input_params)
        DATA = DATA.encode('ascii')
        req = urllib.request.Request(url=uri,data=DATA,method='POST')
        try:
            res = urllib.request.urlopen(req, timeout=max_duration,cafile=cafile)
        except urllib.error.HTTPError as e:
            print("Error requesting service: " + str(e))    #not catch
            if not "shouldFail" in inspection_test:
                test_passed = False 
            else:
                should_fail_tests.append(inspection_test["title"])
        except socket.timeout as e:
            print("Test exceeded time duration.. failing..")
            test_passed = False

        if not "shouldFail" in inspection_test:
            if test_passed: 
                folder_name = "{0}_{1}".format( uri.split('/')[-1].split('.')[0],  inspection_test["manifest"])  # e.g. Centos7_normal  
                folder_path = os.path.join(subdirectory, folder_name)
                file_path = folder_path+".zip"

                print('INFO: Saving file to: ' + file_path )
                if "blob_upload" not in inspection_test or inspection_test["blob_upload"] == False:
                    # extract result from response
                    with open(file_path, "wb") as f:
                        f.write(res.read())
                else:
                    # download result from blob
                    download_result_blob(blob_sas_to_use, file_path)

                response_headers = res.getheaders()
                print("RESPONSE HEADERS:")
                print(response_headers)
                extract_zip(file_path, folder_path)
                mappings = header_to_json_mappings
        else:
            mappings = {} # skip this for "shouldFail" expected failure cases
            folder_path = ""

        test_end_time = datetime.datetime.now()
        test_duration = ((test_end_time - test_start_time).total_seconds()/60)

        if inspection_test["title"] == "KeepAliveThread timeout" and test_passed:
            if test_duration > 1.1 and test_files(inspection_test, folder_path ):
                failed_tests.append(inspection_test["title"])
                test_result = "FAILED"
                print("ERROR: Test did not timeout after 1 minutes" )
            elif test_headers(mappings, inspection_test) and not test_files(inspection_test, folder_path ):
                test_passed = True
                passed_tests.append(inspection_test["title"])
                test_result = "PASSED"
        else:
            if test_passed and test_headers(mappings, inspection_test) and test_files(inspection_test, folder_path ) and test_content(inspection_test, folder_path ):
                passed_tests.append(inspection_test["title"])
                test_result = "PASSED"
            else:
                failed_tests.append(inspection_test["title"])
                test_result = "FAILED"

        print("Test '{1}' {2}. Test duration {0} minutes".format( str( test_duration ), inspection_test["title"],test_result  ) )

    print("==============================================")
    # Query health test: This ensures that we encountered only "expected" errors
    # Sleep for 2 seconds first and let cleanup and service status update complete
    time.sleep(2)
    test_name = 'Health result validation test'
    currentServiceHealth = get_service_health(service_host)
    print(currentServiceHealth)
    if ("success" in currentServiceHealth and "success" in initialServiceHealth 
        and int(currentServiceHealth["success"]) == len(passed_tests) - len(should_fail_tests) + int(initialServiceHealth["success"])
        and "total" in currentServiceHealth and "total" in initialServiceHealth
        and int(currentServiceHealth["total"]) == len(passed_tests) + int(initialServiceHealth["total"])
        and "active" in currentServiceHealth and int(currentServiceHealth["active"]) == 0
        and "consecutive_error" in currentServiceHealth and int(currentServiceHealth["consecutive_error"]) == 0 
    ):
        passed_tests.append(test_name)
        test_result = "PASSED"
    else:
        failed_tests.append(test_name)
        test_result = "FAILED"  

    print( "{0}: {1}".format(test_name, test_result))
    print("==============================================")

    # Ensure we don't have any leftover items under /output
    test_name = 'Remaining output content test'
    container_name = "AzureDiskInspectSvc_US" 
    output = subprocess.run(['docker','diff', container_name], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if output.find("/output/") == -1:  #/output will be present but there should not be anything within in
        passed_tests.append(test_name)
        test_result = "PASSED"
    else:
        failed_tests.append(test_name)
        test_result = "FAILED" 
        print("Remaining content found in /output!")
        print(output)
    print( "{0}: {1}".format(test_name, test_result))

    print("***************************************************")
    print("Passing tests")
    print("=============")
    print(passed_tests)
    print("***************************************************")
    print("Should fail tests")
    print("=============")
    print(should_fail_tests)
    print("***************************************************")    
    print("Failing tests")
    print("=============")
    print(failed_tests)
    print("***************************************************")    
    script_end_time = datetime.datetime.now()
    test_count = len(json_root["tests"]) + 2    # include 'Health result validation test' and 'Remaining output content test'
    print("Ran {1} tests. Script duration {0} minutes".format( str( (script_end_time - script_start_time).total_seconds()/60 ), test_count) )
    
sys.exit( len(failed_tests) ) #zero indicates success 
            
        
