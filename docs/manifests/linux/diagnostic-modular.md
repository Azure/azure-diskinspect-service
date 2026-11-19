# Linux Diagnostic Manifests - Modular Reference

This document provides an overview of modular Linux diagnostic manifests for the Azure Disk Inspect Service. For detailed documentation on each area, see the specific docs linked below.

## Documentation by Area

| Area | Document | Description |
|------|----------|-------------|
| Azure Agent | [diagnostic-azure-agent.md](diagnostic-azure-agent.md) | waagent, ProxyAgent, Managed Identity |
| Azure Extensions | [diagnostic-extensions.md](diagnostic-extensions.md) | Extension handler, AMA, LAD, SQL, etc. |
| Azure Files | [diagnostic-azure-files.md](diagnostic-azure-files.md) | Cloud-init, Blobfuse |
| Network | [diagnostic-network.md](diagnostic-network.md) | DHCP, DNS, SSH, Firewall, netconfig |
| System Config | [diagnostic-sysconfig.md](diagnostic-sysconfig.md) | fstab, PAM, sudoers, boot, kernel |
| System Logs | [diagnostic-syslogs.md](diagnostic-syslogs.md) | syslog, authlog, kernlog, sosreport |
| Packages | [diagnostic-packages.md](diagnostic-packages.md) | APT, YUM, Zypper, TDNF, repos |
| Kubernetes | [diagnostic-kubernetes.md](diagnostic-kubernetes.md) | kubelet, AKS, pods, CNI |
| HPC | [diagnostic-hpc.md](diagnostic-hpc.md) | InfiniBand, Slurm, PBS, NVIDIA |

## Naming Convention

**Format:** `diagnostic-<section>-<distro|common>`

- Section-first enables grouping by problem domain
- `-common` suffix = works on all distros
- `-<distro>` suffix = distro-specific (ubuntu, redhat, suse, mariner)
- AI selects based on issue type, then distro if needed

---

## Quick Reference - All Manifests

### Probing (Directory Listings)
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-probing-ubuntu` | Ubuntu/Debian | APT dirs, systemd | None |
| `diagnostic-probing-redhat` | RHEL/CentOS/Fedora | YUM repos, systemd | None |
| `diagnostic-probing-suse` | SLES/openSUSE | Zypp repos, systemd | None |
| `diagnostic-probing-mariner` | Azure Linux | TDNF, systemd | None |
| `diagnostic-probing-aks` | AKS nodes | pods, containers, k8s dirs | None |

### DHCP
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-dhcp-ubuntu` | Ubuntu/Debian | dhclient, dhcp, NM leases | Low |
| `diagnostic-dhcp-redhat` | RHEL/CentOS/Fedora | dhclient, NM leases | Low |
| `diagnostic-dhcp-suse` | SLES/openSUSE | Wicked, NM leases | Low |
| `diagnostic-dhcp-mariner` | Azure Linux | systemd-networkd, NM leases | Low |

### Network Configuration
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-netconfig-ubuntu` | Ubuntu/Debian | netplan, interfaces | None |
| `diagnostic-netconfig-redhat` | RHEL/CentOS/Fedora | sysconfig/network-scripts | None |
| `diagnostic-netconfig-suse` | SLES/openSUSE | wicked, sysconfig | None |
| `diagnostic-netconfig-mariner` | Azure Linux | systemd-networkd | None |
| `diagnostic-networking-aks` | AKS nodes | CNI, VNET, IPAM, CNS, NPM | None |

### NetworkManager
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-networkmanager-common` | All | NM config files | None |

### DNS/Name Resolution
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-dns-common` | All | resolv.conf, nsswitch, hosts | Low |

### SSH
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-ssh-common` | All | sshd_config, ssh_config | None |

### PAM (Pluggable Auth)
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-pam-common` | All | pam.d, limits.conf | Low |

### Firewall
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-firewall-ubuntu` | Ubuntu/Debian | UFW rules | None |
| `diagnostic-firewall-redhat` | RHEL/CentOS/Fedora | firewalld, iptables | None |
| `diagnostic-firewall-suse` | SLES/openSUSE | SuSEfirewall2, firewalld | None |
| `diagnostic-firewall-mariner` | Azure Linux | nftables, firewalld | None |

### Package Management Logs
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-packages-ubuntu` | Ubuntu/Debian | dpkg, APT logs | None |
| `diagnostic-packages-redhat` | RHEL/CentOS/Fedora | YUM, DNF, RHSM, RHUI | Low |
| `diagnostic-packages-suse` | SLES/openSUSE | Zypper logs | None |
| `diagnostic-packages-mariner` | Azure Linux | TDNF, DNF logs | None |

### Repository Configuration
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-repoconfig-ubuntu` | Ubuntu/Debian | sources.list | None |
| `diagnostic-repoconfig-redhat` | RHEL/CentOS/Fedora | yum.repos.d | None |
| `diagnostic-repoconfig-suse` | SLES/openSUSE | zypp repos | None |
| `diagnostic-repoconfig-mariner` | Azure Linux | tdnf repos | None |

