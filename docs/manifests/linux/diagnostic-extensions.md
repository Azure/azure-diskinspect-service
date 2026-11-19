# Azure Extensions Diagnostic Manifests

Modular manifests for Azure VM extension diagnostics.

## Core Extension Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-extensions-probing` | Directory listings for extension dirs | None |
| `diagnostic-extensions-handler` | Handler config, state, status files | Low |
| `diagnostic-extensions-logs` | Extension logs from /var/log/azure | Low |

## Extension-Specific Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-extensions-monitoring` | Azure Monitor Agent - AMA | Low |
| `diagnostic-extensions-lad` | Linux Diagnostic Extension | Low |
| `diagnostic-extensions-siterecovery` | Site Recovery Extension | Low |
| `diagnostic-extensions-sqliaas` | SQL IaaS Extension | Low |
| `diagnostic-extensions-workloadbackup` | Workload Backup - SAP HANA | Low |
| `diagnostic-extensions-servicefabric` | Service Fabric and Key Vault | Low |

## Issue Type Selection

### General Extension Handler Issues
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

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-extensions-probing | < 100 KB |
| diagnostic-extensions-handler | 100 KB - 1 MB |
| diagnostic-extensions-logs | 1-50 MB |
| diagnostic-extensions-monitoring | 1-20 MB |
| diagnostic-extensions-lad | 1-10 MB |
| diagnostic-extensions-siterecovery | 1-10 MB |
| diagnostic-extensions-sqliaas | 1-20 MB |
| diagnostic-extensions-workloadbackup | 5-50 MB |
| diagnostic-extensions-servicefabric | 1-10 MB |

