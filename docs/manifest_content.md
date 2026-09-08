This file documents the various files collected, or directory listed or registry key queried by disk inspection manifests used by Microsoft Azure support.  Any data collected by Microsoft using this tooling is done according to the policy outlined in the [Azure Trust Center](https://azure.microsoft.com/en-us/support/trust-center/).

* [windows](#windows)
## windows 
 Manifest | Operation | File Path 
 ------------- | ------------- | ------------- 
diagnostic-arc | copy | /Program Files/AzureConnectedMachineAgent/Log/himds.log
diagnostic-arc | copy | /Program Files/AzureConnectedMachineAgent/Log/azcmagent.log
diagnostic-arc | copy | /Program Files/GuestConfig/arc_policy_logs/gc_agent.log
diagnostic-arc | copy | /Program Files/GuestConfig/ext_mgr_logs/gc_ext.log
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/AgentInstall.txt
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/GenevaInstall.txt
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/MsRdcWebRTCSvc.txt
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/MsRdcWebRTCSvcMsiInstall.txt
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/MsRdcWebRTCSvcMsiUninstall.txt
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/SXSStackInstall.txt
diagnostic-avd-rdinfra | copy | /Program Files/Microsoft RDInfra/WVDAgentManagerInstall.txt
diagnostic-avd-rdinfra | copy | /Program Files/MsRDCMMRHost/MsRDCMMRHostInstall.log
diagnostic-avd-rdinfra | copy | /Windows/Temp/MsRDCMMRHostInstall.log
diagnostic-avd-rdinfra | copy | /Windows/Logs/RDMSDeploymentUI.txt
diagnostic-avd-rdinfra | copy | /Windows/web/rdweb/App_Data/rdweb.log
diagnostic-avd-rdinfra | list | /Windows/RemotePackages
diagnostic-avd-rdinfra | list | /Program Files/Microsoft RDInfra
diagnostic-blobfuse | copy | /var/log/blobfuse2.log
diagnostic-blobfuse | copy | /var/log/blobfuse2.log\*
diagnostic-diskinfo | diskinfo | 
diagnostic-domainjoin | copy | /Windows/debug/netlogon.log
diagnostic-domainjoin | copy | /Windows/debug/NetSetup.LOG
diagnostic-domainjoin | copy | /Windows/debug/mrt.log
diagnostic-domainjoin | copy | /Windows/debug/DCPROMO.LOG
diagnostic-domainjoin | copy | /Windows/debug/dcpromoui.log
diagnostic-domainjoin | copy | /Windows/debug/PASSWD.LOG
diagnostic-dotnet | copy | /Windows/Microsoft.NET/Framework/v4.0.30319/Config/machine.config
diagnostic-dotnet | copy | /Windows/Microsoft.NET/Framework64/v4.0.30319/Config/machine.config
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Admin.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-ServiceFabric%4Operational.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Operational.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-ServiceFabric-Lease%4Admin.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4GuestAgent.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Heartbeat.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Runtime.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Diagnostics%4Bootstrapper.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4GuestAgent.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/Microsoft-WindowsAzure-Status%4Plugins.evtx
diagnostic-events-azure | copy | /Windows/System32/winevt/Logs/MicrosoftAzureRecoveryServices-Replication.evtx
diagnostic-events-core | copy | /Windows/System32/winevt/Logs/System.evtx
diagnostic-events-core | copy | /Windows/System32/winevt/Logs/Application.evtx
diagnostic-events-core | copy | /Windows/System32/winevt/Logs/Windows Azure.evtx
diagnostic-events-core | copy | /Windows/System32/winevt/Logs/Security.evtx
diagnostic-events-core | copy | /Windows/System32/winevt/Logs/Setup.evtx
diagnostic-events-directory-services | copy | /Windows/System32/winevt/Logs/Active Directory Web Services.evtx
diagnostic-events-directory-services | copy | /Windows/System32/winevt/Logs/DFS Replication.evtx
diagnostic-events-directory-services | copy | /Windows/System32/winevt/Logs/DNS Server.evtx
diagnostic-events-directory-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-DNSServer%4Audit.evtx
diagnostic-events-directory-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-DNS-Client%4Operational.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Directory Service.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-GroupPolicy%4Operational.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AAD%4Operational.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-HelloForBusiness%4Operational.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-User Device Registration%4Admin.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Workplace Join%4Admin.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Kerberos-KDCProxy%4Operational.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmartCard-Audit%4Authentication.evtx
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmartCard-DeviceEnum%4Operational.evt<br>x
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmartCard-TPM-VCard-Module%4Admin.evt<br>x
diagnostic-events-identity | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmartCard-TPM-VCard-Module%4Operation<br>al.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-CAPI2%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-CodeIntegrity%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-NdisImPlatform%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-NetworkLocationWizard%4Operational.ev<br>tx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProfile%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-NetworkProvider%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-NTLM%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-schannel%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmbClient%4Connectivity.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmbClient%4Security.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SMBClient%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Connectivity.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SmbServer%4Security.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-SMBServer%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4ConnectionSecurity.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Windows Firewall With Advanced Securi<br>ty%4Firewall.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/OpenSSH%4Admin.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/OpenSSH%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-NlaSvc%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TCPIP%4Operational.evtx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-WinINet-Config%4ProxyConfigChanged.ev<br>tx
diagnostic-events-network-security | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-WinRM%4Operational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Oper<br>ational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Admi<br>n.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RemoteDesktopSe<br>ssionManager%4Admin.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-SessionServices<br>%4Operational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Admin.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Operational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Operatio<br>nal.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-PnPDevices%4Admin.ev<br>tx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RDPClient%4Operation<br>al.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Operational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-RemoteConnectionMana<br>ger%4Admin.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Operational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Admin.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/RemoteDesktopServices.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreCDV%4Adm<br>in.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteDesktopServices-RdpCoreCDV%4Ope<br>rational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-TSV-VmHostAgent%4Adm<br>in.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-TSV-VmHostAgent%4Ope<br>rational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteAssistance%4Admin.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteAssistance%4Operational.evtx
diagnostic-events-rdp | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-RemoteHelp%4Operational.evtx
diagnostic-events-storage | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Ntfs%4Operational.evtx
diagnostic-events-storage | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-VHDMP%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker%4BitLocker Management.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-BitLocker-DrivePreparationTool%4Opera<br>tional.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-DSC%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnPConfig%4Configuration.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%4Configuration.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Resource-Exhaustion-Detector%4Operati<br>onal.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-ServerManager%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-UserPnp%4DeviceInstall.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-User Profile Service%4Operational.evt<br>x
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%4Device Configuration.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Kernel-PnP%4Device Management.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppLocker%4EXE and DLL.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppLocker%4Packaged app-Execution.evt<br>x
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppLocker%4Packaged app-Deployment.ev<br>tx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppLocker%4MSI and Script.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppModel-Runtime%4Admin.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppReadiness%4Admin.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppReadiness%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppXDeployment%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppXDeploymentServer%4Operational.evt<br>x
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppXDeploymentServer%4Restricted.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-AppxPackaging%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Diagnostics-Performance%4Operational.<br>evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-PowerShell%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Shell-Core%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TaskScheduler%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-WER-Diagnostics%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-Winlogon%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-WMI-Activity%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-DeviceManagement-Enterprise-Diagnosti<br>cs-Provider%4Sync.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-DeviceManagement-Enterprise-Diagnosti<br>cs-Provider%4Enrollment.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-DeviceManagement-Enterprise-Diagnosti<br>cs-Provider%4Admin.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/PowerShellCore%4Operational.evtx
diagnostic-events-system-services | copy | /Windows/System32/winevt/Logs/icrosoft-Windows-AppxPackaging%4Operational.evtx
diagnostic-extensions-aadlogin | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ActiveDirectory.AADLoginForWindows/\*/\*.l<br>og
diagnostic-extensions-aadlogin | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ActiveDirectory.AADLoginForWindows/\*/\*.t<br>xt
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>Plugin.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Diagnostics<br>PluginLauncher.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.KeyVault.KeyVaultForWindows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.IaaSAntimalware/\*/AntimalwareCon<br>fig.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.Monitoring/\*/AsmExtension.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Compute.JsonADDomainExtension/\*/ADDomainExtensi<br>on.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Compute.VMAccessAgent/\*/JsonVMAccessExtension.l<br>og
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.EnterpriseCloud.Monitoring.MicrosoftMonitoringAg<br>ent/\*/0.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DSCLOG\*.json
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Powershell.DSC/\*/DscExtensionHandler\*.log
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/AnalyzerConfigTempla<br>te.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*.config
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/Logs/\*DiagnosticsPl<br>ugin\*.log
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/schema/wad\*.json
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/StatusMonitor/Applic<br>ationInsightsPackagesVersion.json
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.RecoveryServices.VMSnapshot/\*/SeqNumber.txt
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Microsoft.WindowsAzure.Stora<br>ge.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/AsmExtensio<br>nMonitoringConfig\*.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/ASM.Azure.OSBaseline.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmExtensionSecurityPackStartupConfig.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScan.log
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/AsmScannerConfiguration.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/Azure.Common.scm.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityPackStartup.log
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/Extensions/<br>AzureSecurityPack/SecurityScanLoggerManifest.man
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEvents.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardEventsMin.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AgentStandardExtensions.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/AntiMalwareEvents.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEvents.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsEventsCore.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringEwsRootEvents.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents2.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/MonitoringStandardEvents3.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents2.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/initconfig/<br>\*/Standard/SecurityStandardEvents3.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/Monitoring/agent/MonAgent-Pk<br>g-Manifest.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentCertThumbprin<br>ts.txt
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Azure.Security.Monitoring/\*/MonitoringAgentScheduledServ<br>ice.txt
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Compute.BGInfo/\*/BGInfo.def.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Compute.BGInfo/\*/PluginManifest.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Compute.BGInfo/\*/config.bgi
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Compute.BGInfo/\*/emptyConfig.bgi
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dsc
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.log
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/\*.dpx
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCVersion.xml
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/HotfixInstallInProgress.dsc
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.Powershell.DSC/\*/DSCWork/PreInstallDone.dsc
diagnostic-extensions-azure | copy | /Packages/Plugins/Microsoft.SqlServer.Management.SqlIaaSAgent/\*/PackageDefinition.xm<br>l
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.ManagedServices.ApplicationHealthWindows/\*/\*.l<br>og
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.txt
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.Edp.NetworkWatcherAgentWind<br>ows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.txt
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.NetworkWatcher.NetworkWatcherAgentWindows/<br>\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Compute.CustomScriptExtension/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.RunCommandWindows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.RunCommandHandlerWindows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Security.AzureDiskEncryption/\*/BitlockerE<br>xtension.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/log_\*
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.HpcCompute.NvidiaGpuDriverWindows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.HpcCompute.AmdGpuDriverMicrosoft/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/\*<br>.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/lo<br>g_\*
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.Core.WindowsPatchExtension/\*/windowsUpdat<br>eLog/\*
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.ProxyAgent.ProxyAgentWindowsTest/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.ProxyAgent.ProxyAgentWindows/\*/\*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.ProxyAgent.ProxyAgentWindowsARM64Test/\*/\<br>*.log
diagnostic-extensions-azure | copy | /WindowsAzure/Logs/Plugins/Microsoft.CPlat.ProxyAgent.ProxyAgentWindowsARM64/\*/\*.lo<br>g
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/\*/\*/CommandExecution\*.log
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/\*/\*/Install.log
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/\*/\*/Update.log
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/\*/\*/Heartbeat.log
diagnostic-extensions-core | copy | /Packages/Plugins/\*/\*/config.txt
diagnostic-extensions-core | copy | /Packages/Plugins/\*/\*/HandlerEnvironment.json
diagnostic-extensions-core | copy | /Packages/Plugins/\*/\*/HandlerManifest.json
diagnostic-extensions-core | copy | /Packages/Plugins/\*/\*/Status/HeartBeat.Json
diagnostic-extensions-core | copy | /Packages/Plugins/\*/\*/PackageInformation.txt
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/Checkpoint.txt
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MaConfig.xml
diagnostic-extensions-core | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.Diagnostics.IaaSDiagnostics/\*/\*/Configur<br>ation/MonAgentHost.\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.ServiceFabricMCNode/\*/\*<br>.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.ServiceFabricMCNode/Event<br>s/sfmcnodeagent_Temp/Raw/sfmcnodeagent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.Test.ServiceFabricMCNode-<br>Test/\*/\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.Test.ServiceFabricMCNode-<br>Test/Events/sfmcnodeagent_Temp/Raw/sfmcnodeagent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.SfmcSetup/\*/\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.SfmcSetup/Events/sfmcsetu<br>pextagent_Temp/Raw/sfmcsetupextagent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.Test.SfmcSetup-Test/\*/\*<br>.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.MC.Test.SfmcSetup-Test/Event<br>s/sfmcsetupextagent_Temp/Raw/sfmcsetupextagent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Infrast<br>ructureManifest.xml
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/TempClu<br>sterManifest.xml
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/Events/Boo<br>tstrapAgent_Temp/Raw/BootstrapAgent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/Events/Upg<br>radeAgent_Temp/Raw/UpgradeAgent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.Test.ServiceFabricNode/\*/In<br>frastructureManifest.xml
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.Test.ServiceFabricNode/\*/Te<br>mpClusterManifest.xml
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.Test.ServiceFabricNode/\*/\*<br>.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.Test.ServiceFabricNode/Event<br>s/BootstrapAgent_Temp/Raw/BootstrapAgent\*.log
diagnostic-extensions-servicefabric | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ServiceFabric.Test.ServiceFabricNode/Event<br>s/UpgradeAgent_Temp/Raw/UpgradeAgent\*.log
diagnostic-extensions-servicefabric | copy | /Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/InstallUtil.Inst<br>allLog
diagnostic-extensions-servicefabric | copy | /Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/current.<br>config
diagnostic-extensions-servicefabric | copy | /Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/Infrastr<br>uctureManifest.template.xml
diagnostic-extensions-servicefabric | copy | /Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallLog
diagnostic-extensions-servicefabric | copy | /Packages/Plugins/Microsoft.Azure.ServiceFabric.ServiceFabricNode/\*/Service/ServiceF<br>abricNodeBootstrapAgent.InstallState
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/\*/\*/RuntimeSettings/\*.settings
diagnostic-extensions-thirdparty | copy | /WindowsAzure/Logs/Plugins/Symantec.SymantecEndpointProtection/\*/sepManagedAzure.txt
diagnostic-extensions-thirdparty | copy | /WindowsAzure/Logs/Plugins/TrendMicro.DeepSecurity.TrendMicroDSA/\*/\*.log
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/ESET.FileSecurity/\*/agent_version.txt
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/ESET.FileSecurity/\*/extension_version.txt
diagnostic-extensions-thirdparty | copy | /WindowsAzure/Logs/Plugins/Microsoft.ManagedIdentity.ManagedIdentityExtensionForWindo<br>ws/\*/RuntimeSettings/\*.xml
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/RuntimeSettings<br>/applicationRegistry.active
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/RuntimeSettings<br>/applicationRegistry.backup
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/Microsoft.CPlat.Core.VMApplicationManagerWindows/\*/RuntimeSettings<br>/VMApp.lockfile
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/RuntimeSett<br>ings/applicationRegistry.active
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/RuntimeSett<br>ings/applicationRegistry.backup
diagnostic-extensions-thirdparty | copy | /Packages/Plugins/Microsoft.CPlat.Core.EDP.VMApplicationManagerWindows/\*/RuntimeSett<br>ings/VMApp.lockfile
diagnostic-fslogix | copy | /ProgramData/FSLogix/Logs/Profile/Profile_\*.log
diagnostic-fslogix | copy | /ProgramData/FSLogix/Logs/\*.etl.\*
diagnostic-fslogix | list | /ProgramData/FSLogix/Logs
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-FSLogic-Apps%4Admin.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-FSLogic-Apps%4Operational.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-FSLogic-CloudCache%4Admin.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-FSLogic-CloudCache%4Operational.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-FSLogix-Apps%4Admin.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-FSLogix-Apps%4Operational.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-FSLogix-CloudCache%4Admin.evtx
diagnostic-fslogix | copy | /Windows/System32/winevt/Logs/Microsoft-FSLogix-CloudCache%4Operational.evtx
diagnostic-fslogix | copy | /Program Files/FSLogix/Logs/Profile_\*.log
diagnostic-fslogix | copy | /Program Files/FSLogix/Apps/Rules
diagnostic-fslogix | list | /Program Files/FSLogix/Apps/Rules
diagnostic-fslogix | list | /Program Files/FSLogix/Apps/CompiledRules
diagnostic-guest-agent-core | list | /WindowsAzure
diagnostic-guest-agent-core | list | /Packages/Plugins
diagnostic-guest-agent-core | copy | /WindowsAzure/Logs/Telemetry.log
diagnostic-guest-agent-core | copy | /WindowsAzure/Logs/TransparentInstaller.log
diagnostic-guest-agent-core | copy | /WindowsAzure/Logs/WaAppAgent.log
diagnostic-guest-agent-core | copy | /WindowsAzure/config/\*.xml
diagnostic-guest-agent-core | copy | /WindowsAzure/Logs/AggregateStatus/aggregatestatus\*.json
diagnostic-guest-agent-core | copy | /WindowsAzure/Logs/AppAgentRuntime.log
diagnostic-guest-agent-core | copy | /WindowsAzure/Logs/MonitoringAgent.log
diagnostic-guest-agent-core | copy | /WindowsAzure/GuestAgent\*/CommonAgentConfig.config
diagnostic-hpc | copy | /Windows/System32/winevt/Logs/Microsoft HPC Pack.evtx
diagnostic-hpc | copy | /Windows/System32/winevt/Logs/Microsoft-HPC-Management%4Admin.evtx
diagnostic-hpc | copy | /Windows/System32/winevt/Logs/Microsoft-HPC-Reporting%4Operational.evtx
diagnostic-hpc | copy | /Windows/System32/winevt/Logs/Microsoft-HPC-Scheduler%4Operational.evtx
diagnostic-hpc | copy | /Windows/System32/winevt/Logs/Microsoft-HPC-Scheduler%4Admin.evtx
diagnostic-hpc | copy | /Program Files/NVIDIA Corporation/Installer2/\*
diagnostic-hpc | copy | /Windows/Temp/HPCSetupLogs/\*
diagnostic-hpc | copy | /Windows/Temp/HPCSetupLogs/\*/\*
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/Scheduler
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/Diagnostics
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/HpcFrontend
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/HpcNaming
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/Management
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/Monitoring
diagnostic-hpc-pack-2016 | list | /Program Files/Microsoft HPC Pack 2016/Data/LogFiles/SOA
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/Scheduler/
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/Diagnostics/
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/HpcFrontend/
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/HpcNaming/
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/Management/
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/Monitoring/
diagnostic-hpc-pack-2019 | list | /Program Files/Microsoft HPC Pack 2019/Data/LogFiles/SOA/
diagnostic-misc | copy | /Windows/Temp/ScriptLog.log
diagnostic-misc | list | /Windows/System32/IME
diagnostic-misc | list | /Windows/IME
diagnostic-msrdcollect | copy | /Windows/System32/tssesdir/\*.xml
diagnostic-pnp-appinstall | copy | /Windows/INF/netcfg\*.\*etl
diagnostic-pnp-appinstall | copy | /Windows/INF/setupapi.\*
diagnostic-pnp-appinstall | copy | /Windows/inf/setupapi.app.log
diagnostic-provisioning | list | /AzureData/CustomData.bin
diagnostic-provisioning | copy | /Windows/Setup/State/State.ini
diagnostic-provisioning | copy | /Windows/Panther/WaSetup.xml
diagnostic-provisioning | copy | /Windows/Panther/WaSetup.log
diagnostic-provisioning | copy | /Windows/Panther/VmAgentInstaller.xml
diagnostic-provisioning | copy | /Windows/Panther/unattend.xml
diagnostic-provisioning | copy | /windows/Panther/setup.etl
diagnostic-provisioning | copy | /unattend.xml
diagnostic-provisioning | copy | /Windows/Panther/setupact.log
diagnostic-provisioning | copy | /Windows/Panther/setuperr.log
diagnostic-provisioning | copy | /Windows/Panther/UnattendGC/setupact.log
diagnostic-provisioning | copy | /Windows/Panther/FastCleanup/setupact.log
diagnostic-provisioning | copy | /Windows/System32/Sysprep/ActionFiles/Generalize.xml
diagnostic-provisioning | copy | /Windows/System32/Sysprep/ActionFiles/Specialize.xml
diagnostic-provisioning | copy | /Windows/System32/Sysprep/ActionFiles/Respecialize.xml
diagnostic-provisioning | copy | /Windows/System32/Sysprep/Panther/setupact.log
diagnostic-provisioning | copy | /Windows/System32/Sysprep/Panther/IE/setupact.log
diagnostic-provisioning | copy | /Windows/System32/Sysprep/Panther/setuperr.log
diagnostic-provisioning | copy | /Windows/System32/Sysprep/Panther/IE/setuperr.log
diagnostic-provisioning | copy | /Windows/System32/Sysprep/Sysprep_succeeded.tag
diagnostic-proxyagent | copy | /WindowsAzure/ProxyAgent/Logs/\*
diagnostic-proxyagent | copy | /Windows/Logs/eBPF/committed/\*
diagnostic-registry-core | copy | /Windows/System32/config/SOFTWARE
diagnostic-registry-core | copy | /Windows/System32/config/SYSTEM
diagnostic-registry-core | copy | /Windows/System32/config/SYSTEM.LOG1
diagnostic-registry-core | copy | /Windows/System32/config/SYSTEM.LOG2
diagnostic-registry-core | copy | /Windows/System32/config/SOFTWARE.LOG1
diagnostic-registry-core | copy | /Windows/System32/config/SOFTWARE.LOG2
diagnostic-wga-gap-closure | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-LocalSessionManager%<br>4Operational.evtx
diagnostic-wga-gap-closure | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-TerminalServices-SessionBroker-Client<br>%4Operational.evtx
diagnostic-wga-gap-closure | copy | /Windows/Panther/WaSetup.xml
diagnostic-wga-gap-closure | copy | /Windows/Panther/VmAgentInstaller.xml
diagnostic-wga-gap-closure | copy | /Windows/Panther/setupact.log
diagnostic-wga-gap-closure | copy | /Windows/Panther/setuperr.log
diagnostic-wga-gap-closure | copy | /WindowsAzure/Logs/Plugins/\*/\*/CommandExecution\*.log
diagnostic-wga-gap-closure | copy | /WindowsAzure/Logs/Plugins/Microsoft.Azure.ActiveDirectory.AADLoginForWindows/\*/Comm<br>andExecution\*.log
diagnostic-wga-gap-closure | copy | /Windows/Panther/scanresults.xml
diagnostic-wga-gap-closure | copy | /Windows/Panther/msiexec.log
diagnostic-wga-gap-closure | copy | /Windows/System32/drivers/CrowdStrike/C-00000291\*.sys
diagnostic-windows-update | copy | /Windows/servicing/sessions/sessions.xml
diagnostic-windows-update | copy | /Windows/Logs/CBS/\*.log
diagnostic-windows-update | copy | /Windows/Logs/DISM/\*.log
diagnostic-windows-update | copy | /Windows/windowsupdate\*.log
diagnostic-windows-update | copy | /Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%4Operational.evtx

*File was created by running [parse_manifest.py](../tools/parse_manifest.py) on `2026-09-08 22:01:37.587378`*