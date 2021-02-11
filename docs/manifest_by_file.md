This file documents files collected in disk inspection manifests used by Microsoft Azure support.  Any data collected by Microsoft using this tooling is done according to the policy outlined in the [Azure Trust Center](https://azure.microsoft.com/en-us/support/trust-center/).

* [freebsd](#freebsd)
* [linux](#linux)
* [windows](#windows)
## freebsd 
File Path | Manifest 
------------- | ------------- 
/boot/loader.conf | diagnostic, normal 
/etc/\*-release | agents 
/etc/dhclient.conf | agents, diagnostic 
/etc/fstab | diagnostic, normal 
/etc/networks | diagnostic 
/etc/nsswitch.conf | diagnostic 
/etc/rc.conf | agents, diagnostic, genspec, normal 
/etc/resolv.conf | diagnostic 
/etc/ssh/sshd_config | diagnostic, normal 
/etc/syslog.conf | diagnostic 
/etc/waagent.conf | agents, diagnostic 
/run/systemd/resolve/stub-resolv.conf | diagnostic 
/var/lib/waagent/ExtensionsConfig.\*.xml | agents, diagnostic 
/var/lib/waagent/GoalState.\*.xml | agents, diagnostic 
/var/lib/waagent/HostingEnvironmentConfig.xml | agents, diagnostic 
/var/lib/waagent/Microsoft.OSTCExtensions.CustomScriptForLinux.\*.manifest.xml | agents, diagnostic 
/var/lib/waagent/Prod.\*.manifest.xml | agents, diagnostic 
/var/lib/waagent/SharedConfig.xml | agents, diagnostic 
/var/lib/waagent/\*.xml | agents 
/var/lib/waagent/\*/config/HandlerState | agents, diagnostic 
/var/lib/waagent/\*/config/HandlerStatus | agents, diagnostic 
/var/lib/waagent/\*/config/\*.settings | agents, diagnostic 
/var/lib/waagent/\*/status/\*.status | agents, diagnostic 
/var/lib/waagent/provisioned | diagnostic, genspec 
/var/log/auth\* | agents, diagnostic, normal 
/var/log/azure/\*/\*/\* | agents, diagnostic 
/var/log/boot\* | normal 
/var/log/dmesg\* | agents, diagnostic, normal 
/var/log/messages\* | diagnostic, normal 
/var/log/secure\* | diagnostic 
/var/log/waagent\* | agents, diagnostic, normal 
## linux 
File Path | Manifest 
------------- | ------------- 
