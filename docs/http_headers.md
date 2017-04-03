## Service HTTP headers ##

The disk inspection service will return extended information in defined HTTP headers to the caller as described below

<dl>
<dt>InspectionMetadata-Operating-System</dt>
<dd>
The service will return the string value it believes is the operating system of the target VHD. Typically, this is the value returned from <a href:"http://libguestfs.org/guestfish.1.html#inspect-get-type">inspect-get-type</a>. 
</dd>
<dt>InspectionMetadata-Configuration</dt>
<dd>
This header is used to identify non-standard disk configurations.  Currently this only includes the strings below:
<li>Standard</li>
<li>Encrypted</li>
</dd>
<dt>InspectionMetadata-OS-Distribution</dt>
<dd>
The service will return the string value it believes is the distribution operating system of the target VHD. Typically, this is the value returned from <a href:"http://libguestfs.org/guestfish.1.html#inspect-get-distro">inspect-get-distro</a>. 
</dd>
<dt>InspectionMetadata-Product-Name</dt>
<dd>
The service will return the string value it believes is the product name of the target VHD. Typically, this is the value returned from <a href:"http://libguestfs.org/guestfish.1.html#inspect-get-product-name">inspect-get-product-name</a>. 
</dd>
</dl>