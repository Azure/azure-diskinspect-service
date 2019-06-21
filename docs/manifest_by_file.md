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
/var/lib/waagent/ExtensionsConfig.\*.xml | agents, diagnostic 
/var/lib/waagent/GoalState.\*.xml | agents, diagnostic 
/var/lib/waagent/HostingEnvironmentConfig.xml | agents, diagnostic 
/var/lib/waagent/Microsoft.OSTCExtensions.CustomScriptForLinux.\*.manifest.xml | agents, diagnostic 
/var/lib/waagent/Prod.\*.manifest.xml | agents, diagnostic 
/var/lib/waagent/SharedConfig.xml | agents, diagnostic 
/var/lib/waagent/\*.xml | agents 
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
/boot/grub\*/grub.c\* | diagnostic, eg 
/boot/grub\*/menu.lst | diagnostic, eg 
/etc/HOSTNAME | agents, diagnostic, eg, lad, site-recovery, workloadbackup 
/etc/\*-release | agents, diagnostic, eg, site-recovery, workloadbackup 
/etc/ambari-agent/conf/\* | hdinsight 
/etc/ambari-server/conf/\* | hdinsight 
/etc/fstab | diagnostic, eg, normal 
/etc/hadoop/conf/\* | hdinsight 
/etc/hbase/conf/\* | hdinsight 
/etc/hive2/conf/\* | hdinsight 
/etc/hostname | agents, diagnostic, eg, genspec, lad, site-recovery, workloadbackup 
/etc/hosts | hdinsight 
/etc/netplan/50-cloud-init.yaml | diagnostic, eg 
/etc/network/interfaces | diagnostic, eg 
/etc/network/interfaces.d/\*.cfg | diagnostic, eg 
/etc/nsswitch.conf | diagnostic 
/etc/opt/microsoft/omsagent/LAD/conf/omsagent.d/\* | lad 
/etc/opt/microsoft/omsagent/\*/conf/omsagent.d/\*.conf | monitor-mgmt 
/etc/opt/microsoft/omsagent/conf/omsagent.conf | monitor-mgmt 
/etc/opt/omi/conf/omsconfig/agentid | monitor-mgmt 
/etc/opt/omi/conf/omsconfig/configuration/\*.mof | monitor-mgmt 
/etc/resolv.conf | diagnostic, eg 
/etc/spark/conf/\* | hdinsight 
/etc/ssh/sshd_config | diagnostic, normal 
/etc/storm/conf/\* | hdinsight 
/etc/sysconfig/SuSEfirewall2 | diagnostic, eg 
/etc/sysconfig/iptables | diagnostic, eg 
/etc/sysconfig/network | diagnostic, eg 
/etc/sysconfig/network-scripts/ifcfg-eth\* | diagnostic, eg 
/etc/sysconfig/network-scripts/route-eth\* | diagnostic, eg 
/etc/sysconfig/network/ifcfg-eth\* | diagnostic, eg 
/etc/sysconfig/network/routes | diagnostic, eg 
/etc/ufw/ufw.conf | diagnostic, eg 
/etc/waagent.conf | agents, diagnostic, eg, site-recovery, workloadbackup 
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
/tmp/omsagent\*.tgz | monitor-mgmt 
/var/lib/.jupyter/jupyter_notebook_config.py | hdinsight 
/var/lib/dhclient/dhclient-eth0.leases | diagnostic, eg 
/var/lib/dhcp/dhclient.eth0.leases | diagnostic, eg 
/var/lib/waagent/ExtensionsConfig.\*.xml | diagnostic, lad 
/var/lib/waagent/GoalState.\*.xml | diagnostic, site-recovery, workloadbackup 
/var/lib/waagent/HostingEnvironmentConfig.xml | diagnostic 
/var/lib/waagent/Incarnation | agents, diagnostic 
/var/lib/waagent/ManagedIdentity-\*.json | diagnostic 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-1.1.0.2 | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*.\*/HandlerEn<br>vironment.json | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*.\*/status/\*<br>.status | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/HandlerManif<br>est.json | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/Service/curr<br>ent.config | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/config/\*.se<br>ttings | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode-\*/heartbeat.lo<br>g | servicefabric, servicefabric 
/var/lib/waagent/Microsoft.OSTCExtensions.LinuxDiagnostic-\*/xmlCfg.xml | servicefabric 
/var/lib/waagent/Microsoft.\*LinuxDiagnostic\*/config/\*.settings | lad 
/var/lib/waagent/Microsoft.\*LinuxDiagnostic\*/status/\*.status | lad 
/var/lib/waagent/Microsoft.\*LinuxDiagnostic\*/xmlCfg.xml | lad 
/var/lib/waagent/SharedConfig.xml | diagnostic 
/var/lib/waagent/\*.agentsManifest | agents 
/var/lib/waagent/\*.manifest.xml | diagnostic 
/var/lib/waagent/\*.xml | agents, site-recovery, workloadbackup 
/var/lib/waagent/\*/config/\*.settings | agents, diagnostic 
/var/lib/waagent/\*/status/\*.status | agents, diagnostic 
/var/lib/waagent/error.json | agents, diagnostic 
/var/lib/waagent/history/\*.zip | agents, diagnostic 
/var/lib/waagent/provisioned | diagnostic, eg, genspec 
/var/lib/waagent/waagent_status.json | agents, diagnostic 
/var/lib/wicked/lease-eth0-dhcp-ipv4.xml | diagnostic, eg 
/var/log/AzureRcmCli.log | site-recovery 
/var/log/auth\* | agents, diagnostic, eg, normal 
/var/log/azure-vnet.log | aks 
/var/log/azure/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode/\*.\*/CommandExec<br>ution.log | servicefabric 
/var/log/azure/Microsoft.EnterpriseCloud.Monitoring.OmsAgentForLinux/\*/\*.log | monitor-mgmt 
/var/log/azure/Microsoft.OSTCExtensions.LinuxDiagnostic/\*/mdsd.\* | servicefabric 
/var/log/azure/Microsoft.\*LinuxDiagnostic/\*/\* | lad 
/var/log/azure/\* | site-recovery, workloadbackup 
/var/log/azure/\*/\* | agents, diagnostic 
/var/log/azure/\*/\*/\* | agents, diagnostic 
/var/log/azure/cluster-provision.log | aks 
/var/log/azure/custom-script/handler.log | agents, diagnostic 
/var/log/azure/docker-status.log | aks 
/var/log/azure/kern.log | aks 
/var/log/azure/kubelet-status.log | aks 
/var/log/boot\* | diagnostic, eg, normal 
/var/log/cloud-init-output.log | aks 
/var/log/cloud-init\* | diagnostic, eg, normal 
/var/log/dmesg\* | agents, diagnostic, eg, normal, site-recovery, workloadbackup 
/var/log/dpkg.log | servicefabric 
/var/log/dpkg\* | diagnostic, eg, normal 
/var/log/evtcollforw\*.log | site-recovery 
/var/log/journal/\*/\* | aks 
/var/log/kern.log | servicefabric 
/var/log/kern\* | diagnostic, eg, normal 
/var/log/messages\* | diagnostic, eg, monitor-mgmt, normal 
/var/log/rsyslog\* | diagnostic, eg, lad, normal 
/var/log/s2\*.log | site-recovery 
/var/log/sa/sar\* | performance 
/var/log/secure\* | diagnostic, eg, normal 
/var/log/sfnode/handler.trace | servicefabric 
/var/log/sfnode/loguploader.trace | servicefabric 
/var/log/sfnode/sfnodelog.trace | servicefabric 
/var/log/svagents\*.log | site-recovery 
/var/log/syslog | aks, servicefabric 
/var/log/syslog\* | agents, diagnostic, eg, lad, monitor-mgmt, normal, site-recovery, workloadbackup 
/var/log/ua_install.log | site-recovery 
/var/log/waagent.log | servicefabric 
/var/log/waagent\* | agents, diagnostic, eg, lad, normal, site-recovery, workloadbackup 
/var/log/waagent\*.log | monitor-mgmt 
/var/log/yum\* | diagnostic, eg, normal 
/var/opt/microsoft/omsagent/LAD/log/\* | lad 
/var/opt/microsoft/omsagent/\*/log/omsagent.log | monitor-mgmt 
/var/opt/microsoft/omsagent/\*/run/automationworker/omsupdatemgmt.log | monitor-mgmt 
/var/opt/microsoft/omsagent/run/automationworker/worker.log | monitor-mgmt 
/var/opt/microsoft/omsconfig/omsconfig.log | monitor-mgmt 
/var/opt/microsoft/omsconfig/omsconfigdetailed.log | monitor-mgmt 
/var/opt/microsoft/scx/log/scx.log | monitor-mgmt 
/var/opt/omi/log/\*.log | monitor-mgmt 
/var/spool/cron/tabs/root | workloadbackup 
## windows 
File Path | Manifest 
------------- | ------------- 
/$Windows.~BT/Sources/Panther/miglog.xml | windowsupdate 
/$Windows.~BT/Sources/Panther/setupact.log | windowsupdate 
/$Windows.~BT/Sources/Panther/setuperr.log | windowsupdate 
/AzureData/CustomData.bin | agents, diagnostic, eg, normal, windowsupdate 
/AzureData/CustomDataSetupScript.log | aks 
/AzureData/CustomDataSetupScript.ps1 | aks 
/Boot/BCD | windowsupdate 
/Packages/Plugins/ESET.FileSecurity/\*/agent_version.txt | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/ESET.FileSecurity/\*/extension_version.txt | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/AnalyzerConfigTempla<br>te.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Logs/\*DiagnosticsPl<br>ugin\*.log | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/StatusMonitor/Applic<br>ationInsightsPackagesVersion.json | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*.config | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/schema/wad\*.json | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/SeqNumber.txt | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Microsoft.WindowsAzure.Stora<br>ge.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/AsmExtensio<br>nMonitoringConfig\*.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/ASM.Azure.OSBaseline.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmExtensionSecurityPackStartupConfig.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScan.log | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScannerConfiguration.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/Azure.Common.scm.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityPackStartup.log | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityScanLoggerManifest.man | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/MonAgent-Pk<br>g-Manifest.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEvents.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEventsMin.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardExtensions.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AntiMalwareEvents.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEvents.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEventsCore.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsRootEvents.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents2.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents3.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents2.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents3.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentCertThumbprin<br>ts.txt | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentScheduledServ<br>ice.txt | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/InstallUtil.Inst<br>allLog | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/Infrastr<br>uctureManifest.template.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallLog | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallState | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/current.<br>config | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo.def.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/PluginManifest.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/config.bgi | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/emptyConfig.bgi | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCVersion.xml | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/HotfixInstallInProgress.dsc | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/PreInstallDone.dsc | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dpx | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dsc | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.log | agents, diagnostic, normal, windowsupdate 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/HandlerEnvironment.j<br>son | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/HandlerManifest.json | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/PackageDefinition.xm<br>l | agents, diagnostic, normal, sql-iaas, windowsupdate 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/RuntimeSettings/\*.s<br>ettings | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/Status/HeartBeat.Jso<br>n | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/Status/\*.status | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/config.txt | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/installation_log | sql-iaas 
/Packages/Plugins/\*/\*/HandlerEnvironment.json | agents, diagnostic, normal, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/HandlerManifest.json | agents, diagnostic, normal, servicefabric, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/PackageInformation.txt | agents, diagnostic, normal, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/RuntimeSettings/\*.settings | agents, diagnostic, normal, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/Status/HeartBeat.Json | agents, diagnostic, normal, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/Status/\*.status | agents, diagnostic, normal, servicefabric, windowsupdate 
/Packages/Plugins/\*/\*/config.txt | agents, diagnostic, normal, servicefabric, windowsupdate 
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
/Program Files/Microsoft Monitoring Agent/Agent/Health Service State/Management Packs<br>/\*.xml | monitor-mgmt 
/Program Files/Microsoft SQL Server/\*/MSSQL/Log/\*.\* | sql-iaas 
/ProgramData/ASRSetupLogs/ASRUnifiedAgentConfigurator.log | site-recovery, windowsupdate 
/ProgramData/ASRSetupLogs/ASRUnifiedAgentInstaller.log | site-recovery, windowsupdate 
/ProgramData/ASRSetupLogs/UnifiedAgentMSIInstall.log | site-recovery, windowsupdate 
/ProgramData/ASRSetupLogs/WrapperUnifiedAgent.log | site-recovery, windowsupdate 
/ProgramData/Microsoft/System Center/Orchestrator/7.2/SMA/\*.\* | monitor-mgmt 
/ProgramData/USOShared/Logs/\*.etl | windowsupdate 
/ProgramData/UsoPrivate/UpdateStore/\*.xml | windowsupdate 
/Users/\*/AppData/Local/Packages/WinStore_cw5n1h2txyewy/AC/Temp/winstore.log | windowsupdate 
/Users/\*/AppData/Local/Temp/winstore.log | windowsupdate 
/Users/\*/AppData/Local/microsoft/windows/windowsupdate.log | windowsupdate 
/Windows.old/ProgramData/USOPrivate/UpdateStore | windowsupdate 
/Windows.old/ProgramData/USOShared/Logs | windowsupdate 
/Windows.old/Windows/Logs/WindowsUpdate/\*.etl | windowsupdate 
/Windows.old/Windows/Logs/mosetup/bluebox.log | windowsupdate 
/Windows.old/Windows/SoftwareDistribution/ReportingEvents.log | windowsupdate 
/Windows/INF/netcfg\*.\*etl | diagnostic, windowsupdate 
/Windows/INF/setupapi.\*.log | windowsupdate 
/Windows/INF/setupapi.dev.log | diagnostic 
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
/Windows/Logs/mosetup/bluebox.log | windowsupdate 
/Windows/Logs/waasmedic/waasmedic.\*.etl | windowsupdate 
/Windows/Microsoft.NET/Framework/v4.0.30319/Config/machine.config | diagnostic, windowsupdate 
/Windows/Microsoft.NET/Framework64/v4.0.30319/Config/machine.config | diagnostic, windowsupdate 
/Windows/Minidump/\*.dmp | windowsupdate 
/Windows/Panther/FastCleanup/setupact.log | diagnostic, eg, normal, windowsupdate 
/Windows/Panther/UnattendGC/setupact.log | diagnostic, eg, normal, windowsupdate 
/Windows/Panther/WaSetup.log | diagnostic, eg, normal, windowsupdate 
/Windows/Panther/WaSetup.xml | agents, diagnostic, eg, genspec, normal, site-recovery, windowsupdate 
/Windows/Panther/miglog.xml | windowsupdate 
/Windows/Panther/setupact.log | diagnostic, eg, normal, windowsupdate 
/Windows/Panther/setuperr.log | diagnostic, eg, normal, windowsupdate 
/Windows/Panther/unattend.xml | diagnostic, eg, normal, windowsupdate 
/Windows/ServiceProfiles/LocalService/AppData/Local/Microsoft/WSLicense/tokens.dat | windowsupdate 
/Windows/ServiceProfiles/NetworkService/AppData/Local/Microsoft/Windows/DeliveryOptim<br>ization/Logs/\*.etl | windowsupdate 
/Windows/Setup/State/State.ini | diagnostic, eg, genspec, windowsupdate 
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
/Windows/System32/Sysprep/ActionFiles/Generalize.xml | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/ActionFiles/Respecialize.xml | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/ActionFiles/Specialize.xml | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/Panther/IE/setupact.log | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/Panther/IE/setuperr.log | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/Panther/setupact.log | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/Panther/setuperr.log | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Sysprep/Sysprep_succeeded.tag | diagnostic, eg, normal, windowsupdate 
/Windows/System32/Tasks/Microsoft/IaaSWorkloadBackup/\* | workloadbackup 
/Windows/System32/Winevt/Logs/Microsoft-WS-Licensing%%4Admin.evtx | windowsupdate 
/Windows/System32/Winevt/Logs/\*AppX\*.evtx | windowsupdate 
/Windows/System32/config/SOFTWARE | diagnostic, min-diagnostic, windowsupdate 
/Windows/System32/config/SOFTWARE.LOG1 | min-diagnostic 
/Windows/System32/config/SOFTWARE.LOG2 | min-diagnostic 
/Windows/System32/config/SYSTEM | diagnostic, min-diagnostic, windowsupdate 
/Windows/System32/config/SYSTEM.LOG1 | min-diagnostic 
/Windows/System32/config/SYSTEM.LOG2 | min-diagnostic 
/Windows/System32/winevt/Logs/Application.evtx | agents, aks, diagnostic, eg, min-diagnostic, normal, servicefabric, site-recovery, sql-iaas, windowsupdate, workloadbackup 
/Windows/System32/winevt/Logs/Microsoft-Automation%4Operational.evtx | monitor-mgmt 
/Windows/System32/winevt/Logs/Microsoft-SMA%4Debug.etl | monitor-mgmt 
/Windows/System32/winevt/Logs/Microsoft-SMA%4Operational.evtx | monitor-mgmt 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Admin.evtx | diagnostic, eg, normal, servicefabric, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Operational.evtx | diagnostic, eg, normal, servicefabric, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Admin.evtx | diagnostic, eg, normal, servicefabric, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Operational.evtx | diagnostic, eg, normal, servicefabric, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker%4BitLocker Management.evtx | diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker-DrivePreparationTool%4Opera<br>tional.evtx | diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Bits-Client%%4Operational.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-CAPI2%4Operational.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-DSC%4Operational.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-DeliveryOptimization%%4Operational.ev<br>tx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Admin.evtx | eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Operational.evtx | eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Host-Network-Service-Admin.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Host-Network-Service-Operational.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Hyper-V-Compute-Admin.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Hyper-V-Compute-Operational.evtx | aks 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%%4Configuration.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%4Configuration.evtx | agents, diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnPConfig%4Configuration.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NdisImPlatform%4Operational.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkLocationWizard%4Operational.ev<br>tx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProfile%4Operational.evtx | agents, diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProvider%4Operational.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-NlaSvc%4Operational.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Admi<br>n.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Oper<br>ational.evtx | diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RemoteDesktopSe<br>ssionManager%4Admin.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-SessionServices<br>%4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Resource-Exhaustion-Detector%4Operati<br>onal.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBClient%4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Connectivity.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-ServerManager%4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-SmbClient%4Connectivity.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Store%%4Operational.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TCPIP%4Operational.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TaskScheduler%%4Operational.evtx | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Admin.evtx | diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Admin.ev<br>tx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Operatio<br>nal.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RDPClient%4Operation<br>al.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Admin.evtx | diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Operational.evtx | diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Admin.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-UserPnp%4DeviceInstall.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4ConnectionSecurity.evtx | agents, diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4Firewall.evtx | agents, diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%%4Operational.evt<br>x | windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%4Operational.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Bootstrapper.evtx | agents, diagnostic, eg, monitor-mgmt, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4GuestAgent.evtx | agents, diagnostic, eg, monitor-mgmt, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Heartbeat.evtx | agents, diagnostic, eg, monitor-mgmt, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Runtime.evtx | agents, diagnostic, eg, monitor-mgmt, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4GuestAgent.evtx | agents, diagnostic, eg, monitor-mgmt, windowsupdate 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4Plugins.evtx | agents, diagnostic, eg, monitor-mgmt, windowsupdate 
/Windows/System32/winevt/Logs/MicrosoftAzureRecoveryServices-Replication.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/Security.evtx | diagnostic, eg, min-diagnostic, windowsupdate 
/Windows/System32/winevt/Logs/Setup.evtx | diagnostic, eg, windowsupdate 
/Windows/System32/winevt/Logs/System.evtx | agents, aks, diagnostic, eg, min-diagnostic, normal, servicefabric, site-recovery, sql-iaas, windowsupdate, workloadbackup 
/Windows/System32/winevt/Logs/Windows Azure.evtx | agents, diagnostic, eg, monitor-mgmt, normal, site-recovery, windowsupdate, workloadbackup 
/Windows/System32/winevt/Logs/Windows PowerShell.evtx | monitor-mgmt 
/Windows/Temp/MOMPerfCtrsInstall.log | monitor-mgmt 
/Windows/Temp/MonitoringAgent.log | monitor-mgmt 
/Windows/WinSxS/pending.xml | windowsupdate 
/Windows/WinSxS/poqexec.log | windowsupdate 
/Windows/WindowsUpdate.log | monitor-mgmt 
/Windows/debug/DCPROMO.LOG | diagnostic, eg, normal, windowsupdate 
/Windows/debug/NetSetup.LOG | diagnostic, eg, normal, windowsupdate 
/Windows/debug/PASSWD.LOG | diagnostic, eg, normal, windowsupdate 
/Windows/debug/dcpromoui.log | diagnostic, eg, normal, windowsupdate 
/Windows/debug/mrt.log | diagnostic, eg, normal, windowsupdate 
/Windows/debug/netlogon.log | diagnostic, eg, normal, windowsupdate 
/Windows/servicing/sessions/sessions.xml | diagnostic, windowsupdate 
/Windows/system32/winevt/Logs/Operations Manager.evtx | monitor-mgmt 
/Windows/windowsupdate\*.log | windowsupdate 
/WindowsAzure/GuestAgent\*/CommonAgentConfig.config | diagnostic, windowsupdate 
/WindowsAzure/Logs/AggregateStatus/\*.json | monitor-mgmt 
/WindowsAzure/Logs/AggregateStatus/aggregatestatus\*.json | agents, diagnostic, eg, min-diagnostic, normal, windowsupdate, workloadbackup 
/WindowsAzure/Logs/AppAgentRuntime.log | agents, diagnostic, eg, normal, windowsupdate, workloadbackup 
/WindowsAzure/Logs/MonitoringAgent.log | agents, diagnostic, eg, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>Plugin.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>PluginLauncher.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/Checkpoint.txt | agents, diagnostic, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MaConfig.xml | agents, diagnostic, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MonAgentHost.\*.log | agents, diagnostic, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.txt | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.txt | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/IaaSBcdrExt<br>ension\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.IaaSAntimalware/\*/AntimalwareCon<br>fig.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.Monitoring/\*/AsmExtension.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/FabricM<br>SIInstall\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Infrast<br>ructureManifest.xml | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/TempClu<br>sterManifest.xml | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/VCRunti<br>meInstall\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.CustomScriptExtension/\*/\*.log | diagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.JsonADDomainExtension/\*/ADDomainExtensi<br>on.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.VMAccessAgent/\*/JsonVMAccessExtension.l<br>og | agents, diagnostic, min-diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.EnterpriseCloud.Monitoring.MicrosoftMonitoringAg<br>ent/\*/0.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.ManagedIdentity.ManagedIdentityExtensionForWindo<br>ws/\*/RuntimeSettings/\*.xml | diagnostic, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DSCLOG\*.json | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DscExtensionHandler\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/CommandExec<br>ution\*.log | sql-iaas 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/ExtensionLo<br>g\*.log | sql-iaas 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/SqlCustomer<br>SupportLogs/\* | sql-iaas 
/WindowsAzure/Logs/Plugins/Symantec.SymantecEndpointProtection/\*/sepManagedAzure.txt | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/TrendMicro.DeepSecurity.TrendMicroDSA/\*/\*.log | agents, diagnostic, normal, windowsupdate 
/WindowsAzure/Logs/Plugins/\* | site-recovery, workloadbackup 
/WindowsAzure/Logs/Plugins/\*/\*/CommandExecution.log | agents, diagnostic, eg, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/\*/\*/Heartbeat.log | agents, diagnostic, eg, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/\*/\*/Install.log | agents, diagnostic, eg, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/Plugins/\*/\*/Update.log | agents, diagnostic, eg, normal, servicefabric, windowsupdate 
/WindowsAzure/Logs/SqlServerLogs/\*.\* | sql-iaas 
/WindowsAzure/Logs/Telemetry.log | agents, diagnostic, eg, normal, site-recovery, windowsupdate, workloadbackup 
/WindowsAzure/Logs/TransparentInstaller.log | agents, asc-vmhealth, diagnostic, eg, min-diagnostic, normal, site-recovery, windowsupdate, workloadbackup 
/WindowsAzure/Logs/VFPlugin/\*.log | monitor-mgmt 
/WindowsAzure/Logs/WaAppAgent.log | agents, diagnostic, eg, min-diagnostic, normal, site-recovery, windowsupdate, workloadbackup 
/WindowsAzure/Logs/\*.log | monitor-mgmt 
/WindowsAzure/Logs/plugins/\*/\*/\*.log | monitor-mgmt 
/WindowsAzure/config/\*.xml | agents, diagnostic, eg, normal, windowsupdate 
/WindowsUpdateVerbose.etl | windowsupdate 
/k/\*.err | aks 
/k/\*.log | aks 
/k/azure-vnet-ipam.json | aks 
/k/azure-vnet-ipam.log | aks 
/k/azure-vnet.json | aks 
/k/azure-vnet.log | aks 
/unattend.xml | diagnostic, eg, normal, windowsupdate 

*File was created by running [parse_manifest.py](../tools/parse_manifest.py) on `2019-06-18 15:47:22.119637`*
