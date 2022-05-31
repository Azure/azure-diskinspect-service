# Azure Disk Inspect Service

The Azure Disk Inspect Service is intended to be a service that allows customers, support or third party personnel with privileged access to access an Azure OS Disk for log and configuration files without provisioning a VM and attaching a copy of the disk in order to probe the contents. It is a fast and secure way to retrieve well known contents of an OS disk by the user to aid in system failure diagnosis.


## How To Contribute

**Make sure you are a member of this permission group: https://repos.opensource.microsoft.com/Azure/teams/diskinspection-extended

	1.	Clone github repo locally
		 $ git clone https://github.com/Azure/azure-diskinspect-service <local_path>
	
	2.	Create a new branch from master
		 $ cd <local_path>
		 $ git checkout -b <new_branch>

	4.	Apply your changes in the branch

		-If you are updating/creating new manifest then: Make sure to run "parse_manifest.py"
		 $ cd ./tools/
		 $ python ./parse_manifest.py
		 $ cd -

	5.	Push changes to your remote branch by following below sequesnce of commands
		$ git add <file_changed>
		$ git commit -m "<Commit_message>"
		$ git push --set-upstream origin <new_branch> 

	6.	Raise PR to merge into master for review
-----

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) or Azure experts at vminspector@microsoft.com with any additional questions or comments.
