# Azure Disk Inspect: diagnostic-suse Manifest

This document describes the `diagnostic-suse` manifest used by the Azure Disk Inspect Service (IID/Ghostfish) to collect diagnostic files from SUSE Linux Enterprise Server (SLES) and openSUSE Azure VMs.

**Note:** For Azure Agent and extension issues, use the `azure-agent` and `azure-extensions` manifests alongside this one.

## Summary

| Section | File Count (Est.) | Size (Est.) | Notes |
|---------|-------------------|-------------|-------|
| Probing Directories | 14 listings | Minimal | Directory listings only |
| DHCP Files (Wicked) | 3-6 files | < 50 KB | Wicked and NM leases |
| Networking Files | 10-15 files | < 200 KB | ssh, hosts, pam |
| NetworkManager Files | 5-15 files | < 100 KB | NM configuration |
| Sysconfig Network | 10-15 files | < 200 KB | ifcfg, routes, SuSEfirewall2 |
| Wicked Network | 5-10 files | < 100 KB | Wicked XML config |
| Package Management | 2-5 files | 100 KB - 1 MB | zypper, zypp |
| System Log Files | 15-30 files | 10-100 MB | messages, secure, cloudregister |
| System Configuration | 15-25 files | < 500 KB | fstab, AppArmor, sudoers |
| Disk Info | 1 item | < 100 KB | Disk partition layout |

**Total Estimated Size:** 15-125 MB depending on log retention

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
| `/etc/zypp/repos.d` | Zypper repository configs | |
| `/usr/lib/systemd/system` | Vendor systemd units | |
| `/usr/lib/systemd/user` | Vendor user units | |

### 2. DHCP Files - Wicked (3-6 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/lib/wicked/lease*` | Wicked DHCP leases | |
| `/var/lib/NetworkManager/*.lease` | NetworkManager leases | |
| `/var/lib/NetworkManager/*.leases` | NM leases (alternate) | |

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

### 5. Sysconfig Network Files - SUSE (10-15 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/sysconfig/network` | Global network settings | |
| `/etc/sysconfig/network/ifcfg-*` | Interface configuration | |
| `/etc/sysconfig/network/routes` | Global static routes | |
| `/etc/sysconfig/network/ifroute-*` | Per-interface routes | |
| `/etc/sysconfig/SuSEfirewall2` | SuSEfirewall2 config | |
| `/etc/sysconfig/SuSEfirewall2.d/*` | SuSEfirewall2 includes | |

### 6. Wicked Network Files - SUSE (5-10 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/wicked/*.xml` | Wicked configuration | |
| `/etc/wicked/ifconfig/*.xml` | Wicked interface config | |

### 7. Package Management Log Files - SUSE (2-5 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/zypp/history` | Zypper transaction history | |
| `/var/log/zypper.log` | Zypper log | |

### 8. System Log Files (15-30 files)

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
| `/var/log/cloudregister` | SUSE cloud registration | |
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
| `/etc/HOSTNAME` | Hostname (SUSE style) | |
| `/etc/hostname` | Hostname (standard) | |
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
| `/sys/kernel/security/apparmor/profiles` | AppArmor profiles | |

### 10. Disk Info (1 item)

| Command | Purpose | X |
|---------|---------|---|
| `diskinfo,` | Disk partition info | |

---

## Legend

**X Column:** Items marked with X may contain sensitive or personally identifiable information (PII):
- Authentication logs with usernames
- Sudo user configurations
- Host-specific network information
- Encrypted volume information

---

## Potentially Missing Items

### Boot and Kernel
| Item | Path | Why It's Useful |
|------|------|-----------------|
| GRUB2 configuration | `/boot/grub2/grub.cfg`, `/etc/default/grub` | Boot parameter issues |
| Kernel crash dumps | `/var/crash/*` | Kernel panic analysis |
| mkinitrd logs | `/var/log/YaST2/mkinitrd.log` | initrd issues |

### Zypper/Package Management
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Zypper repos | `/etc/zypp/repos.d/*.repo` | Repository configuration |
| Zypper services | `/etc/zypp/services.d/*` | Repository services |
| RPM database | `/var/lib/rpm/*` (metadata) | Package integrity |
| SUSEConnect | `/etc/SUSEConnect` | Registration config |

### Wicked
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Wicked logs | `/var/log/wicked.log` | Network daemon logs |
| Wicked state | `/var/run/wicked/*` | Runtime state |

### AppArmor
| Item | Path | Why It's Useful |
|------|------|-----------------|
| AppArmor logs | `/var/log/audit/audit.log` | Policy denials |
| AppArmor profiles | `/etc/apparmor.d/*` | Profile definitions |
| aa-status output | `aa-status` | AppArmor state |

### Systemd
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Journal export | `journalctl` output | Comprehensive logs |
| Failed units | `systemctl --failed` | Service failures |
| Service overrides | `/etc/systemd/system/*.d/*.conf` | Custom settings |

### SUSE Cloud
| Item | Path | Why It's Useful |
|------|------|-----------------|
| registercloudguest | `/var/log/registercloudguest` | Cloud registration |
| SUSEConnect log | `/var/log/SUSEConnect.log` | Registration log |
| SMT/RMT config | `/etc/SUSEConnect` | Update server config |

### YaST
| Item | Path | Why It's Useful |
|------|------|-----------------|
| YaST logs | `/var/log/YaST2/*` | YaST operations |
| AutoYaST profile | `/root/autoinst.xml` | AutoYaST config |
