# Azure Disk Inspect: diagnostic-ubuntu Manifest

This document describes the `diagnostic-ubuntu` manifest used by the Azure Disk Inspect Service (IID/Ghostfish) to collect diagnostic files from Ubuntu and Debian-based Azure VMs.

**Note:** For Azure Agent and extension issues, use the `azure-agent` and `azure-extensions` manifests alongside this one.

## Summary

| Section | File Count (Est.) | Size (Est.) | Notes |
|---------|-------------------|-------------|-------|
| Probing Directories | 15 listings | Minimal | Directory listings only |
| DHCP/Dhclient Files | 5-10 files | < 50 KB | DHCP leases |
| Networking Files | 15-25 files | < 500 KB | netplan, ufw, ssh, hosts |
| NetworkManager Files | 5-15 files | < 100 KB | NM configuration |
| Package Management | 10-20 files | 500 KB - 2 MB | dpkg, apt, unattended-upgrades |
| System Log Files | 15-30 files | 10-100 MB | syslog, auth, kern, dmesg |
| System Configuration | 15-25 files | < 500 KB | fstab, sudoers, sysctl |
| Disk Info | 1 item | < 100 KB | Disk partition layout |

**Total Estimated Size:** 15-125 MB depending on log retention

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
| `/etc/apt` | APT configuration | |
| `/etc/apt/sources.list.d` | APT sources | |
| `/usr/lib/systemd/system` | Vendor systemd units | |
| `/usr/lib/systemd/user` | Vendor user units | |

### 2. DHCP/Dhclient Files (5-10 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/lib/NetworkManager/*.lease` | NetworkManager leases | |
| `/var/lib/NetworkManager/*.leases` | NM leases (alternate) | |
| `/var/lib/dhclient/*.lease` | dhclient leases | |
| `/var/lib/dhclient/*.leases` | dhclient leases (alternate) | |
| `/var/lib/dhcp/*.lease` | ISC DHCP leases | |
| `/var/lib/dhcp/*.leases` | ISC DHCP leases (alternate) | |

### 3. Networking Files (15-25 files)

| Path | Purpose | X |
|------|---------|---|
| `/etc/netplan/*.yaml` | Netplan configuration | |
| `/etc/dhcp/*.conf` | DHCP client config | |
| `/etc/network/interfaces` | Legacy network config | |
| `/etc/network/interfaces.d/*.cfg` | Interface includes | |
| `/etc/ufw/ufw.conf` | UFW firewall config | |
| `/etc/ufw/user.rules` | UFW IPv4 rules | |
| `/etc/ufw/user6.rules` | UFW IPv6 rules | |
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

### 5. Package Management Log Files (10-20 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/dpkg*` | dpkg package logs | |
| `/var/log/apt/*` | APT logs | |
| `/var/log/unattended-upgrades/*` | Auto-update logs | |

### 6. System Log Files (15-30 files)

| Path | Purpose | X |
|------|---------|---|
| `/var/log/syslog*` | System log | |
| `/var/log/rsyslog*` | Rsyslog output | |
| `/var/log/messages*` | System messages (fallback) | |
| `/var/log/kern*` | Kernel messages | |
| `/var/log/dmesg*` | Boot ring buffer | |
| `/var/log/boot*` | Boot logs | |
| `/var/log/auth*` | Authentication log | X |
| `/var/log/secure*` | Secure log (fallback) | X |
| `/var/log/pacemaker*` | Pacemaker cluster | |
| `/var/log/corosync*` | Corosync cluster | |
| `/var/log/cluster/*` | Cluster logs | |
| `/var/log/pacemaker/*` | Pacemaker directory | |
| `/var/log/corosync/*` | Corosync directory | |

### 7. System Configuration Files (15-25 files)

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
| `/sys/kernel/security/apparmor/profiles` | AppArmor profiles | |

### 8. Disk Info (1 item)

| Command | Purpose | X |
|---------|---------|---|
| `diskinfo,` | Disk partition info | |

---

## Legend

**X Column:** Items marked with X may contain sensitive or personally identifiable information (PII):
- Authentication logs with usernames
- Encrypted volume passphrases
- Sudo user configurations
- Host-specific network information

---

## Potentially Missing Items

### Boot and Kernel
| Item | Path | Why It's Useful |
|------|------|-----------------|
| GRUB configuration | `/boot/grub/grub.cfg`, `/etc/default/grub` | Boot parameter issues |
| Kernel crash dumps | `/var/crash/*` | Kernel panic analysis |
| initramfs logs | `/var/log/mkinitramfs.log` | Boot issues |

### APT/Package Management
| Item | Path | Why It's Useful |
|------|------|-----------------|
| APT sources | `/etc/apt/sources.list` | Repository configuration |
| APT preferences | `/etc/apt/preferences.d/*` | Package pinning |
| dpkg status | `/var/lib/dpkg/status` | Installed packages |

### Systemd
| Item | Path | Why It's Useful |
|------|------|-----------------|
| Journal export | `journalctl` output | Comprehensive logs |
| Failed units | `systemctl --failed` | Service failures |
| Service overrides | `/etc/systemd/system/*.d/*.conf` | Custom settings |

### Security
| Item | Path | Why It's Useful |
|------|------|-----------------|
| AppArmor logs | `/var/log/audit/audit.log` | Policy denials |
| fail2ban logs | `/var/log/fail2ban.log` | SSH brute force |
| UFW logs | `/var/log/ufw.log` | Firewall events |

### Network
| Item | Path | Why It's Useful |
|------|------|-----------------|
| netplan rendered config | `/run/netplan/*.yaml` | Applied config |
| systemd-resolved | `/etc/systemd/resolved.conf` | DNS resolution |
| Wireguard config | `/etc/wireguard/*.conf` | VPN configuration |
