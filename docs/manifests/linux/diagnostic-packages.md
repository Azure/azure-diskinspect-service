# Package Management Diagnostic Manifests

Modular manifests for package management troubleshooting.

## Package Logs - Distro Specific

| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-packages-ubuntu` | Ubuntu/Debian | dpkg, APT, unattended-upgrades | None |
| `diagnostic-packages-redhat` | RHEL/CentOS/Fedora | YUM, DNF, RHSM, RHUI | Low |
| `diagnostic-packages-suse` | SLES/openSUSE | Zypper logs | None |
| `diagnostic-packages-mariner` | Azure Linux | TDNF, DNF logs | None |

## Repository Configuration - Distro Specific

| Manifest | Scope | Description | PII Risk |
|----------|-------|-------------|----------|
| `diagnostic-repoconfig-ubuntu` | Ubuntu/Debian | sources.list | None |
| `diagnostic-repoconfig-redhat` | RHEL/CentOS/Fedora | yum.repos.d | None |
| `diagnostic-repoconfig-suse` | SLES/openSUSE | zypp repos | None |
| `diagnostic-repoconfig-mariner` | Azure Linux | tdnf repos | None |

## Issue Type Selection

### Package Installation Issues
```
diagnostic-packages-<distro>
diagnostic-repoconfig-<distro>
diagnostic-syslog-common
```

### Repository Access Issues
```
diagnostic-repoconfig-<distro>
diagnostic-dns-common
diagnostic-netconfig-<distro>
diagnostic-syslog-common
```

### RHEL Subscription Issues
```
diagnostic-packages-redhat
diagnostic-repoconfig-redhat
diagnostic-syslog-common
```

### SUSE Registration Issues
```
diagnostic-packages-suse
diagnostic-repoconfig-suse
diagnostic-cloudregister-suse
diagnostic-syslog-common
```

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-packages-ubuntu | 100 KB - 2 MB |
| diagnostic-packages-redhat | 100 KB - 5 MB |
| diagnostic-packages-suse | 100 KB - 1 MB |
| diagnostic-packages-mariner | 100 KB - 1 MB |
| diagnostic-repoconfig-* | < 100 KB |

