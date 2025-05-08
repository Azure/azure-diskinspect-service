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
/etc/apt/sources.list.d/\*.sources | linux-repoconfig 
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
/etc/sysconfig/network/config | eg, vmdiagnostic 
/etc/sysconfig/network/dhcp | eg, vmdiagnostic 
/etc/sysconfig/network/ifcfg-\* | eg, vmdiagnostic 
/etc/sysconfig/network/routes | eg, vmdiagnostic 
/etc/sysctl.conf | diagnostic 
/etc/sysctl.d/\*.conf | diagnostic 
/etc/syslog-ng/\* | azuremonitoragent 
/etc/udev/rules.d/\*.rules | diagnostic 
/etc/ufw/ufw.conf | diagnostic, eg, vmdiagnostic 
/etc/ufw/user.rules | diagnostic 
/etc/ufw/user6.rules | diagnostic 
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
/var/lib/waagent/Microsoft.Azure.KeyVault.KeyVaultForLinux-\*/config/\* | servicefabric 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/\* | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/\*.settings | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/metrics_con<br>figs/\*Configuration.json | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/telegraf_co<br>nfigs/telegraf.conf | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/config/telegraf_co<br>nfigs/telegraf.d/\* | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent-\*/status/\*.status | azuremonitoragent 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*.\*/Handler<br>Environment.json | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*.\*/status/<br>\*.status | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/HandlerMan<br>ifest.json | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/Service/cu<br>rrent.config | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/ServiceFab<br>ricLinuxExtension_install.log | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/WindowsFab<br>ricLinuxExtension_enable.log | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/background<br>_installer.log | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/config/\*.<br>settings | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/dotnet-uni<br>nstall-log-\*.log | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/heartbeat.<br>log | servicefabric 
/var/lib/waagent/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode-\*/sfbootstra<br>pagentdebdownload.log | servicefabric 
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
/var/log/azure-cni\* | aks 
/var/log/azure-cns\* | aks 
/var/log/azure-ipam\* | aks 
/var/log/azure-npm.log | aks 
/var/log/azure-proxy-agent/\* | agents, diagnostic, normal 
/var/log/azure-vnet\* | aks 
/var/log/azure/Microsoft.AKS.Compute.AKS.Linux.AKSNode/extension.log | aks 
/var/log/azure/Microsoft.Azure.KeyVault.KeyVaultForLinux/\* | servicefabric 
/var/log/azure/Microsoft.Azure.Monitor.AzureMonitorLinuxAgent/\*/\*.log | azuremonitoragent 
/var/log/azure/Microsoft.Azure.ServiceFabric.ServiceFabricLinuxNode/events/\* | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/CommandExecutio<br>n\*.log | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/InfrastructureM<br>anifest.xml | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/ServiceFabricLi<br>nuxExtension.log | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/TempClusterMani<br>fest.xml | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/extension.log | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/handler.log | servicefabric 
/var/log/azure/Microsoft.Azure.ServiceFabric.\*ServiceFabricLinuxNode/sfbootstrapagen<br>t\*.log | servicefabric 
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
/var/log/journal/\*/\* | aks, vmdiagnostic 
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
