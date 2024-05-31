This file documents files collected in disk inspection manifests used by Microsoft Azure support.  Any data collected by Microsoft using this tooling is done according to the policy outlined in the [Azure Trust Center](https://azure.microsoft.com/en-us/support/trust-center/).

* [freebsd](#freebsd)
* [linux](#linux)
* [windows](#windows)
## freebsd 
File Path | Manifest 
------------- | ------------- 
/boot/loader.conf | diagnostic, normal, vmdiagnostic 
/etc/\*-release | agents 
/etc/dhclient.conf | agents, diagnostic, vmdiagnostic 
/etc/fstab | diagnostic, normal, vmdiagnostic 
/etc/networks | diagnostic, vmdiagnostic 
/etc/nsswitch.conf | diagnostic, vmdiagnostic 
/etc/rc.conf | agents, diagnostic, genspec, normal, vmdiagnostic 
/etc/resolv.conf | diagnostic, vmdiagnostic 
/etc/ssh/sshd_config | diagnostic, normal, vmdiagnostic 
/etc/syslog.conf | diagnostic, vmdiagnostic 
/etc/waagent.conf | agents, diagnostic, vmdiagnostic 
/run/systemd/resolve/stub-resolv.conf | diagnostic, vmdiagnostic 
/var/lib/waagent/ExtensionsConfig.\*.xml | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/GoalState.\*.xml | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/HostingEnvironmentConfig.xml | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/Microsoft.OSTCExtensions.CustomScriptForLinux.\*.manifest.xml | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/Prod.\*.manifest.xml | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/SharedConfig.xml | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*.xml | agents 
/var/lib/waagent/\*/config/HandlerState | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*/config/HandlerStatus | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*/config/\*.settings | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*/status/\*.status | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/provisioned | diagnostic, genspec, vmdiagnostic 
/var/log/auth\* | agents, diagnostic, normal, vmdiagnostic 
/var/log/azure/\*/\*/\* | agents, diagnostic, vmdiagnostic 
/var/log/boot\* | normal 
/var/log/dmesg\* | agents, diagnostic, normal, vmdiagnostic 
/var/log/messages\* | diagnostic, normal, vmdiagnostic 
/var/log/secure\* | diagnostic, vmdiagnostic 
/var/log/waagent\* | agents, diagnostic, normal, vmdiagnostic 
## linux 
File Path | Manifest 
------------- | ------------- 
/boot/grub\*/grub.c\* | eg, linux-bootconfig, vmdiagnostic 
/boot/grub\*/grubenv | linux-bootconfig 
/boot/grub\*/menu.lst | eg, linux-bootconfig, vmdiagnostic 
/boot/loader/entries/\*.conf | linux-bootconfig 
/etc/HOSTNAME | agents, diagnostic, eg, lad, site-recovery, sql-iaas, vmdiagnostic, workloadbackup 
/etc/NetworkManager/\*.conf | diagnostic, eg, vmdiagnostic 
/etc/NetworkManager/conf.d/\*.conf | diagnostic, eg, vmdiagnostic 
/etc/\*-release | agents, diagnostic, eg, site-recovery, sql-iaas, vmdiagnostic, workloadbackup 
/etc/ambari-agent/conf/\* | hdinsight 
/etc/ambari-server/conf/\* | hdinsight 
/etc/apt/sources.list | linux-repoconfig 
/etc/apt/sources.list.d/\*.list | linux-repoconfig 
/etc/chrony/chrony.conf | diagnostic, vmdiagnostic 
/etc/cloud/cloud.cfg | diagnostic, diskpool, eg, vmdiagnostic 
/etc/cloud/cloud.cfg.d/\*.cfg | diagnostic, diskpool, eg, vmdiagnostic 
/etc/cni/net.d/\*.conflist | aks 
/etc/crypttab | diagnostic 
/etc/default/azuremonitoragent | azuremonitoragent 
/etc/default/grub | linux-bootconfig 
/etc/default/grub.d/\*.cfg | linux-bootconfig 
/etc/dhclient\*.conf | vmdiagnostic 
/etc/dhcp/\*.conf | diagnostic, eg, vmdiagnostic 
/etc/dnf/dnf.conf | linux-repoconfig 
/etc/dnf/vars/releasever | linux-repoconfig 
/etc/fstab | diagnostic, eg, normal, vmdiagnostic 
/etc/hadoop/conf/\* | hdinsight 
/etc/hbase/conf/\* | hdinsight 
/etc/hive2/conf/\* | hdinsight 
/etc/hostname | agents, diagnostic, eg, genspec, lad, site-recovery, sql-iaas, vmdiagnostic, workloadbackup 
/etc/hosts | diagnostic, hdinsight, linux-repoconfig 
/etc/hosts.allow | diagnostic 
/etc/hosts.deny | diagnostic 
/etc/idmapd.conf | diagnostic, vmdiagnostic 
/etc/kdump.conf | crashdump 
/etc/localtime | diagnostic 
/etc/modprobe.d/\*.conf | diagnostic 
/etc/netplan/\*.yaml | diagnostic, eg, vmdiagnostic 
/etc/network/interfaces | diagnostic, eg, vmdiagnostic 
/etc/network/interfaces.d/\*.cfg | diagnostic, eg, vmdiagnostic 
/etc/nsswitch.conf | diagnostic, eg, vmdiagnostic 
/etc/opt/microsoft/azuremonitoragent/amacoreagent/\* | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/configchunks/\* | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/configtransformid.txt | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/fluentbit/\*.conf | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/mcsconfig\* | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/mdsd\* | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/metricCounters.json | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/config-cache/syslog\* | azuremonitoragent 
/etc/opt/microsoft/azuremonitoragent/dmiinfo.txt | azuremonitoragent 
/etc/opt/microsoft/omsagent/LAD/conf/omsagent.d/\* | lad 
/etc/opt/microsoft/omsagent/\*/conf/omsagent.d/\*.conf | monitor-mgmt 
/etc/opt/microsoft/omsagent/conf/\*.conf | monitor-mgmt 
/etc/opt/omi/conf/\* | monitor-mgmt 
/etc/opt/omi/conf/omsconfig/agentid | monitor-mgmt 
/etc/opt/omi/conf/omsconfig/configuration/\*.mof | monitor-mgmt 
/etc/pam.d/\* | diagnostic 
/etc/products.d/\*.prod | linux-repoconfig 
/etc/regionserverclnt.cfg | linux-repoconfig 
/etc/resolv.conf | diagnostic, eg, vmdiagnostic 
/etc/rsyslog.conf | azuremonitoragent 
/etc/rsyslog.d/\*.conf | azuremonitoragent 
/etc/security/limits.conf | diagnostic 
/etc/selinux/config | diagnostic 
/etc/spark/conf/\* | hdinsight 
/etc/ssh/sshd_config | diagnostic, eg, normal, vmdiagnostic 
/etc/ssh/sshd_config.d/\* | diagnostic 
/etc/ssh/sshd_config.d/\*.conf | vmdiagnostic 
/etc/storm/conf/\* | hdinsight 
/etc/sudoers | diagnostic 
/etc/sudoers.d/\* | diagnostic 
/etc/sysconfig/SuSEfirewall2 | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/iptables | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network-scripts/ifcfg-\* | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network-scripts/ifcfg-eth0 | normal 
/etc/sysconfig/network-scripts/route-\* | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network/config | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network/dhcp | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network/ifcfg-\* | diagnostic, eg, vmdiagnostic 
/etc/sysconfig/network/routes | diagnostic, eg, vmdiagnostic 
/etc/sysctl.conf | diagnostic 
/etc/sysctl.d/\*.conf | diagnostic 
/etc/syslog-ng/\* | azuremonitoragent 
/etc/udev/rules.d/\*.rules | diagnostic 
/etc/ufw/ufw.conf | diagnostic, eg, vmdiagnostic 
/etc/waagent.conf | agents, diagnostic, eg, site-recovery, vmdiagnostic, workloadbackup 
/etc/wicked/\*.xml | diagnostic, eg, vmdiagnostic 
/etc/yum.conf | linux-repoconfig 
/etc/yum.repos.d/\*.repo | linux-repoconfig 
/etc/yum.repos.d/rh-cloud-rhel\*.repo | linux-repoconfig 
/etc/yum/vars/releasever | linux-repoconfig 
/etc/zypp/repos.d/\*.repo | linux-repoconfig 
/opt/microsoft/servicefabric/bin/Fabric/Fabric.Code/Fabric | servicefabric 
/opt/msawb/bin/AzureWLBackupCommonManagementSettings.json | workloadbackup 
/opt/msawb/bin/AzureWLBackupMonitoringSync_config.json | workloadbackup 
/opt/msawb/etc/config/SAPHana/\* | workloadbackup 
/opt/msawb/etc/config/global.json | workloadbackup 
/opt/msawb/var/lib/catalog/AutoHealCatalog/AutoHealTask/\*.bin | workloadbackup 
/opt/msawb/var/lib/catalog/InquiryCatalog/\*/\*.bin | workloadbackup 
/opt/msawb/var/lib/catalog/SyncObjectsCatalog/AlertEventsTable/\*.bin | workloadbackup 
/opt/msawb/var/lib/catalog/SyncObjectsCatalog/DatasourceSyncTable/\*.bin | workloadbackup 
/opt/msawb/var/lib/catalog/WorkloadExtDatasourceCatalog/\*/\*.bin | workloadbackup 
/opt/msawb/var/lib/catalog/WorkloadSchedules/\*/\*.bin | workloadbackup 
/opt/msawb/var/log/\*/\*/\* | workloadbackup 
/opt/msawb/var/log/\*/\*/\*/\*/\* | workloadbackup 
/opt/mssql/bin/mssql-conf | sql-iaas 
/run/NetworkManager/\*.conf | eg 
/run/NetworkManager/conf.d/\*.conf | eg 
/run/azure-vnet\* | aks 
/run/cloud-init/cloud.cfg | diskpool, eg 
/run/cloud-init/dhclient.hooks/\*.json | eg 
/run/cloud-init/ds-identify.log | diskpool, eg 
/run/cloud-init/result.json | diskpool, eg 
/run/cloud-init/status.json | diskpool, eg 
/run/resolvconf/\*.conf | eg 
/run/systemd/netif/leases/\* | eg 
/run/systemd/resolve/\*.conf | eg 
/sys/kernel/security/apparmor/profiles | diagnostic 
/tmp/omsagent\*.tgz | monitor-mgmt 
/tmp/sosreport\*.tar.xz | linux-sos-scc 
/usr/lib/NetworkManager/\*.conf | diagnostic, eg, vmdiagnostic 
/usr/lib/NetworkManager/conf.d/\*.conf | diagnostic, eg, vmdiagnostic 
/var/crash/\* | crashdump 
/var/lib/.jupyter/jupyter_notebook_config.py | hdinsight 
/var/lib/GuestConfig/Configuration/\* | monitor-mgmt 
/var/lib/GuestConfig/gc_agent_logs/\* | monitor-mgmt 
/var/lib/NetworkManager/\*.conf | diagnostic, eg, vmdiagnostic 
/var/lib/NetworkManager/\*.lease | diagnostic, eg, vmdiagnostic 
/var/lib/NetworkManager/\*.leases | diagnostic, eg, vmdiagnostic 
/var/lib/NetworkManager/\*.state | diagnostic, eg, vmdiagnostic 
/var/lib/NetworkManager/conf.d/\*.conf | diagnostic, eg, vmdiagnostic 
/var/lib/dhclient/\*.lease | diagnostic, eg, vmdiagnostic 
/var/lib/dhclient/\*.leases | diagnostic, eg, vmdiagnostic 
/var/lib/dhcp/\*.lease | diagnostic, eg, vmdiagnostic 
/var/lib/dhcp/\*.leases | diagnostic, eg, vmdiagnostic 
/var/lib/waagent/ExtensionsConfig.\*.xml | diagnostic, lad, vmdiagnostic 
/var/lib/waagent/GoalState.\*.xml | diagnostic, site-recovery, vmdiagnostic, workloadbackup 
/var/lib/waagent/HostingEnvironmentConfig.xml | diagnostic, vmdiagnostic 
/var/lib/waagent/Incarnation | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/ManagedIdentity-\*.json | diagnostic, vmdiagnostic 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/\* | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/\*.settings | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/metrics_con<br>figs/\*Configuration.json | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/telegraf_co<br>nfigs/telegraf.conf | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/telegraf_co<br>nfigs/telegraf.d/\* | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/status/\*.status | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-1.1.0.2 | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*.\*/HandlerEn<br>vironment.json | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*.\*/status/\*<br>.status | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/HandlerManif<br>est.json | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/Service/curr<br>ent.config | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/config/\*.se<br>ttings | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/heartbeat.lo<br>g | servicefabric 
/var/lib/waagent/Microsoft.EnterpriseCloud.Monitoring.OmsAgentForLinux-\*/\* | monitor-mgmt, monitor-mgmt 
/var/lib/waagent/Microsoft.EnterpriseCloud.Monitoring.OmsAgentForLinux.\*.manifest.xm<br>l | monitor-mgmt, monitor-mgmt 
/var/lib/waagent/Microsoft.OSTCExtensions.LinuxDiagnostic-\*/xmlCfg.xml | servicefabric 
/var/lib/waagent/Microsoft.SqlServer.Management.SqlIaaSAgentLinux\*/HandlerEnvironmen<br>t.json | sql-iaas 
/var/lib/waagent/Microsoft.SqlServer.Management.SqlIaaSAgentLinux\*/HandlerManifest.j<br>son | sql-iaas 
/var/lib/waagent/Microsoft.SqlServer.Management.SqlIaaSAgentLinux\*/config/\* | sql-iaas 
/var/lib/waagent/Microsoft.SqlServer.Management.SqlIaaSAgentLinux\*/deployer.log | sql-iaas 
/var/lib/waagent/Microsoft.SqlServer.Management.SqlIaaSAgentLinux\*/status/\* | sql-iaas 
/var/lib/waagent/Microsoft.\*LinuxDiagnostic\*/config/\*.settings | lad 
/var/lib/waagent/Microsoft.\*LinuxDiagnostic\*/status/\*.status | lad 
/var/lib/waagent/Microsoft.\*LinuxDiagnostic\*/xmlCfg.xml | lad 
/var/lib/waagent/SharedConfig.xml | diagnostic, vmdiagnostic 
/var/lib/waagent/\*.agentsManifest | agents 
/var/lib/waagent/\*.manifest.xml | diagnostic, vmdiagnostic 
/var/lib/waagent/\*.xml | agents, site-recovery, workloadbackup 
/var/lib/waagent/\*/config/HandlerState | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*/config/HandlerStatus | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*/config/VMApp.lockfile | agents, diagnostic 
/var/lib/waagent/\*/config/\*.settings | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/\*/config/applicationRegistry.active | agents, diagnostic 
/var/lib/waagent/\*/error.json | diagnostic, vmdiagnostic 
/var/lib/waagent/\*/status/\*.status | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/error.json | agents, eg 
/var/lib/waagent/history/\*.zip | agents, diagnostic, vmdiagnostic 
/var/lib/waagent/provisioned | diagnostic, eg, genspec, vmdiagnostic 
/var/lib/waagent/waagent_status.\*.json | agents, diagnostic, eg, vmdiagnostic 
/var/lib/waagent/waagent_status.json | agents, diagnostic, eg, vmdiagnostic 
/var/lib/wicked/lease\* | diagnostic, eg, vmdiagnostic 
/var/log/AzureRcmCli.log | site-recovery 
/var/log/ambari-agent/ambari-agent.log | hdinsight 
/var/log/ambari-server/ambari-audit.log | hdinsight 
/var/log/ambari-server/ambari-server.log | hdinsight 
/var/log/auth\* | agents, diagnostic, eg, normal, vmdiagnostic 
/var/log/azure-cns\* | aks 
/var/log/azure-ipam\* | aks 
/var/log/azure-npm.log | aks 
/var/log/azure-proxy-agent/\* | agents, normal 
/var/log/azure-vnet\* | aks 
/var/log/azure/Microsoft.AKS.Compute.AKS.Linux.AKSNode/extension.log | aks 
/var/log/azure/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent/\*/\*.log | azuremonitoragent 
/var/log/azure/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode/\*.\*/CommandExec<br>ution.log | servicefabric 
/var/log/azure/Microsoft.EnterpriseCloud.Monitoring.OmsAgentForLinux/\*/\*.log | monitor-mgmt 
/var/log/azure/Microsoft.OSTCExtensions.DSCForLinux/extension.log | monitor-mgmt 
/var/log/azure/Microsoft.OSTCExtensions.LinuxDiagnostic/\*/mdsd.\* | servicefabric 
/var/log/azure/Microsoft.SqlServer.Management.SqlIaaSAgentLinux\* | sql-iaas 
/var/log/azure/Microsoft.\*LinuxDiagnostic/\*/\* | lad 
/var/log/azure/\* | site-recovery, workloadbackup 
/var/log/azure/\*/\* | agents, diagnostic, vmdiagnostic 
/var/log/azure/\*/\*/\* | agents, diagnostic, vmdiagnostic 
/var/log/azure/cluster-provision-cse-output.log | aks 
/var/log/azure/cluster-provision.log | aks, diagnostic, vmdiagnostic 
/var/log/azure/containerd-status.log | aks 
/var/log/azure/custom-script/handler.log | agents, diagnostic, vmdiagnostic 
/var/log/azure/docker-status.log | aks 
/var/log/azure/kern.log | aks 
/var/log/azure/kubelet-status.log | aks 
/var/log/azure/run-command/handler.log | diagnostic, vmdiagnostic 
/var/log/boot\* | diagnostic, eg, normal, vmdiagnostic 
/var/log/cilium-cni\* | aks 
/var/log/cloud-init\* | aks, diagnostic, diskpool, eg, normal, vmdiagnostic 
/var/log/cloudregister | diagnostic 
/var/log/cluster/\* | diagnostic 
/var/log/corosync/\* | diagnostic 
/var/log/corosync\* | diagnostic 
/var/log/diskpool-agent\* | diskpool 
/var/log/diskpool/bootstrapper.log\* | diskpool 
/var/log/dmesg\* | agents, diagnostic, eg, normal, site-recovery, vmdiagnostic, workloadbackup 
/var/log/dnf\* | diagnostic, eg, vmdiagnostic 
/var/log/dpkg.log | servicefabric 
/var/log/dpkg\* | diagnostic, diskpool, eg, normal, vmdiagnostic 
/var/log/evtcollforw\*.log | site-recovery 
/var/log/hadoop-yarn/yarn/\*.log | hdinsight 
/var/log/hdinsight-agent/hdinsight-agent.log | hdinsight 
/var/log/hdinsight-agent/hdinsight-agent.out | hdinsight 
/var/log/hdinsight-provisioning-agent/hdinsight-provisioning-agent.log | hdinsight 
/var/log/hdinsight-startupagent/hdinsight-startupagent.log | hdinsight 
/var/log/hdinsight-startupagent/hdinsight-startupagent.out | hdinsight 
/var/log/hive/hivemetastore.log | hdinsight 
/var/log/hive/hiveserver2.log | hdinsight 
/var/log/journal/\*/\* | aks 
/var/log/kern.log | servicefabric 
/var/log/kern\* | diagnostic, diskpool, eg, normal, vmdiagnostic 
/var/log/messages\* | azuremonitoragent, diagnostic, eg, monitor-mgmt, normal, vmdiagnostic 
/var/log/nvidia\*.log | aks 
/var/log/pacemaker/\* | diagnostic 
/var/log/pacemaker\* | diagnostic 
/var/log/pods/calico-system\*/\*/\*.log\* | aks 
/var/log/pods/kube-system\*/\*/\*.log\* | aks 
/var/log/pods/kured\*/\*/\*.log\* | aks 
/var/log/pods/tigera-operator\*/\*/\*.log\* | aks 
/var/log/rhuicheck.log | linux-repoconfig 
/var/log/rsyslog\* | diagnostic, eg, lad, normal, vmdiagnostic 
/var/log/s2\*.log | site-recovery 
/var/log/sa/sa\* | performance 
/var/log/scc\*.txz | linux-sos-scc 
/var/log/secure\* | diagnostic, eg, normal, vmdiagnostic 
/var/log/sfnode/handler.trace | servicefabric 
/var/log/sfnode/loguploader.trace | servicefabric 
/var/log/sfnode/sfnodelog.trace | servicefabric 
/var/log/svagents\*.log | site-recovery 
/var/log/syslog | aks, servicefabric 
/var/log/syslog\* | agents, azuremonitoragent, diagnostic, diskpool, eg, lad, monitor-mgmt, normal, site-recovery, vmdiagnostic, workloadbackup 
/var/log/ua_install.log | site-recovery 
/var/log/waagent.log | servicefabric 
/var/log/waagent\* | agents, diagnostic, eg, lad, normal, site-recovery, vmdiagnostic, workloadbackup 
/var/log/waagent\*.log | azuremonitoragent, monitor-mgmt 
/var/log/yum\* | diagnostic, eg, normal, vmdiagnostic 
/var/log/zypp/history | diagnostic 
/var/opt/microsoft/azuremonitoragent/events/taskstate.json | azuremonitoragent 
/var/opt/microsoft/azuremonitoragent/log/\* | azuremonitoragent 
/var/opt/microsoft/omsagent/LAD/log/\* | lad 
/var/opt/microsoft/omsagent/\*/log/omsagent.log | monitor-mgmt 
/var/opt/microsoft/omsagent/\*/run/automationworker/omsupdatemgmt.log | monitor-mgmt 
/var/opt/microsoft/omsagent/run/automationworker/worker.log | monitor-mgmt 
/var/opt/microsoft/omsconfig/omsconfig.log | monitor-mgmt 
/var/opt/microsoft/omsconfig/omsconfigdetailed.log | monitor-mgmt 
/var/opt/microsoft/scx/log/scx.log | monitor-mgmt 
/var/opt/mssql/log/\*.tar.gz2 | sql-iaas 
/var/opt/mssql/log/errorlog\* | sql-iaas 
/var/opt/mssql/setup\* | sql-iaas 
/var/opt/omi/log/\*.log | monitor-mgmt 
/var/run/azure-vnet\* | aks 
/var/spool/cron/tabs/root | workloadbackup 
/var/tmp/sosreport\*.tar.xz | linux-sos-scc 
copy | sql-iaas 
## windows 
File Path | Manifest 
------------- | ------------- 
/$Windows.~BT/Sources/Panther/miglog.xml | windowsupdate 
/$Windows.~BT/Sources/Panther/setupact.log | windowsupdate 
/$Windows.~BT/Sources/Panther/setuperr.log | windowsupdate 
/AzureData/CustomDataSetupScript.log | aks 
/AzureData/CustomDataSetupScript.ps1 | aks 
/Boot/BCD | windowsupdate 
/CalicoWindows/logs/\*.log | aks 
/Packages/Plugins/ESET.FileSecurity/\*/agent_version.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/ESET.FileSecurity/\*/extension_version.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/AnalyzerConfigTempla<br>te.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Logs/\*DiagnosticsPl<br>ugin\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/StatusMonitor/Applic<br>ationInsightsPackagesVersion.json | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*.config | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/schema/wad\*.json | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/SeqNumber.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Microsoft.WindowsAzure.Stora<br>ge.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/AsmExtensio<br>nMonitoringConfig\*.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/ASM.Azure.OSBaseline.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmExtensionSecurityPackStartupConfig.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScan.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScannerConfiguration.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/Azure.Common.scm.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityPackStartup.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityScanLoggerManifest.man | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/MonAgent-Pk<br>g-Manifest.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEvents.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEventsMin.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardExtensions.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AntiMalwareEvents.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEvents.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEventsCore.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsRootEvents.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents2.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents3.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents2.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents3.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentCertThumbprin<br>ts.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentScheduledServ<br>ice.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/InstallUtil.Inst<br>allLog | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/Infrastr<br>uctureManifest.template.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallLog | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallState | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/current.<br>config | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/RuntimeSett<br>ings/VMApp.lockfile | agents, diagnostic 
/Packages/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/RuntimeSett<br>ings/applicationRegistry.active | agents, diagnostic 
/Packages/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/RuntimeSett<br>ings/applicationRegistry.backup | agents, diagnostic 
/Packages/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/RuntimeSettings<br>/VMApp.lockfile | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/RuntimeSettings<br>/applicationRegistry.active | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/RuntimeSettings<br>/applicationRegistry.backup | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo.def.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/PluginManifest.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/config.bgi | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/emptyConfig.bgi | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCVersion.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/HotfixInstallInProgress.dsc | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/PreInstallDone.dsc | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dpx | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dsc | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/CommandExecution\*.l<br>og | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/HandlerEnvironment.j<br>son | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/HandlerManifest.json | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/PackageDefinition.xm<br>l | agents, diagnostic, normal, sql-iaas, vmdiagnostic, windowsupdate 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/RuntimeSettings/\*.s<br>ettings | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/Status/HeartBeat.Jso<br>n | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/Status/\*.status | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/config.txt | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/installation_log | sql-iaas 
/Packages/Plugins/\* | monitor-mgmt 
/Packages/Plugins/\*/\*/HandlerEnvironment.json | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/Packages/Plugins/\*/\*/HandlerManifest.json | agents, diagnostic, normal, servicefabric, servicefabric, vmdiagnostic, windowsupdate 
/Packages/Plugins/\*/\*/PackageInformation.txt | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/Packages/Plugins/\*/\*/RuntimeSettings/\*.settings | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/Packages/Plugins/\*/\*/Status/HeartBeat.Json | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/Packages/Plugins/\*/\*/Status/\*.status | agents, normal, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/config.txt | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/AzureRcmCli.log | site-recovery, windowsupdate 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/evtcollforw\*.log | site-recovery, windowsupdate 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/s2\*.log | site-recovery, windowsupdate 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/svagents\*.log | site-recovery, windowsupdate 
/Program Files/Azure Workload Backup/Catalog/InquiryCatalog/\*/\*.bin | workloadbackup 
/Program Files/Azure Workload Backup/Catalog/SyncObjectsCatalog/AlertEventsTable/\*.b<br>in | workloadbackup 
/Program Files/Azure Workload Backup/Catalog/SyncObjectsCatalog/DatasourceSyncTable/\<br>*.bin | workloadbackup 
/Program Files/Azure Workload Backup/Catalog/WorkloadExtDatasourceCatalog/\*/\*.bin | workloadbackup 
/Program Files/Azure Workload Backup/Catalog/WorkloadSchedules/\*/\*.bin | workloadbackup 
/Program Files/Azure Workload Backup/bin/AzureWLBackupCommonManagementSettings.json | workloadbackup 
/Program Files/Azure Workload Backup/bin/AzureWLBackupMonitoringSync_config.json | workloadbackup 
/Program Files/Microsoft Dependency Agent/logs/\*.\* | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/CT_\*/work/Servi<br>ceState/\*.log | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/FCT_\*/work/Inve<br>ntory/asmhost.log | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/FCT_\*/work/Inve<br>ntory/localhost.json | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/FCT_\*/work/Inve<br>ntory/localhost.mof | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/FCT_\*/work/asmh<br>ost.log | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/FCT_\*/work/loca<br>lhost.mof | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/FCT_\*/work/loca<br>lhost.prevmof | monitor-mgmt 
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/Management Packs<br>/\*.xml | monitor-mgmt 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/ERRORLOG | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/ERRORLOG.\* | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/ExtensibilityLog/ExtensibilityLog/EX<br>TLAUNCHERRORLOG | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/ExtensibilityLog/ExtensibilityLog/\*<br>.bin | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/ExtensibilityLog/ExtensibilityLog/\*<br>.log | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/FDLAUNCHERRORLOG | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/FDLAUNCHERRORLOG.\* | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/SQLAGENT.\* | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/\*.log | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/\*.mdmp | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/\*.trc | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/\*.txt | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/\*.xel | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/fd | sql-iaas 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/fd.\* | sql-iaas 
/Program Files/Microsoft SQL Server/\*/Setup Bootstrap/Log/Summary.txt | sql-iaas 
/Program Files/Microsoft SQL Server/\*/Setup Bootstrap/Log/\*/Log\*.cab | sql-iaas 
/Program Files/containerd/config.toml | aks 
/ProgramData/ASRSetupLogs/ASRUnifiedAgentConfigurator.log | site-recovery, windowsupdate 
/ProgramData/ASRSetupLogs/ASRUnifiedAgentInstaller.log | site-recovery, windowsupdate 
/ProgramData/ASRSetupLogs/UnifiedAgentMSIInstall.log | site-recovery, windowsupdate 
/ProgramData/ASRSetupLogs/WrapperUnifiedAgent.log | site-recovery, windowsupdate 
/ProgramData/GuestConfig/Configuration/\* | monitor-mgmt 
/ProgramData/GuestConfig/gc_agent_logs/\* | monitor-mgmt 
/ProgramData/Microsoft/System Center/Orchestrator/7.2/SMA/\*.\* | monitor-mgmt 
/ProgramData/USOShared/Logs/\*.etl | windowsupdate 
/ProgramData/UsoPrivate/UpdateStore/\*.xml | windowsupdate 
/ProgramData/containerd/root/panic.log | aks 
/Users/\*/AppData/Local/Packages/WinStore_cw5n1h2txyewy/AC/Temp/winstore.log | windowsupdate 
/Users/\*/AppData/Local/Temp/winstore.log | windowsupdate 
/Users/\*/AppData/Local/microsoft/windows/windowsupdate.log | windowsupdate 
/Windows.old/ProgramData/USOPrivate/UpdateStore | windowsupdate 
/Windows.old/ProgramData/USOShared/Logs | windowsupdate 
/Windows.old/Windows/Logs/WindowsUpdate/\*.etl | windowsupdate 
/Windows.old/Windows/Logs/mosetup/bluebox.log | windowsupdate 
/Windows.old/Windows/SoftwareDistribution/ReportingEvents.log | windowsupdate 
/Windows/INF/netcfg\*.\*etl | diagnostic, vmdiagnostic, windowsupdate 
/Windows/INF/setupapi.\*.log | windowsupdate 
/Windows/INF/setupapi.dev.log | diagnostic, vmdiagnostic 
/Windows/Inf/netcfg\*.\*etl | normal 
/Windows/Inf/setupapi.dev.log | normal 
/Windows/Logs/CBS/\*.cab | windowsupdate 
/Windows/Logs/CBS/\*.log | windowsupdate 
/Windows/Logs/DISM/\*.log | windowsupdate 
/Windows/Logs/MoSetup/UpdateAgent.log | windowsupdate 
/Windows/Logs/NetSetup/\*.etl | windowsupdate 
/Windows/Logs/OpsMgrTrace/\*.\* | monitor-mgmt 
/Windows/Logs/SIH/SIH.\*.etl | windowsupdate 
/Windows/Logs/SetupCleanupTask/setupact.log | windowsupdate 
/Windows/Logs/SetupCleanupTask/setuperr.log | windowsupdate 
/Windows/Logs/SystemRestore/\*.\* | windowsupdate 
/Windows/Logs/WindowsUpdate/WindowsUpdate.\*.etl | monitor-mgmt, windowsupdate 
/Windows/Logs/dpx/\*.log | windowsupdate 
/Windows/Logs/eBPF/committed/\* | agents, normal 
/Windows/Logs/mosetup/bluebox.log | windowsupdate 
/Windows/Logs/waasmedic/waasmedic.\*.etl | windowsupdate 
/Windows/Microsoft.NET/Framework/v4.0.30319/Config/machine.config | diagnostic, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/Microsoft.NET/Framework64/v4.0.30319/Config/machine.config | diagnostic, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/Minidump/\*.dmp | windowsupdate 
/Windows/Panther/FastCleanup/setupact.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/Panther/UnattendGC/setupact.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/Panther/VmAgentInstaller.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/Windows/Panther/WaSetup.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/Panther/WaSetup.xml | agents, diagnostic, eg, genspec, normal, site-recovery, vmdiagnostic, windowsupdate 
/Windows/Panther/miglog.xml | windowsupdate 
/Windows/Panther/setupact.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/Panther/setuperr.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/Panther/unattend.xml | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/ServiceProfiles/LocalService/AppData/Local/Microsoft/WSLicense/tokens.dat | windowsupdate 
/Windows/ServiceProfiles/NetworkService/AppData/Local/Microsoft/Windows/DeliveryOptim<br>ization/Logs/\*.etl | windowsupdate 
/Windows/Setup/State/State.ini | diagnostic, eg, genspec, vmdiagnostic, windowsupdate 
/Windows/Setup/State/state.ini | agents, normal 
/Windows/SoftwareDistribution/DeliveryOptimization/SavedLogs/\*.etl | windowsupdate 
/Windows/SoftwareDistribution/DeliveryOptimization/SavedLogs/\*.log | windowsupdate 
/Windows/SoftwareDistribution/Download/\*/\*/\*.log | windowsupdate 
/Windows/SoftwareDistribution/Download/\*/\*/\*.xml | windowsupdate 
/Windows/SoftwareDistribution/Plugins/7D5F3CBA-03DB-4BE5-B4B36DBED19A6833/117CAB2D-82<br>B1-4B5A-A08C-4D62DBEE7782.cache | windowsupdate 
/Windows/SoftwareDistribution/Plugins/7D5F3CBA-03DB-4BE5-B4B36DBED19A6833/TokenRetrie<br>val.log | windowsupdate 
/Windows/SoftwareDistribution/ReportingEvents.log | monitor-mgmt, windowsupdate 
/Windows/SoftwareDistribution/datastore/DataStore.edb | windowsupdate 
/Windows/System32/LogFiles/Firewall/pfirewall.log | windowsupdate 
/Windows/System32/LogFiles/Firewall/pfirewall.log.old | windowsupdate 
/Windows/System32/Sysprep/ActionFiles/Generalize.xml | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/ActionFiles/Respecialize.xml | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/ActionFiles/Specialize.xml | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/Panther/IE/setupact.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/Panther/IE/setuperr.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/Panther/setupact.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/Panther/setuperr.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Sysprep/Sysprep_succeeded.tag | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/System32/Tasks/Microsoft/IaaSWorkloadBackup/\* | workloadbackup 
/Windows/System32/Winevt/Logs/Microsoft-WS-Licensing%%4Admin.evtx | windowsupdate 
/Windows/System32/Winevt/Logs/\*AppX\*.evtx | windowsupdate 
/Windows/System32/config/SOFTWARE | diagnostic, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/config/SOFTWARE.LOG1 | min-diagnostic 
/Windows/System32/config/SOFTWARE.LOG2 | min-diagnostic 
/Windows/System32/config/SYSTEM | diagnostic, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/config/SYSTEM.LOG1 | min-diagnostic 
/Windows/System32/config/SYSTEM.LOG2 | min-diagnostic 
/Windows/System32/winevt/Logs/Application.evtx | agents, aks, diagnostic, eg, min-diagnostic, normal, servicefabric, site-recovery, sql-iaas, vmdiagnostic, windowsupdate, workloadbackup 
/Windows/System32/winevt/Logs/Microsoft-AKSGMSAPlugin%4Admin.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Automation%4Operational.evtx | monitor-mgmt 
/Windows/System32/winevt/Logs/Microsoft-SMA%4Debug.etl | monitor-mgmt 
/Windows/System32/winevt/Logs/Microsoft-SMA%4Operational.evtx | monitor-mgmt 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Admin.evtx | diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Operational.evtx | diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Admin.evtx | diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Operational.evtx | diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker%4BitLocker Management.evtx | diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker-DrivePreparationTool%4Opera<br>tional.evtx | diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Bits-Client%%4Operational.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-CAPI2%4Operational.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Containers-CCG%4Admin.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-DSC%4Operational.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-DeliveryOptimization%%4Operational.ev<br>tx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Admin.evtx | eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Operational.evtx | eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Host-Network-Service-Admin.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Host-Network-Service-Operational.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Hyper-V-Compute-Admin.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Hyper-V-Compute-Operational.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%%4Configuration.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%4Configuration.evtx | agents, diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnPConfig%4Configuration.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NdisImPlatform%4Operational.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkLocationWizard%4Operational.ev<br>tx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProfile%4Operational.evtx | agents, diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProvider%4Operational.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NlaSvc%4Operational.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Admi<br>n.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Oper<br>ational.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RemoteDesktopSe<br>ssionManager%4Admin.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-SessionServices<br>%4Operational.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Resource-Exhaustion-Detector%4Operati<br>onal.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBClient%4Operational.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Connectivity.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Operational.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-ServerManager%4Operational.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SmbClient%4Connectivity.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Store%%4Operational.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TCPIP%4Operational.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TaskScheduler%%4Operational.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Admin.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Operational.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Admin.ev<br>tx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Operatio<br>nal.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RDPClient%4Operation<br>al.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Admin.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Operational.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Admin.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Operational.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-UserPnp%4DeviceInstall.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4ConnectionSecurity.evtx | agents, diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4Firewall.evtx | agents, diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%%4Operational.evt<br>x | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%4Operational.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Bootstrapper.evtx | agents, diagnostic, eg, monitor-mgmt, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4GuestAgent.evtx | agents, diagnostic, eg, monitor-mgmt, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Heartbeat.evtx | agents, diagnostic, eg, monitor-mgmt, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Runtime.evtx | agents, diagnostic, eg, monitor-mgmt, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4GuestAgent.evtx | agents, diagnostic, eg, monitor-mgmt, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4Plugins.evtx | agents, diagnostic, eg, monitor-mgmt, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/MicrosoftAzureRecoveryServices-Replication.evtx | diagnostic, eg, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Security.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Setup.evtx | diagnostic, eg, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/System32/winevt/Logs/System.evtx | agents, aks, diagnostic, eg, min-diagnostic, normal, servicefabric, site-recovery, sql-iaas, vmdiagnostic, windowsupdate, workloadbackup 
/Windows/System32/winevt/Logs/Windows Azure.evtx | agents, diagnostic, eg, monitor-mgmt, normal, site-recovery, vmdiagnostic, windowsupdate, workloadbackup 
/Windows/System32/winevt/Logs/Windows PowerShell.evtx | monitor-mgmt 
/Windows/Temp/MOMPerfCtrsInstall.log | monitor-mgmt 
/Windows/Temp/MonitoringAgent.log | monitor-mgmt 
/Windows/WinSxS/pending.xml | windowsupdate 
/Windows/WinSxS/poqexec.log | windowsupdate 
/Windows/WindowsUpdate.log | monitor-mgmt 
/Windows/debug/DCPROMO.LOG | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/debug/NetSetup.LOG | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/debug/PASSWD.LOG | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/debug/dcpromoui.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/debug/mrt.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/debug/netlogon.log | diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/Windows/servicing/sessions/sessions.xml | diagnostic, min-diagnostic, vmdiagnostic, windowsupdate 
/Windows/system32/winevt/Logs/Operations Manager.evtx | monitor-mgmt 
/Windows/windowsupdate\*.log | windowsupdate 
/WindowsAzure/Config/\* | monitor-mgmt 
/WindowsAzure/GuestAgent\*/CommonAgentConfig.config | diagnostic, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/AggregateStatus/\*.json | monitor-mgmt 
/WindowsAzure/Logs/AggregateStatus/aggregatestatus\*.json | agents, diagnostic, eg, min-diagnostic, normal, vmdiagnostic, windowsupdate, workloadbackup 
/WindowsAzure/Logs/AppAgentRuntime.log | agents, diagnostic, eg, normal, vmdiagnostic, windowsupdate, workloadbackup 
/WindowsAzure/Logs/MonitoringAgent.log | agents, diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ActiveDirectory.AADLoginForWindows/\*/\*.l<br>og | diagnostic, vmdiagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ActiveDirectory.AADLoginForWindows/\*/\*.t<br>xt | diagnostic, vmdiagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>Plugin.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>PluginLauncher.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/Checkpoint.txt | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MaConfig.xml | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MonAgentHost.\*.log | agents, diagnostic, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/IaaSBcdrExt<br>ension\*.log | agents, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.AzureDiskEncryption/\*/BitlockerE<br>xtension.log | diagnostic, vmdiagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.IaaSAntimalware/\*/AntimalwareCon<br>fig.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.Monitoring/\*/AsmExtension.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/FabricM<br>SIInstall\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Infrast<br>ructureManifest.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/TempClu<br>sterManifest.xml | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/VCRunti<br>meInstall\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/\*<br>.log | agents, diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/lo<br>g_\* | agents, diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.RunCommandHandlerWindows/\*/\*.log | diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.RunCommandWindows/\*/\*.log | diagnostic, vmdiagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/log_\* | agents, diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.WindowsPatchExtension/\*/windowsUpdat<br>eLog/\* | diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.CustomScriptExtension/\*/\*.log | diagnostic, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.JsonADDomainExtension/\*/ADDomainExtensi<br>on.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.VMAccessAgent/\*/JsonVMAccessExtension.l<br>og | agents, diagnostic, min-diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.EnterpriseCloud.Monitoring.MicrosoftMonitoringAg<br>ent/\*/0.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.ManagedIdentity.ManagedIdentityExtensionForWindo<br>ws/\*/RuntimeSettings/\*.xml | diagnostic, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DSCLOG\*.json | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DscExtensionHandler\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/CommandExec<br>ution\*.log | sql-iaas 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/ExtensionLo<br>g\*.log | sql-iaas 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/SqlCustomer<br>SupportLogs/\* | sql-iaas 
/WindowsAzure/Logs/Plugins/Symantec.SymantecEndpointProtection/\*/sepManagedAzure.txt | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/TrendMicro.DeepSecurity.TrendMicroDSA/\*/\*.log | agents, diagnostic, normal, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/\* | site-recovery, workloadbackup 
/WindowsAzure/Logs/Plugins/\*/\*/CommandExecution.log | agents, diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/\*/\*/Heartbeat.log | agents, diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/\*/\*/Install.log | agents, diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/\*/\*/Update.log | agents, diagnostic, eg, normal, servicefabric, vmdiagnostic, windowsupdate 
/WindowsAzure/Logs/SqlServerLogs/ERRORLOG | sql-iaas 
/WindowsAzure/Logs/SqlServerLogs/\*.txt | sql-iaas 
/WindowsAzure/Logs/SqlServerLogs/\*.xel | sql-iaas 
/WindowsAzure/Logs/Telemetry.log | agents, diagnostic, eg, normal, site-recovery, vmdiagnostic, windowsupdate, workloadbackup 
/WindowsAzure/Logs/TransparentInstaller.log | agents, asc-vmhealth, diagnostic, eg, min-diagnostic, normal, site-recovery, vmdiagnostic, windowsupdate, workloadbackup 
/WindowsAzure/Logs/VFPlugin/\*.log | monitor-mgmt 
/WindowsAzure/Logs/WaAppAgent.log | agents, diagnostic, eg, min-diagnostic, normal, site-recovery, vmdiagnostic, windowsupdate, workloadbackup 
/WindowsAzure/Logs/\*.log | monitor-mgmt 
/WindowsAzure/Logs/plugins/\*/\*/\*.log | monitor-mgmt 
/WindowsAzure/ProxyAgent/Logs/\* | agents, normal 
/WindowsAzure/config/\*.xml | agents, diagnostic, eg, normal, vmdiagnostic, windowsupdate 
/WindowsUpdateVerbose.etl | windowsupdate 
/k/\*.err | aks 
/k/\*.log | aks 
/k/azure-vnet-ipam.json | aks 
/k/azure-vnet-ipam.log | aks 
/k/azure-vnet.json | aks 
/k/azure-vnet.log | aks 
/k/bootstrap-config | aks 
/k/kubeclusterconfig.json | aks 
/unattend.xml | diagnostic, eg, normal, vmdiagnostic, windowsupdate 

*File was created by running [parse_manifest.py](../tools/parse_manifest.py) on `2024-05-31 16:54:08.065129`*