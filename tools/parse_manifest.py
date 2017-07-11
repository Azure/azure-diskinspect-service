#!/usr/bin/env python3

import sys
import os
import inspect
import datetime


def hyperlink_to_this_file():
    filename= os.path.basename( inspect.getfile(inspect.currentframe() ) ) 
    return "[{0}](../tools/{0})".format(filename)

# The markdown increases the width of the table with each entry and it is difficult to find the scrollbars.  
# This is hack to make it fit
def return_line_with_breaks(text_line):   
    col_width = 85
    insertion=col_width
    while insertion < len(text_line):  
        text_line = "{0}<br>{1}".format(text_line[0:insertion],text_line[insertion:])
        if not use_verbosity is None:
            print(text_line)
        insertion+=col_width
    
    return text_line

"""
This scripts creates two doc files by different pivots
"""

manifest_folder = "../pyServer/manifests"
documentation_folder = "../docs"
if len(sys.argv) > 1:
    documentation_folder = sys.argv[1]
    
use_verbosity = os.environ.get('PARSE_SCRIPT_VERBOSITY')

print("Output folder: {0}".format(documentation_folder) )
manifest_doc_file = "manifest_content.md"
manifest_doc_file_path = os.path.join(documentation_folder,manifest_doc_file)
by_content_doc_file = "manifest_by_file.md"
by_content_doc_file_path = os.path.join(documentation_folder,by_content_doc_file)

with open( file=manifest_doc_file_path, mode="w", newline="\r\n") as manifestDocFile:
    with open( file=by_content_doc_file_path, mode="w", newline="\r\n") as contentDocFile:
        template = "This file documents {0} disk inspection manifests used by Microsoft Azure support.  Any data collected by Microsoft using this tooling is done according to the policy outlined in the [Azure Trust Center](https://azure.microsoft.com/en-us/support/trust-center/).\n\n"
        manifestDocFile.write(template.format("the various files collected, or directory listed or registry key queried by") )
        contentDocFile.write(template.format("files collected in"))
        for root, dirs, files in os.walk(manifest_folder):
            dirs.sort()
            if root is manifest_folder:
                # create an initial list    
                for dirname in dirs:
                    manifestDocFile.write("* [{0}](#{0})\n".format(dirname) )
                    contentDocFile.write("* [{0}](#{0})\n".format(dirname) )
            else:
                listing={}
                current_os = os.path.basename(root)
                manifestDocFile.write("## {0} \n".format(current_os) )     
                manifestDocFile.write(" Manifest | Operation | File Path \n")     
                manifestDocFile.write(" ------------- | ------------- | ------------- \n")
                contentDocFile.write("## {0} \n".format(current_os) ) 
                contentDocFile.write("File Path | Manifest \n")     
                contentDocFile.write("------------- | ------------- \n")
                files.sort()
                for filename in files:
                    filepath = os.path.join(root, filename)
                    current_manifest = filename
                    if not use_verbosity is None: 
                        print(filepath)
                    with open(file=filepath, mode="r") as manifestFile:
                        for line in manifestFile:
                            line = line.strip()
                            if ( len(line)>0 and line != "\n" and not line.lower().startswith("echo") ):
                                splitline = line.split(',')
                                if (splitline[0].strip() == "ll"):
                                    splitline[0] = "list"
                                elif (splitline[0].strip() == "reg"):
                                    splitline[0] = "registry query"
                                manifestDocFile.write("{0} | {1} | {2}\n".format(current_manifest, splitline[0], return_line_with_breaks(splitline[1].replace("*","\*")) ) )

                                if (splitline[0].strip() == "copy"):
                                    filename = splitline[1].replace("*","\*")
                                    if not use_verbosity is None:
                                        print("{0} - {1}".format(filename,current_manifest) )
                                    if ( filename in listing ):
                                        # Add to existing
                                         listing[filename].append(current_manifest)
                                    else:
                                        # create a new item
                                        listing[filename]=[current_manifest]

                for copiedFile in sorted(listing):
                    contentDocFile.write("{0} | {1} \n".format(return_line_with_breaks(copiedFile), ', '.join(listing[copiedFile]) ) ) 
        
        footer = "\n*File was created by running " + hyperlink_to_this_file()  + " on `" + str(datetime.datetime.now())+ "`*" 
        manifestDocFile.write( footer )
        manifestDocFile.flush()
        contentDocFile.write( footer )
        contentDocFile.flush()
        for f in [manifest_doc_file_path,by_content_doc_file_path]:
            print("'{0}' was created, file size={1}".format(f, os.path.getsize(f)) )