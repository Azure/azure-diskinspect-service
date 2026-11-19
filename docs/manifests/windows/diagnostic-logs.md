# Windows Update Logs Diagnostic Manifests

Modular manifests for Windows Update and Setup log files.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-logs-client-windowsupdate` | WindowsUpdate.log, ETL | 10-100 MB | None |
| `diagnostic-logs-sih-windowsupdate` | SIH service logs | 5-20 MB | None |
| `diagnostic-logs-dpx-windowsupdate` | DPX setup logs | 1-10 MB | None |
| `diagnostic-logs-setupapi-windowsupdate` | SetupAPI logs | 10-50 MB | None |
| `diagnostic-logs-mosetup-osupgrade` | MoSetup/UpdateAgent | 5-30 MB | None |

## File Locations

### diagnostic-logs-client-windowsupdate
```
/Windows/WindowsUpdate.log
/Windows/Logs/WindowsUpdate/*.log
/Windows/Logs/WindowsUpdate/*.etl
```

### diagnostic-logs-sih-windowsupdate
```
/Windows/Logs/SIH/SIH*.log
/Windows/Logs/SIH/SIH*.etl
```

### diagnostic-logs-dpx-windowsupdate
```
/Windows/Logs/DPX/setupact.log
/Windows/Logs/DPX/setuperr.log
```

### diagnostic-logs-setupapi-windowsupdate
```
/Windows/INF/setupapi.dev.log
/Windows/INF/setupapi.app.log
```

### diagnostic-logs-mosetup-osupgrade
```
/Windows/Logs/mosetup/UpdateAgent.log
/Windows/Logs/MoSetup/BlueBox.log
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Windows Update failures | `logs-client-windowsupdate` |
| Driver update issues | `logs-setupapi-windowsupdate` |
| Feature update issues | `logs-mosetup-osupgrade` |
| SIH/remediation issues | `logs-sih-windowsupdate` |
| Package extraction | `logs-dpx-windowsupdate` |

## Log Descriptions

| Log | Purpose |
|-----|---------|
| WindowsUpdate.log | Main WU client log (legacy and ETL-converted) |
| SIH*.log | Self-Initiated Healing service logs |
| setupapi.dev.log | Device driver installation log |
| setupapi.app.log | Application setup log |
| UpdateAgent.log | Feature update agent log |

## Notes

- WindowsUpdate.log on Windows 10+ requires ETL conversion
- SetupAPI logs are key for driver installation issues
- SIH is used for automated WU remediation
