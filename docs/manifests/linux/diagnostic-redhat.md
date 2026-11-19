# Azure Disk Inspect: diagnostic-redhat Manifest

This document describes the `diagnostic-redhat` manifest used by the Azure Disk Inspect Service (IID/Ghostfish) to collect diagnostic files from RHEL, CentOS, Fedora, and other Red Hat-based Azure VMs.

**Note:** For Azure Agent and extension issues, use the `azure-agent` and `azure-extensions` manifests alongside this one.

## Summary

| Section | File Count (Est.) | Size (Est.) | Notes |
|---------|-------------------|-------------|-------|
| Probing Directories | 14 listings | Minimal | Directory listings only |
| DHCP Files | 4-8 files | < 50 KB | NetworkManager/dhclient leases |
| Networking Files | 10-15 files | < 200 KB | ssh, hosts, pam |
| NetworkManager Files | 5-15 files | < 100 KB | NM configuration |
| Sysconfig Network | 10-20 files | < 200 KB | ifcfg, routes, firewalld |
| Package Management | 10-30 files | 500 KB - 5 MB | yum, dnf, rhsm |
| System Log Files | 15-30 files | 10-100 MB | messages, secure, kern |
| System Configuration | 15-30 files | < 500 KB | fstab, SELinux, sudoers |
| Disk Info | 1 item | < 100 KB | Disk partition layout |
| RHUI | 2-5 files | < 1 MB | Red Hat Update Infrastructure |

**Total Estimated Size:** 15-130 MB depending on log retention

---

## Section Details

### 1. Probing Directories (14 items)

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
| `/etc/yum.repos.d` | YUM/DNF repository configs | |
| `/usr/lib/systemd/system` | Vendor systemd units | |
| `/usr/lib/systemd/user` | Vendor user units | |

### 2. DHCP Files (4-8 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/lib/NetworkManager/*.lease` | NetworkManager leases | |
| `/var/lib/NetworkManager/*.leases` | NM leases (alternate) | |
| `/var/lib/dhclient/*.lease` | dhclient leases | |
| `/var/lib/dhclient/*.leases` | dhclient leases (alternate) | |

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

### 5. Sysconfig Network Files (10-20 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/sysconfig/network` | Global network settings | |
| `/etc/sysconfig/network-scripts/ifcfg-*` | Interface configuration | |
| `/etc/sysconfig/network-scripts/route-*` | Static routes | |
| `/etc/sysconfig/iptables` | iptables rules | |
| `/etc/firewalld/*.xml` | firewalld config | |
| `/etc/firewalld/zones/*.xml` | firewalld zones | |

### 6. Package Management Log Files (10-30 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/yum*` | YUM package logs | |
| `/var/log/dnf*` | DNF package logs | |
| `/var/log/rhsm/*` | Red Hat Subscription Manager | X |

### 7. System Log Files (15-30 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/messages*` | System messages | |
| `/var/log/syslog*` | Syslog (fallback) | |
| `/var/log/rsyslog*` | Rsyslog output | |
| `/var/log/kern*` | Kernel messages | |
| `/var/log/dmesg*` | Boot ring buffer | |
| `/var/log/boot*` | Boot logs | |
| `/var/log/auth*` | Authentication log (fallback) | X |
| `/var/log/secure*` | Secure log | X |
| `/var/log/pacemaker*` | Pacemaker cluster | |
| `/var/log/corosync*` | Corosync cluster | |
| `/var/log/cluster/*` | Cluster logs | |
| `/var/log/pacemaker/*` | Pacemaker directory | |
| `/var/log/corosync/*` | Corosync directory | |

### 8. System Configuration Files (15-30 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/fstab` | Filesystem mounts | |
| `/etc/crypttab` | Encrypted volumes | X |
| `/etc/*-release` | OS release info | |
| `/etc/HOSTNAME` | Hostname (legacy) | |
| `/etc/hostname` | Hostname | |
| `/etc/localtime` | Timezone symlink | |
| `/etc/chrony/chrony.conf` | Chrony NTP config | |
| `/etc/idmapd.conf` | NFSv4 ID mapping | |
| `/etc/sudoers` | Sudo configuration | X |
| `/etc/sudoers.d/*` | Sudo includes | X |
| `/etc/sysctl.conf` | Kernel parameters | |
| `/etc/sysctl.d/*.conf` | Sysctl includes | |
| `/etc/udev/rules.d/*.rules` | Device rules | |
| `/etc/modprobe.d/*.conf` | Kernel module config | |
| `/etc/security/limits.conf` | Resource limits | |
| `/etc/selinux/config` | SELinux configuration | |
| `/etc/sysconfig/selinux` | SELinux sysconfig | |

### 9. Disk Info (1 item)

| Command | Purpose | X |
|---------|---------|---|
| `diskinfo,` | Disk partition info | |

### 10. Red Hat Update Infrastructure (2-5 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/rhuicheck.log` | RHUI health check | |
| `/var/log/rhui/*` | RHUI logs | |

---

## Legend

**X Column:** Items marked with X may contain sensitive or personally identifiable information (PII):
- Authentication logs with usernames
- Subscription/entitlement information
- Sudo user configurations
- Encrypted volume information

---

## Potentially Missing Items

### Boot and Kernel
| Item | Path | Why It's Useful |
|------|------|-----------------|
| GRUB2 configuration | `/boot/grub2/grub.cfg`, `/etc/default/grub` | Boot parameter issues |
| Kernel crash dumps | `/var/crash/*` | Kernel panic analysis |
| dracut logs | `/var/log/dracut.log` | initramfs issues |

### YUM/DNF
| Item | Path | Why It's Useful |
|------|------|-----------------|
| YUM repo files | `/etc/yum.repos.d/*.repo` | Repository configuration |
| DNF modules | `/etc/dnf/modules.d/*` | Module streams |
| RPM database | `/var/lib/rpm/*` (metadata) | Package integrity |

### SELinux
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Audit log | `/var/log/audit/audit.log` | SELinux denials |
| SELinux booleans | `getsebool -a` output | Policy tuning |
| SELinux contexts | `/etc/selinux/*/contexts/*` | Context configuration |

### Systemd
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Journal export | `journalctl` output | Comprehensive logs |
| Failed units | `systemctl --failed` | Service failures |
| Service overrides | `/etc/systemd/system/*.d/*.conf` | Custom settings |

### Network
| Item | Path | Why It's Useful |
|------|------|-----------------|
| nmcli output | `nmcli connection show` | Connection details |
| firewall-cmd output | `firewall-cmd --list-all` | Active firewall rules |
| Network scripts (RHEL 8+) | `/etc/NetworkManager/system-connections/*` | NM keyfiles |

### Subscription
| Item | Path | Why It's Useful |
|------|------|-----------------|
| RHSM identity | `/etc/pki/consumer/cert.pem` | Subscription cert |
| RHSM config | `/etc/rhsm/rhsm.conf` | Subscription settings |
| Entitlements | `/etc/pki/entitlement/*` | Product entitlements |
