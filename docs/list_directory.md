## Directory or file listing ##

The disk inspection capability includes the ability to list the files in a particular directory without returning any files.  To use the functionality add a "ll" moniker to the manifest with a folder or file path as a second parameter.  For example:

`ll,/var/log` 

The output will be added to a results.txt file as text.  This can be useful in several scenarios, including:

- determining if a file or subdirectory is present without actually copying it
- getting a count of files in a directory
- capturing timestamps and permissions on the original disk
 
__Additional info__

- Wild cards in paths are supported


__Example output__

	15:52:59  Listing contents of /var/log:
	
	total 111784
	drwxrwxr-x 11   0 104     4096 Nov 21 15:53 .
	drwxr-xr-x 13   0   0     4096 Jun 13  2016 ..
	-rw-r--r--  1   0   0        0 Jul  1  2016 alternatives.log
	-rw-r--r--  1   0   0     3134 Jun 13  2016 alternatives.log.1
	-rw-r-----  1   0   4        0 Jun 30  2016 apport.log
	-rw-r-----  1   0   4     1411 Jun 29  2016 apport.log.1
	-rw-r-----  1   0   4      247 Jun 28  2016 apport.log.2.gz
	-rw-r-----  1   0   4      236 Jun 18  2016 apport.log.3.gz
	-rw-r-----  1   0   4      327 Jun 13  2016 apport.log.4.gz
	drwxr-xr-x  2   0   0     4096 Jul  1  2016 apt
	-rw-r-----  1 101   4    86059 Nov 21 16:17 auth.log
	-rw-r-----  1 101   4  2039263 Jul 17  2016 auth.log.1
	-rw-r-----  1 101   4   149759 Jul 10  2016 auth.log.2.gz
	-rw-r-----  1 101   4   176408 Jul  4  2016 auth.log.3.gz
	-rw-r-----  1 101   4   991415 Jun 26  2016 auth.log.4.gz
	drwxr-xr-x  3   0   0     4096 Jun 13  2016 azure
...