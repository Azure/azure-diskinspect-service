# Windows Update and OS Upgrade Diagnostic Manifests - Modular Reference

This document provides an overview of modular Windows Update and OS Upgrade diagnostic manifests. For detailed documentation on each area, see the specific docs linked below.

## Documentation by Area

| Area | Document | Description |
|------|----------|-------------|
| Event Logs | [diagnostic-eventlogs.md](diagnostic-eventlogs.md) | System, WU, DO, Setup event logs |
| Registry | [diagnostic-registry.md](diagnostic-registry.md) | BCD, SYSTEM, SOFTWARE, COMPONENTS |
| Servicing | [diagnostic-servicing.md](diagnostic-servicing.md) | CBS, DISM, SFC, WaaS Medic |
| Software Distribution | [diagnostic-softwaredistribution.md](diagnostic-softwaredistribution.md) | Download cache, DataStore, DO |
| Orchestrator | [diagnostic-orchestrator.md](diagnostic-orchestrator.md) | USO, Update Health Tools |
| Provisioning | [diagnostic-provisioning.md](diagnostic-provisioning.md) | Panther, Sysprep, Setup State |
| Staging | [diagnostic-staging.md](diagnostic-staging.md) | $Windows.~BT, ~WS, SafeOS |
| Recovery | [diagnostic-recovery.md](diagnostic-recovery.md) | Startup Repair, WER, Post-Setup |
| Logs | [diagnostic-logs.md](diagnostic-logs.md) | WindowsUpdate.log, SetupAPI, SIH |
| OS Upgrade | [diagnostic-osupgrade.md](diagnostic-osupgrade.md) | Appraiser, Windows.old, Cleanup |

## Naming Convention

**Format:** `diagnostic-<category>-<subcategory>-<windowsupdate|osupgrade|common>`

- Category-first enables grouping by data type
- `-windowsupdate` suffix = Windows Update specific
- `-osupgrade` suffix = Feature Update / OS Upgrade specific
- `-common` suffix = shared across both scenarios

---

## Quick Reference - All Manifests

### Event Logs
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-eventlogs-general-common` | System, Application, Setup logs | 25-150 MB |
| `diagnostic-eventlogs-client-windowsupdate` | Windows Update client event logs | 5-50 MB |
| `diagnostic-eventlogs-do-windowsupdate` | Delivery Optimization, BITS logs | 5-30 MB |
| `diagnostic-eventlogs-setup-osupgrade` | OS Setup and Upgrade Diagnostics logs | 5-50 MB |
| `diagnostic-eventlogs-taskscheduler-common` | Task Scheduler operational logs | 5-30 MB |
| `diagnostic-eventlogs-kernel-common` | Kernel PnP, Kernel Power logs | 5-30 MB |
| `diagnostic-eventlogs-security-common` | CAPI2, Licensing logs | 5-30 MB |
| `diagnostic-eventlogs-grouppolicy-common` | Group Policy operational logs | 5-20 MB |

### Registry Hives
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-registry-bcd-common` | Boot Configuration Data | 1-5 MB |
| `diagnostic-registry-system-common` | SYSTEM hive | 20-80 MB |
| `diagnostic-registry-software-common` | SOFTWARE hive | 50-200 MB |
| `diagnostic-registry-components-windowsupdate` | COMPONENTS hive (CBS state) | 50-300 MB |

### Component-Based Servicing (Windows Update)
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-servicing-cbs-windowsupdate` | CBS logs and cabs | 50-300 MB |
| `diagnostic-servicing-dism-windowsupdate` | DISM logs | 5-30 MB |
| `diagnostic-servicing-sessions-windowsupdate` | Servicing Sessions.xml | 1-10 MB |
| `diagnostic-servicing-sfc-windowsupdate` | SFC logs | 1-10 MB |
| `diagnostic-servicing-waasmedic-windowsupdate` | WaaS Medic service logs | 5-20 MB |

### Software Distribution (Windows Update)
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-softwaredistribution-reporting-windowsupdate` | ReportingEvents.log | 1-10 MB |
| `diagnostic-softwaredistribution-do-windowsupdate` | Delivery Optimization logs | 5-50 MB |
| `diagnostic-softwaredistribution-plugins-windowsupdate` | WU Plugins directory | 1-5 MB |
| `diagnostic-softwaredistribution-download-windowsupdate` | Download metadata, SLS logs | 5-30 MB |
| `diagnostic-softwaredistribution-datastore-windowsupdate` | DataStore.edb database | 50-500 MB |