### System Logs
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-syslog-common` | All | syslog, messages | Low |
| `diagnostic-authlog-common` | All | auth.log, secure, wtmp | **High** |
| `diagnostic-kernlog-common` | All | kern.log, dmesg | None |
| `diagnostic-bootlog-common` | All | boot.log | None |
| `diagnostic-clusterlog-common` | All | pacemaker, corosync | Low |
| `diagnostic-cloudregister-suse` | SLES/openSUSE | cloudregister log | None |

### System Configuration
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-fstab-common` | All | fstab, crypttab | None |
| `diagnostic-sudoers-common` | All | sudoers, sudoers.d | **Medium** |
| `diagnostic-sysctl-common` | All | sysctl.conf | None |
| `diagnostic-udev-common` | All | udev rules, modprobe | None |
| `diagnostic-release-common` | All | os-release, hostname | Low |
| `diagnostic-time-common` | All | chrony, ntp, timezone | None |
| `diagnostic-nfs-common` | All | NFS/idmapd config | None |

### Security (MAC)
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-security-ubuntu` | Ubuntu/Debian | AppArmor | None |
| `diagnostic-security-redhat` | RHEL/CentOS/Fedora | SELinux | None |
| `diagnostic-security-suse` | SLES/openSUSE | AppArmor | None |
| `diagnostic-security-mariner` | Azure Linux | SELinux | None |

### Boot Configuration
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-bootconfig-common` | All | GRUB config | None |

### Disk Info
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-diskinfo-common` | All | Partition layout | None |

### Kubernetes/Containers
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-kubernetes-common` | All | kubelet, containerd, pods | Medium |
| `diagnostic-kubernetes-aks` | AKS nodes | kubelet-status, containerd-status, journal | Medium |
| `diagnostic-provision-aks` | AKS nodes | cluster-provision, CSE output | Low |
| `diagnostic-pods-aks` | AKS nodes | kube-system, calico, tigera pods | Medium |

