# Network Diagnostic Manifests

Modular manifests for network configuration and troubleshooting.

## Available Manifests

### Network Configuration - Distro Specific
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-netconfig-ubuntu` | Ubuntu/Debian | netplan, interfaces | None |
| `diagnostic-netconfig-redhat` | RHEL/CentOS/Fedora | sysconfig/network-scripts | None |
| `diagnostic-netconfig-suse` | SLES/openSUSE | wicked, sysconfig | None |
| `diagnostic-netconfig-mariner` | Azure Linux | systemd-networkd | None |

### NetworkManager
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-networkmanager-common` | All | NM config and state files | None |

### DHCP - Distro Specific
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-dhcp-ubuntu` | Ubuntu/Debian | dhclient, dhcp, NM leases | Low |
| `diagnostic-dhcp-redhat` | RHEL/CentOS/Fedora | dhclient, NM leases | Low |
| `diagnostic-dhcp-suse` | SLES/openSUSE | Wicked, NM leases | Low |
| `diagnostic-dhcp-mariner` | Azure Linux | systemd-networkd, NM leases | Low |

### DNS
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-dns-common` | All | resolv.conf, nsswitch, hosts | Low |

### SSH
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-ssh-common` | All | sshd_config, ssh_config | None |

### Firewall - Distro Specific
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-firewall-ubuntu` | Ubuntu/Debian | UFW rules | None |
| `diagnostic-firewall-redhat` | RHEL/CentOS/Fedora | firewalld, iptables | None |
| `diagnostic-firewall-suse` | SLES/openSUSE | SuSEfirewall2, firewalld | None |
| `diagnostic-firewall-mariner` | Azure Linux | nftables, firewalld | None |

## Issue Type Selection

### Network Connectivity Issues
```
diagnostic-probing-<distro>
diagnostic-dhcp-<distro>
diagnostic-netconfig-<distro>
diagnostic-networkmanager-common
diagnostic-firewall-<distro>
diagnostic-syslog-common
```

### DNS Resolution Issues
```
diagnostic-dns-common
diagnostic-netconfig-<distro>
diagnostic-networkmanager-common
diagnostic-syslog-common
```

### SSH Access Issues
```
diagnostic-ssh-common
diagnostic-pam-common
diagnostic-authlog-common
diagnostic-firewall-<distro>
```

### DHCP Issues
```
diagnostic-dhcp-<distro>
diagnostic-networkmanager-common
diagnostic-syslog-common
```

### Firewall Blocking Issues
```
diagnostic-firewall-<distro>
diagnostic-security-<distro>
diagnostic-syslog-common
```

