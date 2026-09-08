# System Logs Diagnostic Manifests

Modular manifests for system log collection.

## Available Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-syslog-common` | syslog, messages | Low |
| `diagnostic-authlog-common` | auth.log, secure, wtmp, btmp | **High** |
| `diagnostic-kernlog-common` | kern.log, dmesg | None |
| `diagnostic-bootlog-common` | boot.log | None |
| `diagnostic-clusterlog-common` | Pacemaker, Corosync cluster logs | Low |
| `diagnostic-cloudregister-suse` | SUSE cloud registration log | None |

## Probing Manifests - Distro Specific

| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-probing-ubuntu` | Ubuntu/Debian | APT dirs, systemd | None |
| `diagnostic-probing-redhat` | RHEL/CentOS/Fedora | YUM repos, systemd | None |
| `diagnostic-probing-suse` | SLES/openSUSE | Zypp repos, systemd | None |
| `diagnostic-probing-mariner` | Azure Linux | TDNF, systemd | None |

## SOS Reports

| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-sosreport-common` | RHEL/Ubuntu | sosreport tarballs | **High** |
| `diagnostic-supportconfig-suse` | SLES/openSUSE | supportconfig tarballs | **High** |

## Issue Type Selection

### General System Issues
```
diagnostic-probing-<distro>
diagnostic-syslog-common
diagnostic-kernlog-common
```

### Boot Issues
```
diagnostic-bootlog-common
diagnostic-kernlog-common
diagnostic-syslog-common
```

### Kernel Panic or Crash
```
diagnostic-kernlog-common
diagnostic-syslog-common
diagnostic-bootlog-common
```

### Cluster HA Issues
```
diagnostic-clusterlog-common
diagnostic-syslog-common
diagnostic-fstab-common
```

### Full System Snapshot
```
diagnostic-sosreport-common   (RHEL/Ubuntu)
diagnostic-supportconfig-suse (SUSE)
```

## PII Risk Summary

| Risk Level | Manifests |
|------------|-----------|
| **High** | authlog-common, sosreport-common, supportconfig-suse |
| **Medium** | sudoers-common |
| **Low** | syslog-common, clusterlog-common |
| **None** | All others |

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-syslog-common | 1-50 MB |
| diagnostic-authlog-common | 1-20 MB |
| diagnostic-kernlog-common | 1-10 MB |
| diagnostic-bootlog-common | < 1 MB |
| diagnostic-clusterlog-common | 1-20 MB |
| diagnostic-sosreport-common | 10-500 MB |
| diagnostic-supportconfig-suse | 10-500 MB |

