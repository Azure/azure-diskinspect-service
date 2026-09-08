# Azure Disk Inspect: diagnostic-mariner Manifest

This document describes the `diagnostic-mariner` manifest used by the Azure Disk Inspect Service (IID/Ghostfish) to collect diagnostic files from Azure Linux (CBL-Mariner) VMs.

**Note:** For Azure Agent and extension issues, use the `azure-agent` and `azure-extensions` manifests alongside this one.

## Summary

| Section | File Count (Est.) | Size (Est.) | Notes |
|---------|-------------------|-------------|-------|
| Probing Directories | 15 listings | Minimal | Directory listings only |
| DHCP Files | 3-6 files | < 50 KB | NM and systemd-networkd leases |
| Networking Files | 10-15 files | < 200 KB | ssh, hosts, pam |
| NetworkManager Files | 5-15 files | < 100 KB | NM configuration |
| systemd-networkd Files | 5-10 files | < 100 KB | Network unit files |
| Firewall Files | 3-10 files | < 100 KB | iptables, nftables, firewalld |
| Package Management (TDNF) | 5-15 files | 100 KB - 1 MB | TDNF/DNF logs |
| System Log Files | 15-30 files | 10-100 MB | messages, secure, kern |
| System Configuration | 15-25 files | < 500 KB | fstab, SELinux, sudoers |
| Disk Info | 1 item | < 100 KB | Disk partition layout |
| Kubernetes/Container | 10-50 files | 5-50 MB | kubelet, containerd, pods |

**Total Estimated Size:** 20-175 MB depending on log retention and AKS workloads

---

## Section Details

### 1. Probing Directories (15 items)

| Path | Purpose | X |
|------|---------|---|
| `/boot` | Kernel and boot files | |
| `/var/log` | Log directory structure | |
| `/var/lib/cloud` | Cloud-init state | |
| `/var/lib/waagent` | Azure Agent state | |
| `/etc` | Configuration overview | |
| `/etc/udev/rules.d` | Device rules | |
| `/etc/alternatives` | System alternatives | |
| `/etc/systemd/system` | Custom systemd units | |
| `/etc/systemd/system/multi-user.target.wants` | Multi-user services | |
| `/etc/systemd/system/graphical.target.wants` | Graphical services | |
| `/etc/systemd/user` | User systemd units | |
| `/etc/yum.repos.d` | YUM repository configs (compat) | |
| `/etc/tdnf` | TDNF configuration | |
| `/usr/lib/systemd/system` | Vendor systemd units | |
| `/usr/lib/systemd/user` | Vendor user units | |

### 2. DHCP Files - Mariner (3-6 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/lib/NetworkManager/*.lease` | NetworkManager leases | |
| `/var/lib/NetworkManager/*.leases` | NM leases (alternate) | |
| `/run/systemd/netif/leases/*` | systemd-networkd leases | |

### 3. Networking Files (10-15 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/dhcp/*.conf` | DHCP client config | |
| `/etc/ssh/sshd_config` | SSH daemon config | |
| `/etc/ssh/sshd_config.d/*` | SSH config includes | |
| `/etc/nsswitch.conf` | Name service switch | |
| `/etc/resolv.conf` | DNS resolver config | |
| `/etc/hosts` | Static host mappings | X |
| `/etc/hosts.allow` | TCP wrappers allow | |
| `/etc/hosts.deny` | TCP wrappers deny | |
| `/etc/pam.d/*` | PAM configuration | X |

### 4. NetworkManager Files (5-15 files)

| Path | Purpose | X |
|------|---------|---|
| `/usr/lib/NetworkManager/*.conf` | Vendor NM config | |
| `/usr/lib/NetworkManager/conf.d/*.conf` | Vendor NM includes | |
| `/etc/NetworkManager/*.conf` | System NM config | |
| `/etc/NetworkManager/conf.d/*.conf` | System NM includes | |
| `/var/lib/NetworkManager/*.conf` | Runtime NM config | |
| `/var/lib/NetworkManager/conf.d/*.conf` | Runtime NM includes | |
| `/var/lib/NetworkManager/*.state` | NM state files | |

### 5. systemd-networkd Files - Mariner (5-10 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/systemd/network/*.network` | Network unit files | |
| `/etc/systemd/network/*.netdev` | Network device files | |
| `/etc/systemd/network/*.link` | Link configuration | |
| `/run/systemd/network/*.network` | Runtime network config | |
| `/usr/lib/systemd/network/*.network` | Vendor network config | |

### 6. Firewall Files - Mariner (3-10 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/sysconfig/iptables` | iptables rules | |
| `/etc/nftables.conf` | nftables configuration | |
| `/etc/firewalld/*.xml` | firewalld config | |
| `/etc/firewalld/zones/*.xml` | firewalld zones | |

### 7. Package Management Log Files - TDNF (5-15 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/tdnf*` | TDNF package manager logs | |
| `/var/log/dnf*` | DNF logs (if installed) | |
| `/var/log/yum*` | YUM logs (compatibility) | |
| `/var/cache/tdnf/history/*` | TDNF transaction history | |

