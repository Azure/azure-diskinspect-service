## Windows registry queries ##

The disk inspection capability now includes basic queries for Windows registry content.  To use the functionality add a "reg" moniker to the manifest with a full registry path, including value, as a second parameter.  For example:

`reg, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ProgramFilesDir` 

The output of the registry query will be added to a registry.json file as simple JSON.  The intent is to enable straightforward consumption by both automation code and humans.

__Additional info__

The registry functionality was tested with the following data types:
> - REG_SZ
> - REG_DWORD
> - REG\_MULTI\_SZ
> - REG\_EXPAND\_SZ
> - REG_QWORD
> - REG_BINARY


- No support writing to keys/values, only reading them
- Manifests are forgiving with case insensitive registry path and values
- A simple cache mechanism is used on a VM partition basis to try to avoid unnecessary round trips for common registry nodes
 - The simple caching mechanism tries to be forgiving of case sensitive variance in paths across keys in the same manifest
- If the registry key or value is not present, logging to this effect will be added to operational log
- The registry functionality supports SkipToStep.  There are no minor operational steps.
- HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet is not an actual node, however there is code to determine what the “current” controlset is and redirect the query to that location
- Registry permissions: there is no capability to read and unpack a security descriptor, ACLs, and access control entries.  Adding this would be a significant amount of work.  
 - Please use the workaround of collecting the hive containing the key in question, then mounting and interrogating on a Windows computer locally to determine permissions.
- Currently there is no support for a registry query to dump all values of a key or a wildcard in the path to return multiple subordinate keys.  We can evaluate those for future additions based on need and priority.
- There is no support for returning Unicode registry values at this time.  Unicode characters in registry values will be converted to the default ascii replacment character '?'



__Best Practices__

- Opening and closing hives is expensive: Group queries to the same hive file together in manifest to avoid unnecessary transitions. (e.g. HKEY\_LOCAL\_MACHINE\SOFTWARE == /Windows/System32/config/SOFTWARE file) 
