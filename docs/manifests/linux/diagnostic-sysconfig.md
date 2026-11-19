# System Configuration Diagnostic Manifests

Modular manifests for system configuration troubleshooting.

## Available Manifests

### Filesystem and Storage
| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-fstab-common` | fstab, crypttab, mdadm | None |
| `diagnostic-diskinfo-common` | Disk partition layout | None |
| `diagnostic-nfs-common` | NFS and idmapd config | None |

### Security and Authentication
| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-pam-common` | All | PAM configuration, limits.conf | Low |
| `diagnostic-sudoers-common` | All | sudoers configuration | **Medium** |
| `diagnostic-authlog-common` | All | auth.log, secure, wtmp, btmp | **High** |
| `diagnostic-security-ubuntu` | Ubuntu/Debian | AppArmor | None |
| `diagnostic-security-redhat` | RHEL/CentOS/Fedora | SELinux | None |
| `diagnostic-security-suse` | SLES/openSUSE | AppArmor | None |
| `diagnostic-security-mariner` | Azure Linux | SELinux | None |

### Kernel and Boot
| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-bootconfig-common` | GRUB configuration | None |
| `diagnostic-bootlog-common` | Boot logs | None |
| `diagnostic-kernlog-common` | Kernel logs, dmesg | None |
| `diagnostic-sysctl-common` | Sysctl configuration | None |
| `diagnostic-udev-common` | Udev rules, modprobe | None |

### System Identity
| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-release-common` | OS release, hostname, machine-id | Low |
| `diagnostic-time-common` | Chrony, NTP, timezone | None |

## Issue Type Selection

### Boot Issues
```
diagnostic-bootconfig-common
diagnostic-bootlog-common
diagnostic-kernlog-common
diagnostic-fstab-common
diagnostic-diskinfo-common
```

### Disk Mount Issues
```
diagnostic-fstab-common
diagnostic-diskinfo-common
diagnostic-kernlog-common
diagnostic-syslog-common
```

### Authentication Issues
```
diagnostic-authlog-common
diagnostic-pam-common
diagnostic-sudoers-common
diagnostic-ssh-common
```

### Kernel Driver Issues
```
diagnostic-kernlog-common
diagnostic-udev-common
diagnostic-sysctl-common
diagnostic-bootlog-common
```

### Time Sync Issues
```
diagnostic-time-common
diagnostic-syslog-common
```

### Security Policy Issues
```
diagnostic-security-<distro>
diagnostic-authlog-common
diagnostic-syslog-common
```