### 8. System Log Files (15-30 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/messages*` | System messages | |
| `/var/log/syslog*` | Syslog (fallback) | |
| `/var/log/rsyslog*` | Rsyslog output | |
| `/var/log/kern*` | Kernel messages | |
| `/var/log/dmesg*` | Boot ring buffer | |
| `/var/log/boot*` | Boot logs | |
| `/var/log/auth*` | Authentication log | X |
| `/var/log/secure*` | Secure log | X |
| `/var/log/pacemaker*` | Pacemaker cluster | |
| `/var/log/corosync*` | Corosync cluster | |
| `/var/log/cluster/*` | Cluster logs | |
| `/var/log/pacemaker/*` | Pacemaker directory | |
| `/var/log/corosync/*` | Corosync directory | |

### 9. System Configuration Files (15-25 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/fstab` | Filesystem mounts | |
| `/etc/crypttab` | Encrypted volumes | X |
| `/etc/*-release` | OS release info | |
| `/etc/mariner-release` | Mariner version | |
| `/etc/HOSTNAME` | Hostname (legacy) | |
| `/etc/hostname` | Hostname | |
| `/etc/localtime` | Timezone symlink | |
| `/etc/chrony/chrony.conf` | Chrony NTP config | |
| `/etc/chrony.conf` | Chrony config (alt path) | |
| `/etc/idmapd.conf` | NFSv4 ID mapping | |
| `/etc/sudoers` | Sudo configuration | X |
| `/etc/sudoers.d/*` | Sudo includes | X |
| `/etc/sysctl.conf` | Kernel parameters | |
| `/etc/sysctl.d/*.conf` | Sysctl includes | |
| `/etc/udev/rules.d/*.rules` | Device rules | |
| `/etc/modprobe.d/*.conf` | Kernel module config | |
| `/etc/security/limits.conf` | Resource limits | |
| `/etc/selinux/config` | SELinux configuration | |

### 10. Disk Info (1 item)

| Command | Purpose | X |
|---------|---------|---|
| `diskinfo,` | Disk partition info | |

### 11. Kubernetes/Container Files - Mariner (10-50 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/pods/*/*/*.log` | Pod logs | |
| `/var/log/containers/*.log` | Container logs | |
| `/etc/kubernetes/*.conf` | Kubernetes configs | |
| `/etc/kubernetes/*.yaml` | Kubernetes YAML configs | |
| `/var/lib/kubelet/config.yaml` | Kubelet configuration | |
| `/var/log/kubelet.log` | Kubelet logs | |
| `/etc/containerd/config.toml` | Containerd config | |
| `/var/log/containerd.log` | Containerd logs | |

---

## Legend

**X Column:** Items marked with X may contain sensitive or personally identifiable information (PII):
- Authentication logs with usernames
- Sudo user configurations
- Host-specific network information
- Encrypted volume information

---

## Azure Linux (CBL-Mariner) Characteristics

| Characteristic | Details |
|----------------|---------|
| Package Manager | TDNF (Tiny DNF) |
| Security Framework | SELinux |
| Network Manager | NetworkManager or systemd-networkd |
| Init System | systemd |
| Package Format | RPM |
| Primary Use Case | AKS nodes, container workloads |

---

## Potentially Missing Items

### Boot and Kernel
| Item | Path | Why It's Useful |
|------|------|-----------------|
| GRUB configuration | `/boot/grub2/grub.cfg`, `/etc/default/grub` | Boot parameter issues |
| Kernel crash dumps | `/var/crash/*` | Kernel panic analysis |
| dracut logs | `/var/log/dracut.log` | initramfs issues |

### TDNF/Package Management
| Item | Path | Why It's Useful |
|------|------|-----------------|
| TDNF configuration | `/etc/tdnf/tdnf.conf` | Package manager settings |
| TDNF repos | `/etc/yum.repos.d/*.repo` | Repository definitions |
| GPG keys | `/etc/pki/rpm-gpg/*` | Package signing |

### SELinux
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Audit log | `/var/log/audit/audit.log` | SELinux denials |
| SELinux booleans | `getsebool -a` output | Policy tuning |
| SELinux status | `sestatus` output | SELinux state |

### Systemd
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Journal export | `journalctl` output | Comprehensive logs |
| Failed units | `systemctl --failed` | Service failures |
| networkctl status | `networkctl` output | systemd-networkd state |

### Kubernetes/AKS
| Item | Path | Why It's Useful |
|------|------|-----------------|
| CNI configuration | `/etc/cni/net.d/*` | Container networking |
| Azure CNI logs | `/var/log/azure-cni*.log` | Azure CNI issues |
| kube-proxy logs | `/var/log/kube-proxy.log` | Service proxy issues |
| crictl info | `crictl info` output | Container runtime state |

### Azure/Cloud
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Azure Arc agent | `/var/lib/GuestConfig/*` | Arc diagnostics |
| Azure Monitor Agent | `/var/opt/microsoft/azuremonitoragent/*` | AMA diagnostics |
| Accelerated Networking | `/var/log/azure/Microsoft.Azure.Networking.LinuxAgent/*` | AN driver issues |
