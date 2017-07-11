#!/bin/bash

cd ./tools
# generate current documentation to a temp folder
if [ ! -d ~/doc_temp ]; then
    mkdir ~/doc_temp
fi
python3 parse_manifest.py ~/doc_temp

# compare with the current check-in
if ! diff -w --ignore-matching-lines="File was created by running" ../docs/manifest_content.md ~/doc_temp/manifest_content.md; then
    echo "Failed validating manifest_content.md!  Check lines above for details and run parse_manifest.py prior to submitting the PR."
    exit 1
fi 
if ! diff -w --ignore-matching-lines="File was created by running" ../docs/manifest_by_file.md ~/doc_temp/manifest_by_file.md; then
    echo "Failed validating manifest_by_file.md!  Check lines above for details and run parse_manifest.py prior to submitting the PR."
    exit 1
fi 

cd ..
rm -rf ~/doc_temp