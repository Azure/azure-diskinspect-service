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
/etc/fstab | diagnostic, eg, normal 
/etc/hostname | agents, diagnostic, eg, genspec, lad, site-recovery, workloadbackup 
/etc/network/interfaces | diagnostic, eg 
/etc/network/interfaces.d/\*.cfg | diagnostic, eg 
/etc/nsswitch.conf | diagnostic 
/etc/opt/microsoft/omsagent/LAD/conf/omsagent.d/\* | lad 
/etc/opt/microsoft/omsagent/\*/conf/omsagent.d/\*.conf | monitor-mgmt 
/etc/opt/microsoft/omsagent/conf/omsagent.conf | monitor-mgmt 
/etc/opt/omi/conf/omsconfig/agentid | monitor-mgmt 
/etc/opt/omi/conf/omsconfig/configuration/\*.mof | monitor-mgmt 
/etc/resolv.conf | diagnostic, eg 
/etc/ssh/sshd_config | diagnostic, normal 
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
/tmp/omsagent\*.tgz | monitor-mgmt 
/var/lib/dhclient/dhclient-eth0.leases | diagnostic, eg 
/var/lib/dhcp/dhclient.eth0.leases | diagnostic, eg 
/var/lib/waagent/ExtensionsConfig.\*.xml | diagnostic, lad 
/var/lib/waagent/GoalState.\*.xml | diagnostic, site-recovery, workloadbackup 
/var/lib/waagent/HostingEnvironmentConfig.xml | diagnostic 
/var/lib/waagent/Incarnation | agents, diagnostic 
/var/lib/waagent/ManagedIdentity-\*.json | diagnostic 
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
/var/lib/wicked/lease-eth0-dhcp-ipv4.xml | diagnostic, eg 
/var/log/AzureRcmCli.log | site-recovery 
/var/log/auth\* | agents, diagnostic, eg, normal 
/var/log/azure/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode/\*.\*/CommandExec<br>ution.log | servicefabric 
/var/log/azure/Microsoft.EnterpriseCloud.Monitoring.OmsAgentForLinux/\*/\*.log | monitor-mgmt 
/var/log/azure/Microsoft.OSTCExtensions.LinuxDiagnostic/\*/mdsd.\* | servicefabric 
/var/log/azure/Microsoft.\*LinuxDiagnostic/\*/\* | lad 
/var/log/azure/\* | site-recovery, workloadbackup 
/var/log/azure/\*/\*/\* | agents, diagnostic 
/var/log/azure/custom-script/handler.log | agents, diagnostic 
/var/log/boot\* | diagnostic, eg, normal 
/var/log/cloud-init\* | diagnostic, eg, normal 
/var/log/dmesg\* | agents, diagnostic, eg, normal, site-recovery, workloadbackup 
/var/log/dpkg\* | diagnostic, eg, normal 
/var/log/evtcollforw\*.log | site-recovery 
/var/log/kern\* | diagnostic, eg, normal 
/var/log/messages\* | diagnostic, eg, monitor-mgmt, normal 
/var/log/rsyslog\* | diagnostic, eg, lad, normal 
/var/log/s2\*.log | site-recovery 
/var/log/sa/sar\* | performance 
/var/log/secure\* | diagnostic, eg, normal 
/var/log/sfnode/sfnodelog | servicefabric 
/var/log/svagents\*.log | site-recovery 
/var/log/syslog | servicefabric 
/var/log/syslog\* | agents, diagnostic, eg, lad, monitor-mgmt, normal, site-recovery, workloadbackup 
/var/log/ua_install.log | site-recovery 
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
/var/opt/msawb/catalog/InquiryCatalog/\*/\*.bin | workloadbackup 
/var/opt/msawb/catalog/SyncObjectsCatalog/AlertEventsTable/\*.bin | workloadbackup 
/var/opt/msawb/catalog/SyncObjectsCatalog/DatasourceSyncTable/\*.bin | workloadbackup 
/var/opt/msawb/catalog/WorkloadExtDatasourceCatalog/\*/\*.bin | workloadbackup 
/var/opt/msawb/catalog/WorkloadSchedules/\*/\*.bin | workloadbackup 
/var/opt/msawb/catalogRegisteredObjectInfoCatalog/\*/\*.bin | workloadbackup 
/var/opt/omi/log/\*.log | monitor-mgmt 
/var/spool/cron/tabs/root | workloadbackup 
## windows 
File Path | Manifest 
------------- | ------------- 
/AzureData/CustomData.bin | agents, diagnostic, eg, normal 
/Packages/Plugins/ESET.FileSecurity/\*/agent_version.txt | agents, diagnostic, normal 
/Packages/Plugins/ESET.FileSecurity/\*/extension_version.txt | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/AnalyzerConfigTempla<br>te.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Logs/\*DiagnosticsPl<br>ugin\*.log | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/StatusMonitor/Applic<br>ationInsightsPackagesVersion.json | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*.config | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/schema/wad\*.json | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/SeqNumber.txt | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Microsoft.WindowsAzure.Stora<br>ge.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/AsmExtensio<br>nMonitoringConfig\*.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/ASM.Azure.OSBaseline.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmExtensionSecurityPackStartupConfig.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScan.log | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScannerConfiguration.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/Azure.Common.scm.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityPackStartup.log | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityScanLoggerManifest.man | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/MonAgent-Pk<br>g-Manifest.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEvents.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEventsMin.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardExtensions.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AntiMalwareEvents.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEvents.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEventsCore.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsRootEvents.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents2.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents3.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents2.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents3.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentCertThumbprin<br>ts.txt | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentScheduledServ<br>ice.txt | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/InstallUtil.Inst<br>allLog | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/Infrastr<br>uctureManifest.template.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallLog | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallState | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/current.<br>config | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo.def.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/PluginManifest.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/config.bgi | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Compute.BGInfo/\*/emptyConfig.bgi | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCVersion.xml | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/HotfixInstallInProgress.dsc | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/PreInstallDone.dsc | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dpx | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dsc | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.log | agents, diagnostic, normal 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/HandlerEnvironment.j<br>son | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/HandlerManifest.json | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/PackageDefinition.xm<br>l | agents, diagnostic, normal, sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/RuntimeSettings/\*.s<br>ettings | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/Status/HeartBeat.Jso<br>n | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/Status/\*.status | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/config.txt | sql-iaas 
/Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/installation_log | sql-iaas 
/Packages/Plugins/\*/\*/HandlerEnvironment.json | agents, diagnostic, normal, servicefabric 
/Packages/Plugins/\*/\*/HandlerManifest.json | agents, diagnostic, normal, servicefabric, servicefabric 
/Packages/Plugins/\*/\*/PackageInformation.txt | agents, diagnostic, normal, servicefabric 
/Packages/Plugins/\*/\*/RuntimeSettings/\*.settings | agents, diagnostic, normal, servicefabric 
/Packages/Plugins/\*/\*/Status/HeartBeat.Json | agents, diagnostic, normal, servicefabric 
/Packages/Plugins/\*/\*/Status/\*.status | agents, diagnostic, normal, servicefabric 
/Packages/Plugins/\*/\*/config.txt | agents, diagnostic, normal, servicefabric 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/AzureRcmCli.log | site-recovery 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/evtcollforw\*.log | site-recovery 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/s2\*.log | site-recovery 
/Program Files (x86)/Microsoft Azure Site Recovery/agent/svagents\*.log | site-recovery 
/Program Files/Azure Workload Backup/Catalog/InquiryCatalog/\*/\*.bin | workloadbackup 
/Program Files/Azure Workload Backup/Catalog/RegisteredObjectInfoCatalog/\*/\*.bin | workloadbackup 
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
/ProgramData/ASRSetupLogs/ASRUnifiedAgentConfigurator.log | site-recovery 
/ProgramData/ASRSetupLogs/ASRUnifiedAgentInstaller.log | site-recovery 
/ProgramData/ASRSetupLogs/UnifiedAgentMSIInstall.log | site-recovery 
/ProgramData/ASRSetupLogs/WrapperUnifiedAgent.log | site-recovery 
/ProgramData/Microsoft/System Center/Orchestrator/7.2/SMA/\*.\* | monitor-mgmt 
/Windows/Inf/netcfg\*.\*etl | diagnostic, normal 
/Windows/Inf/setupapi.dev.log | diagnostic, normal 
/Windows/Microsoft.NET/Framework/v4.0.30319/Config/machine.config | diagnostic 
/Windows/Microsoft.NET/Framework64/v4.0.30319/Config/machine.config | diagnostic 
/Windows/Panther/FastCleanup/setupact.log | diagnostic, eg, normal 
/Windows/Panther/UnattendGC/setupact.log | diagnostic, eg, normal 
/Windows/Panther/WaSetup.log | diagnostic, eg, normal 
/Windows/Panther/WaSetup.xml | agents, diagnostic, eg, genspec, normal, site-recovery 
/Windows/Panther/setupact.log | diagnostic, eg, normal 
/Windows/Panther/setuperr.log | diagnostic, eg, normal 
/Windows/Panther/unattend.xml | diagnostic, eg, normal 
/Windows/Setup/State/State.ini | diagnostic, eg, genspec 
/Windows/Setup/State/state.ini | agents, normal 
/Windows/SoftwareDistribution/ReportingEvents.log | monitor-mgmt 
/Windows/System32/Sysprep/ActionFiles/Generalize.xml | diagnostic, eg, normal 
/Windows/System32/Sysprep/ActionFiles/Respecialize.xml | diagnostic, eg, normal 
/Windows/System32/Sysprep/ActionFiles/Specialize.xml | diagnostic, eg, normal 
/Windows/System32/Sysprep/Panther/IE/setupact.log | diagnostic, eg, normal 
/Windows/System32/Sysprep/Panther/IE/setuperr.log | diagnostic, eg, normal 
/Windows/System32/Sysprep/Panther/setupact.log | diagnostic, eg, normal 
/Windows/System32/Sysprep/Panther/setuperr.log | diagnostic, eg, normal 
/Windows/System32/Sysprep/Sysprep_succeeded.tag | diagnostic, eg, normal 
/Windows/System32/Tasks/Microsoft/IaaSWorkloadBackup/\* | workloadbackup 
/Windows/System32/Winevt/Logs/Microsoft-Automation%4Operational.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-SMA%4Debug.etl | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-SMA%4Operational.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Bootstrapper.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4GuestAgent.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Heartbeat.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Runtime.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-WindowsAzure-Status%4GuestAgent.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Microsoft-WindowsAzure-Status%4Plugins.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Windows Azure.evtx | monitor-mgmt 
/Windows/System32/Winevt/Logs/Windows PowerShell.evtx | monitor-mgmt 
/Windows/System32/config/SOFTWARE | diagnostic, min-diagnostic 
/Windows/System32/config/SOFTWARE.LOG1 | min-diagnostic 
/Windows/System32/config/SOFTWARE.LOG2 | min-diagnostic 
/Windows/System32/config/SYSTEM | diagnostic, min-diagnostic 
/Windows/System32/config/SYSTEM.LOG1 | min-diagnostic 
/Windows/System32/config/SYSTEM.LOG2 | min-diagnostic 
/Windows/System32/winevt/Logs/Application.evtx | agents, diagnostic, eg, normal, servicefabric, site-recovery, sql-iaas, workloadbackup 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Admin.evtx | diagnostic, eg, normal, servicefabric 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Operational.evtx | diagnostic, eg, normal, servicefabric 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Admin.evtx | diagnostic, eg, normal, servicefabric 
/Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Operational.evtx | diagnostic, eg, normal, servicefabric 
/Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker%4BitLocker Management.evtx | diagnostic 
/Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker-DrivePreparationTool%4Opera<br>tional.evtx | diagnostic 
/Windows/System32/winevt/Logs/Microsoft-Windows-CAPI2%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-DSC%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Admin.evtx | eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Operational.evtx | eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%4Configuration.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnPConfig%4Configuration.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-NdisImPlatform%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkLocationWizard%4Operational.ev<br>tx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProfile%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProvider%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-NlaSvc%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Admi<br>n.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Oper<br>ational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RemoteDesktopSe<br>ssionManager%4Admin.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-SessionServices<br>%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Resource-Exhaustion-Detector%4Operati<br>onal.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBClient%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Connectivity.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-ServerManager%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-SmbClient%4Connectivity.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TCPIP%4Operational.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Admin.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Admin.ev<br>tx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Operatio<br>nal.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RDPClient%4Operation<br>al.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Admin.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Admin.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-UserPnp%4DeviceInstall.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4ConnectionSecurity.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4Firewall.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%4Operational.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Bootstrapper.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4GuestAgent.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Heartbeat.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Runtime.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4GuestAgent.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4Plugins.evtx | agents, diagnostic, eg 
/Windows/System32/winevt/Logs/MicrosoftAzureRecoveryServices-Replication.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Security.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/Setup.evtx | diagnostic, eg 
/Windows/System32/winevt/Logs/System.evtx | agents, diagnostic, eg, normal, servicefabric, site-recovery, sql-iaas, workloadbackup 
/Windows/System32/winevt/Logs/Windows Azure.evtx | agents, diagnostic, eg, normal, site-recovery, workloadbackup 
/Windows/WindowsUpdate.log | monitor-mgmt 
/Windows/debug/DCPROMO.LOG | diagnostic, eg, normal 
/Windows/debug/NetSetup.LOG | diagnostic, eg, normal 
/Windows/debug/PASSWD.LOG | diagnostic, eg, normal 
/Windows/debug/dcpromoui.log | diagnostic, eg, normal 
/Windows/debug/mrt.log | diagnostic, eg, normal 
/Windows/debug/netlogon.log | diagnostic, eg, normal 
/Windows/logs/OpsMgrTrace/\*.\* | monitor-mgmt 
/Windows/logs/WindowsUpdate/WindowsUpdate.\*.etl | monitor-mgmt 
/Windows/system32/winevt/logs/Operations Manager.evtx | monitor-mgmt 
/Windows/temp/MOMPerfCtrsInstall.log | monitor-mgmt 
/Windows/temp/MonitoringAgent.log | monitor-mgmt 
/WindowsAzure/GuestAgent\*/CommonAgentConfig.config | diagnostic 
/WindowsAzure/Logs/AggregateStatus/\*.json | monitor-mgmt 
/WindowsAzure/Logs/AggregateStatus/aggregatestatus\*.json | agents, diagnostic, eg, normal, workloadbackup 
/WindowsAzure/Logs/AppAgentRuntime.log | agents, diagnostic, eg, normal, workloadbackup 
/WindowsAzure/Logs/MonitoringAgent.log | agents, diagnostic, eg, normal, servicefabric 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>Plugin.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>PluginLauncher.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/Checkpoint.txt | agents, diagnostic, normal, servicefabric 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MaConfig.xml | agents, diagnostic, normal, servicefabric 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MonAgentHost.\*.log | agents, diagnostic, normal, servicefabric 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.txt | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.txt | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/IaaSBcdrExt<br>ension\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.IaaSAntimalware/\*/AntimalwareCon<br>fig.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.Monitoring/\*/AsmExtension.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/FabricM<br>SIInstall\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Infrast<br>ructureManifest.xml | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/TempClu<br>sterManifest.xml | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/VCRunti<br>meInstall\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.CustomScriptExtension/\*/\*.log | diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.JsonADDomainExtension/\*/ADDomainExtensi<br>on.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Compute.VMAccessAgent/\*/JsonVMAccessExtension.l<br>og | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.EnterpriseCloud.Monitoring.MicrosoftMonitoringAg<br>ent/\*/0.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.ManagedIdentity.ManagedIdentityExtensionForWindo<br>ws/\*/RuntimeSettings/\*.xml | diagnostic 
/WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DSCLOG\*.json | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DscExtensionHandler\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/CommandExec<br>ution\*.log | sql-iaas 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/ExtensionLo<br>g\*.log | sql-iaas 
/WindowsAzure/Logs/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/SqlCustomer<br>SupportLogs/\* | sql-iaas 
/WindowsAzure/Logs/Plugins/Symantec.SymantecEndpointProtection/\*/sepManagedAzure.txt | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/TrendMicro.DeepSecurity.TrendMicroDSA/\*/\*.log | agents, diagnostic, normal 
/WindowsAzure/Logs/Plugins/\* | site-recovery, workloadbackup 
/WindowsAzure/Logs/Plugins/\*/\*/CommandExecution.log | agents, diagnostic, eg, normal, servicefabric 
/WindowsAzure/Logs/Plugins/\*/\*/Heartbeat.log | agents, diagnostic, eg, normal, servicefabric 
/WindowsAzure/Logs/Plugins/\*/\*/Install.log | agents, diagnostic, eg, normal, servicefabric 
/WindowsAzure/Logs/Plugins/\*/\*/Update.log | agents, diagnostic, eg, normal, servicefabric 
/WindowsAzure/Logs/SqlServerLogs/\*.\* | sql-iaas 
/WindowsAzure/Logs/Telemetry.log | agents, diagnostic, eg, normal, site-recovery, workloadbackup 
/WindowsAzure/Logs/TransparentInstaller.log | agents, asc-vmhealth, diagnostic, eg, min-diagnostic, normal, site-recovery, workloadbackup 
/WindowsAzure/Logs/VFPlugin/\*.log | monitor-mgmt 
/WindowsAzure/Logs/WaAppAgent.log | agents, diagnostic, eg, normal, site-recovery, workloadbackup 
/WindowsAzure/Logs/\*.log | monitor-mgmt 
/WindowsAzure/config/\*.xml | agents, diagnostic, eg, normal 
/WindowsAzure/logs/plugins/\*/\*/\*.log | monitor-mgmt 
/unattend.xml | diagnostic, eg, normal 

*File was created by running [parse_manifest.py](../tools/parse_manifest.py) on `2018-10-24 17:44:24.104910`*