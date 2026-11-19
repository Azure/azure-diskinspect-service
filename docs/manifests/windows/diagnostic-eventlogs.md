# Windows Event Logs Diagnostic Manifests

Modular manifests for collecting Windows Event Logs.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-eventlogs-general-common` | System, Application, Setup logs | 25-150 MB | Low |
| `diagnostic-eventlogs-client-windowsupdate` | Windows Update client events | 5-50 MB | None |
| `diagnostic-eventlogs-do-windowsupdate` | Delivery Optimization, BITS | 5-30 MB | None |
| `diagnostic-eventlogs-setup-osupgrade` | Setup, Upgrade Diagnostics | 5-50 MB | None |
| `diagnostic-eventlogs-taskscheduler-common` | Task Scheduler operational | 5-30 MB | None |
| `diagnostic-eventlogs-kernel-common` | Kernel PnP, Power events | 5-30 MB | None |
| `diagnostic-eventlogs-security-common` | CAPI2, Licensing events | 5-30 MB | Low |
| `diagnostic-eventlogs-grouppolicy-common` | Group Policy operational | 5-20 MB | None |

## File Locations

### diagnostic-eventlogs-general-common
```
/Windows/System32/winevt/Logs/System.evtx
/Windows/System32/winevt/Logs/Application.evtx
/Windows/System32/winevt/Logs/Setup.evtx
```

### diagnostic-eventlogs-client-windowsupdate
```
/Windows/System32/winevt/Logs/Microsoft-Windows-WindowsUpdateClient%4Operational.evtx
/Windows/System32/winevt/Logs/Microsoft-Windows-Servicing%4Admin.evtx
/Windows/System32/winevt/Logs/Microsoft-Windows-WUSA%4Operational.evtx
```

### diagnostic-eventlogs-do-windowsupdate
```
/Windows/System32/winevt/Logs/Microsoft-Windows-DeliveryOptimization%4Operational.evtx
/Windows/System32/winevt/Logs/Microsoft-Windows-Bits-Client%4Operational.evtx
```

### diagnostic-eventlogs-setup-osupgrade
```
/Windows/System32/winevt/Logs/Microsoft-Windows-Setup%4Operational.evtx
/Windows/System32/winevt/Logs/Microsoft-Windows-Upgrade-Diagnostics%4Operational.evtx
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Windows Update failures | `eventlogs-general-common` + `eventlogs-client-windowsupdate` |
| Download issues | `eventlogs-do-windowsupdate` |
| OS Upgrade failures | `eventlogs-setup-osupgrade` + `eventlogs-general-common` |
| Boot/driver issues | `eventlogs-kernel-common` |
| Scheduled task issues | `eventlogs-taskscheduler-common` |
| Policy issues | `eventlogs-grouppolicy-common` |