### Windows Update Logs
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-logs-client-windowsupdate` | WindowsUpdate.log, ETL traces | 10-100 MB |
| `diagnostic-logs-sih-windowsupdate` | SIH service logs | 5-20 MB |
| `diagnostic-logs-dpx-windowsupdate` | DPX setup logs | 1-10 MB |
| `diagnostic-logs-setupapi-windowsupdate` | SetupAPI device/app logs | 10-50 MB |

### Update Orchestrator (Windows Update)
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-orchestrator-uso-windowsupdate` | USO UpdateStore, logs | 10-100 MB |
| `diagnostic-orchestrator-healthtools-windowsupdate` | Update Health Tools logs | 5-30 MB |

### Provisioning (OS Upgrade)
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-provisioning-panther-osupgrade` | Panther setup logs | 10-50 MB |
| `diagnostic-provisioning-sysprep-osupgrade` | Sysprep files and logs | 5-30 MB |
| `diagnostic-provisioning-state-osupgrade` | Setup State.ini | 1-5 MB |
| `diagnostic-provisioning-firstboot-osupgrade` | First logon commands log | 1-10 MB |

### OS Upgrade Staging
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-staging-bt-osupgrade` | $Windows.~BT staging folder | 10-100 MB |
| `diagnostic-staging-ws-osupgrade` | $Windows.~WS rollback folder | 10-100 MB |
| `diagnostic-staging-safeos-osupgrade` | SafeOS DU phase logs | 5-30 MB |

### OS Upgrade - Additional
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-compat-appraiser-osupgrade` | Compatibility Appraiser data | 5-50 MB |
| `diagnostic-logs-mosetup-osupgrade` | MoSetup/UpdateAgent logs | 5-30 MB |
| `diagnostic-previousos-osupgrade` | Windows.old folder logs | 10-50 MB |
| `diagnostic-cleanup-osupgrade` | Disk Cleanup logs | 1-10 MB |

### Recovery (OS Upgrade)
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-recovery-startuprepair-osupgrade` | SRT startup repair logs | 1-10 MB |
| `diagnostic-recovery-wer-osupgrade` | Windows Error Reporting queue | 5-30 MB |
| `diagnostic-recovery-postsetup-osupgrade` | Post-setup action logs | 1-10 MB |

### Azure Extensions
| Manifest | Description | Size Est. |
|----------|-------------|-----------|
| `diagnostic-extensions-updatemanager` | Azure Update Manager extension | 5-100 MB |

## Monolithic Manifest

The original `windowsupdate` manifest remains available and includes all of the above.

## Issue Type Selection

### Windows Update Failure - General
```
diagnostic-eventlogs-general-common
diagnostic-eventlogs-client-windowsupdate
diagnostic-servicing-cbs-windowsupdate
diagnostic-logs-client-windowsupdate
```

### Windows Update Failure - Download Issues
```
diagnostic-softwaredistribution-reporting-windowsupdate
diagnostic-softwaredistribution-do-windowsupdate
diagnostic-softwaredistribution-datastore-windowsupdate
diagnostic-orchestrator-uso-windowsupdate
diagnostic-eventlogs-do-windowsupdate
```

### Windows Update Failure - Installation Issues
```
diagnostic-servicing-cbs-windowsupdate
diagnostic-servicing-dism-windowsupdate
diagnostic-logs-client-windowsupdate
diagnostic-eventlogs-client-windowsupdate
diagnostic-registry-components-windowsupdate
```

### Azure Update Manager Issues
```
diagnostic-extensions-updatemanager
diagnostic-eventlogs-client-windowsupdate
diagnostic-servicing-cbs-windowsupdate
```

