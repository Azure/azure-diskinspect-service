## Disk Inspection ##

The disk inspection capability now includes basic information about the partitions on the targeted VHD.  To use the functionality add a "diskinfo" moniker to the manifest, the second parameter is not necessary and will be ignored.  For example:

`diskinfo,` 

The output will be added to a diskinfo.txt file as text.

If the OS type of disk is determined to be Windows, the partition to Windows drive letter mappings will be added.  Next, the `df` command is run to provide human readable disk size and use information. Lastly, it will loop through each mounted partition and provide [statvfs](http://man.he.net/man2/statvfs) for each.  This is useful for several troubleshooting scenarios including determining if inodes have been exhausted. 


__Example output__

	Windows drive letter mappings [Inspect skipped]:
	C: /dev/sda1

	Filesystem      Size  Used Avail Use% Mounted on
	/dev/root       4.0G  423M  3.4G  12% /
	tmpfs            96M  172K   96M   1% /run
	/dev            236M     0  236M   0% /dev
 	/dev/sda1       127G   15G  113G  12% /sysroot


	[Device: /dev/sda1, mountpoint: / ]
	bsize: 4096
	frsize: 4096
	blocks: 33291775
	bfree: 29462997
	bavail: 29462997
	files: 118048596
	ffree: 117915009
	favail: 117915009
	fsid: 0
	flag: 4097
	namemax: 255 