## Automated testing
For check-ins and pull requests this project will perform the following automated testing through github actions.

### Manifest documentation test
*[[requires_doc_change.sh](../tests/requires_doc_change.sh)]*
It is a goal that the repo documentation of the manifests accurately reflect their current content. This simple script, triggered by travis-ci, will run the [parse manifest](../tools/parse_manifest.py) script to an alternate location and compare the content of the current manifests with the content in the /docs folder.  If the content differs (except for the ending line with the date/time) then the script returns a non-zero value and the build will fail.

***If travis-ci reports the build is broken checking the manifest documentation*** <br>
This failure is easily correctable by:
1. running the [parse manifest](../tools/parse_manifest.py)  script manually
2. adding the revised doc files to your check-in
3. updating the pull request.  

Additional information on the parse manifest script [here](tools.md)


