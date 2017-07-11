## Automated testing
For check-ins and pull requests this project will perform the following automated testing through [travis-ci](https://travis-ci.org)

### Inspection Tests 
*[[inspection_tests.py](../tests/inspection_tests.py)]*
The inspection test script will run after building and running the container. It reads a series of tests from [test_config.json](../test_config.json) which invokes the service to interrogate predefined test VHDs representing core Azure scenarios and manifests across Windows, Linux, and BSD operating systems.  The json configuration describes the location of the VHD and the expected headers and file payload in the resulting response. 

The inspection test script will return the number of failing tests as a return code.  A non-zero value will cause the travis-ci build to fail.  Reviewing the travis-ci raw log will yield insight into the cause of the failures.

### Manifest documentation test
*[[requires_doc_change.sh](../tests/requires_doc_change.sh)]*
It is a goal that the repo documentation of the manifests accurately reflect their current content. This simple script, triggered by travis-ci, will run the [parse manifest](../tools/parse_manifest.py) script to an alternate location and compare the content of the current manifests with the content in the /docs folder.  If the content differs (except for the ending line with the date/time) then the script returns a non-zero value and the build will fail.

***If travis-ci reports the build is broken checking the manifest documentation*** <br>
This failure is easily correctable by:
1. running the [parse manifest](../tools/parse_manifest.py)  script manually
2. adding the revised doc files to your check-in
3. updating the pull request.  

Additional information on the parse manifest script [here](tools.md)