### OS Upgrade Failure - Pre-Upgrade
```
diagnostic-compat-appraiser-osupgrade
diagnostic-provisioning-state-osupgrade
diagnostic-eventlogs-setup-osupgrade
```

### OS Upgrade Failure - During Upgrade
```
diagnostic-staging-bt-osupgrade
diagnostic-staging-safeos-osupgrade
diagnostic-servicing-cbs-windowsupdate
diagnostic-eventlogs-setup-osupgrade
```

### OS Upgrade Failure - Rollback
```
diagnostic-staging-ws-osupgrade
diagnostic-previousos-osupgrade
diagnostic-recovery-postsetup-osupgrade
diagnostic-eventlogs-setup-osupgrade
```

### Boot Failure After Update
```
diagnostic-recovery-startuprepair-osupgrade
diagnostic-recovery-wer-osupgrade
diagnostic-registry-bcd-common
diagnostic-eventlogs-kernel-common
```

### VM Provisioning Issues
```
diagnostic-provisioning-panther-osupgrade
diagnostic-provisioning-sysprep-osupgrade
diagnostic-provisioning-firstboot-osupgrade
diagnostic-eventlogs-general-common
diagnostic-registry-system-common
```

## Manifest Details

### diagnostic-registry-*-common
Registry hives containing system configuration:
- `/Boot/BCD` - Boot Configuration Data (diagnostic-registry-bcd-common)
- `/Windows/System32/config/SYSTEM` - Service configurations (diagnostic-registry-system-common)
- `/Windows/System32/config/SOFTWARE` - WU policies, CBS state (diagnostic-registry-software-common)

### diagnostic-registry-components-windowsupdate
CBS-specific registry hive:
- `/Windows/System32/config/COMPONENTS` - Component servicing state

### diagnostic-servicing-*-windowsupdate
Component-Based Servicing - primary diagnostic source:
- `diagnostic-servicing-cbs-windowsupdate` - CBS logs, CBS.log, CbsPersist cabs
- `diagnostic-servicing-dism-windowsupdate` - DISM.log
- `diagnostic-servicing-sessions-windowsupdate` - Sessions.xml
- `diagnostic-servicing-sfc-windowsupdate` - SFC logs
- `diagnostic-servicing-waasmedic-windowsupdate` - WaaS Medic logs

### diagnostic-softwaredistribution-*-windowsupdate
Windows Update download cache and database:
- `diagnostic-softwaredistribution-reporting-windowsupdate` - ReportingEvents.log
- `diagnostic-softwaredistribution-do-windowsupdate` - Delivery Optimization logs
- `diagnostic-softwaredistribution-datastore-windowsupdate` - DataStore.edb (50-500 MB)
- `diagnostic-softwaredistribution-download-windowsupdate` - Download metadata
- `diagnostic-softwaredistribution-plugins-windowsupdate` - WU plugins

### diagnostic-staging-*-osupgrade
Feature update staging folder contents:
- `diagnostic-staging-bt-osupgrade` - $Windows.~BT/Sources/Panther/*
- `diagnostic-staging-ws-osupgrade` - $Windows.~WS rollback logs
- `diagnostic-staging-safeos-osupgrade` - SafeOS phase logs

## Size Warnings

| Manifest | Warning |
|----------|---------|
| `diagnostic-registry-software-common` | SOFTWARE hive can be 50-200 MB |
| `diagnostic-registry-components-windowsupdate` | COMPONENTS hive can be 50-300 MB |
| `diagnostic-servicing-cbs-windowsupdate` | CBS cab files can be 10-100 MB each |
| `diagnostic-softwaredistribution-datastore-windowsupdate` | DataStore.edb can be 50-500 MB |

## Total Size Estimates

| Scenario | Manifests | Total Size |
|----------|-----------|------------|
| Minimal WU triage | eventlogs + cbs | 75-450 MB |
| Full WU diagnostics | All *-windowsupdate manifests | 200 MB - 1.5 GB |
| OS Upgrade diagnostics | All *-osupgrade manifests | 50-450 MB |
| Full diagnostics | All manifests | 350 MB - 2.5 GB |

