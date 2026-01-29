# Azure Files Diagnostic Manifests

Modular manifests for Azure cloud and storage integration diagnostics.

## Available Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-cloudinit-common` | Cloud-init provisioning logs and config | Low |
| `diagnostic-blobfuse-common` | Blobfuse mount logs | None |

## Issue Type Selection

### VM Provisioning Issues
```
diagnostic-cloudinit-common
diagnostic-azure-agent-logs
diagnostic-azure-agent-state
```

### Blobfuse Mount Issues
```
diagnostic-blobfuse-common
diagnostic-syslog-common
diagnostic-fstab-common
```

### Cloud-init Issues
```
diagnostic-cloudinit-common
diagnostic-syslog-common
diagnostic-kernlog-common
```

## Manifest Details

### diagnostic-cloudinit-common

Collects cloud-init provisioning files:
- `/var/log/cloud-init*` - Cloud-init logs
- `/etc/cloud/cloud.cfg` - Main cloud-init config
- `/etc/cloud/cloud.cfg.d/*.cfg` - Config includes
- `/run/cloud-init/cloud.cfg` - Runtime config
- `/run/cloud-init/ds-identify.log` - Datasource identification
- `/run/cloud-init/result.json` - Provisioning result
- `/run/cloud-init/status.json` - Provisioning status

### diagnostic-blobfuse-common

Collects blobfuse mount logs:
- `/var/log/blobfuse*` - Blobfuse v1 logs
- `/var/log/blobfuse2.log*` - Blobfuse v2 logs

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-cloudinit-common | 500 KB - 2 MB |
| diagnostic-blobfuse-common | < 10 MB |