### HPC
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-hpc-common` | All | InfiniBand, Slurm, PBS | Medium |

### SOS/Support Reports
| Manifest | Scope | Description | PII |
|----------|-------|-------------|-----|
| `diagnostic-sosreport-common` | RHEL/Ubuntu | sosreport tarballs | **High** |
| `diagnostic-supportconfig-suse` | SLES/openSUSE | supportconfig tarballs | **High** |

---

## Selection by Issue Type

### SSH Access Issues
```
diagnostic-ssh-common
diagnostic-pam-common
diagnostic-authlog-common
diagnostic-firewall-<distro>
```

### DNS/Name Resolution Issues
```
diagnostic-dns-common
diagnostic-netconfig-<distro>
diagnostic-networkmanager-common
```

### Network Connectivity Issues
```
diagnostic-probing-<distro>
diagnostic-dhcp-<distro>
diagnostic-netconfig-<distro>
diagnostic-networkmanager-common
diagnostic-firewall-<distro>
```

### Boot/Startup Issues
```
diagnostic-bootconfig-common
diagnostic-bootlog-common
diagnostic-kernlog-common
diagnostic-fstab-common
diagnostic-diskinfo-common
```

### Kernel/Driver Issues
```
diagnostic-kernlog-common
diagnostic-udev-common
diagnostic-sysctl-common
```

### Package Installation Issues
```
diagnostic-packages-<distro>
diagnostic-repoconfig-<distro>
diagnostic-syslog-common
```

### Disk/Mount Issues
```
diagnostic-diskinfo-common
diagnostic-fstab-common
diagnostic-kernlog-common
diagnostic-syslog-common
```

### Authentication/Login Issues
```
diagnostic-authlog-common
diagnostic-pam-common
diagnostic-sudoers-common
diagnostic-ssh-common
```

### Firewall/Connectivity Blocked
```
diagnostic-firewall-<distro>
diagnostic-security-<distro>
diagnostic-syslog-common
```

### Time/NTP Issues
```
diagnostic-time-common
diagnostic-syslog-common
```

### Cluster (HA) Issues
```
diagnostic-clusterlog-common
diagnostic-fstab-common
diagnostic-netconfig-<distro>
```

### Kubernetes Issues
```
diagnostic-kubernetes-common
diagnostic-syslog-common
diagnostic-netconfig-<distro>
```

### AKS Issues
```
diagnostic-probing-aks
diagnostic-provision-aks
diagnostic-kubernetes-aks
diagnostic-pods-aks
diagnostic-networking-aks
```

### HPC/GPU Issues
```
diagnostic-hpc-common
diagnostic-kernlog-common
diagnostic-udev-common
```

---

## PII Risk Summary

| Risk Level | Manifests |
|------------|-----------|
| **High** | authlog-common, sosreport-common, supportconfig-suse |
| **Medium** | sudoers-common, kubernetes-common, hpc-common |
| **Low** | dns-common, dhcp-*, packages-redhat, syslog-common, release-common, pam-common, clusterlog-common |
| **None** | All others |

---

## Azure-Specific Manifests

See detailed docs: [diagnostic-azure-agent.md](diagnostic-azure-agent.md) | [diagnostic-extensions.md](diagnostic-extensions.md) | [diagnostic-azure-files.md](diagnostic-azure-files.md)

### Azure Agent
| Manifest | Description | PII |
|----------|-------------|-----|
| `diagnostic-azure-agent-probing` | Directory listings for waagent | None |
| `diagnostic-azure-agent-config` | waagent.conf | None |
| `diagnostic-azure-agent-logs` | waagent logs | Low |
| `diagnostic-azure-agent-state` | Agent state, status, incarnation | None |
| `diagnostic-azure-agent-xml` | SharedConfig, GoalState, ExtensionsConfig | Low |
| `diagnostic-azure-agent-identity` | ManagedIdentity JSON files | **Medium** |
| `diagnostic-azure-agent-proxyagent` | Guest ProxyAgent logs | Low |

### Azure Extensions
| Manifest | Description | PII |
|----------|-------------|-----|
| `diagnostic-extensions-probing` | Directory listings for extensions | None |
| `diagnostic-extensions-handler` | Handler config, state, status | Low |
| `diagnostic-extensions-logs` | Extension log files /var/log/azure | Low |
| `diagnostic-extensions-monitoring` | Azure Monitor Agent - AMA | Low |
| `diagnostic-extensions-lad` | Linux Diagnostic Extension | Low |
| `diagnostic-extensions-siterecovery` | Site Recovery Extension | Low |
| `diagnostic-extensions-sqliaas` | SQL IaaS Extension | Low |
| `diagnostic-extensions-workloadbackup` | Workload Backup - SAP HANA | Low |
| `diagnostic-extensions-servicefabric` | Service Fabric and Key Vault | Low |

### Azure Files
| Manifest | Description | PII |
|----------|-------------|-----|
| `diagnostic-cloudinit-common` | Cloud-init provisioning | Low |
| `diagnostic-blobfuse-common` | Blobfuse mount logs | None |

### Azure Agent Issues
```
diagnostic-azure-agent-probing
diagnostic-azure-agent-config
diagnostic-azure-agent-logs
diagnostic-azure-agent-state
diagnostic-azure-agent-xml
```

### Managed Identity Issues
```
diagnostic-azure-agent-identity
diagnostic-azure-agent-logs
diagnostic-azure-agent-state
```

### ProxyAgent Issues
```
diagnostic-azure-agent-proxyagent
diagnostic-azure-agent-logs
```

### Extension Handler Issues
```
diagnostic-extensions-probing
diagnostic-extensions-handler
diagnostic-extensions-logs
```

### Azure Monitor Agent Issues
```
diagnostic-extensions-monitoring
diagnostic-extensions-probing
diagnostic-extensions-logs
```

### Linux Diagnostic Extension Issues
```
diagnostic-extensions-lad
diagnostic-extensions-handler
diagnostic-extensions-logs
```

### Site Recovery Issues
```
diagnostic-extensions-siterecovery
diagnostic-extensions-handler
diagnostic-extensions-logs
```

### SQL IaaS Issues
```
diagnostic-extensions-sqliaas
diagnostic-extensions-handler
diagnostic-extensions-logs
```

### Workload Backup Issues
```
diagnostic-extensions-workloadbackup
diagnostic-extensions-handler
diagnostic-extensions-logs
```

### Service Fabric Issues
```
diagnostic-extensions-servicefabric
diagnostic-extensions-handler
diagnostic-extensions-logs
```

---

## Estimated Sizes

| Category | Size Range |
|----------|------------|
| Probing/Listings | < 100 KB |
| Config files | < 100 KB each |
| Package logs | 100 KB - 5 MB |
| System logs | 1 - 50 MB each |
| Auth logs | 1 - 20 MB |
| Kubernetes logs | 5 - 50 MB |
| SOS/Supportconfig | 10 - 500 MB |
