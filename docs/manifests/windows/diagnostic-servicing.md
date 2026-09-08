# Windows Servicing Diagnostic Manifests

Modular manifests for Component-Based Servicing (CBS) diagnostics.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-servicing-cbs-windowsupdate` | CBS logs and cabs | 50-300 MB | None |
| `diagnostic-servicing-dism-windowsupdate` | DISM operation logs | 5-30 MB | None |
| `diagnostic-servicing-sessions-windowsupdate` | Servicing Sessions.xml | 1-10 MB | None |
| `diagnostic-servicing-sfc-windowsupdate` | System File Checker logs | 1-10 MB | None |
| `diagnostic-servicing-waasmedic-windowsupdate` | WaaS Medic service logs | 5-20 MB | None |

## File Locations

### diagnostic-servicing-cbs-windowsupdate
```
/Windows/Logs/CBS/CBS.log
/Windows/Logs/CBS/CbsPersist*.log
/Windows/Logs/CBS/CbsPersist*.cab
```

### diagnostic-servicing-dism-windowsupdate
```
/Windows/Logs/DISM/dism.log
/Windows/Logs/DISM/dism_*.log
```

### diagnostic-servicing-sessions-windowsupdate
```
/Windows/servicing/Sessions.xml
/Windows/servicing/Sessions/Sessions.xml
ll,/Windows/servicing/Sessions
```

### diagnostic-servicing-sfc-windowsupdate
```
/Windows/Logs/CBS/sfc*.log
```

### diagnostic-servicing-waasmedic-windowsupdate
```
/Windows/Logs/waasmedic/waasmedic.log
/Windows/Logs/waasmedic/WaaSMedic*.etl
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Update installation failures | `servicing-cbs-windowsupdate` + `servicing-dism-windowsupdate` |
| CBS corruption | `servicing-cbs-windowsupdate` + `servicing-sessions-windowsupdate` |
| DISM errors | `servicing-dism-windowsupdate` |
| SFC failures | `servicing-sfc-windowsupdate` + `servicing-cbs-windowsupdate` |
| WU not working | `servicing-waasmedic-windowsupdate` |

## Size Warnings

| Manifest | Warning |
|----------|---------|
| `diagnostic-servicing-cbs-windowsupdate` | CbsPersist cabs can be 10-100 MB each |

## Key Error Patterns

- CBS.log: `Error`, `HRESULT`, `STATUS_`
- DISM.log: `Error`, `Failed`
- SFC: `Cannot repair`, `Corrupt`
