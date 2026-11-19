# Windows Update Orchestrator Diagnostic Manifests

Modular manifests for Update Session Orchestrator (USO) and health tools.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-orchestrator-uso-windowsupdate` | USO UpdateStore, logs | 10-100 MB | None |
| `diagnostic-orchestrator-healthtools-windowsupdate` | Update Health Tools | 5-30 MB | None |

## File Locations

### diagnostic-orchestrator-uso-windowsupdate
```
/ProgramData/USOPrivate/UpdateStore/*.xml
/ProgramData/USOShared/Logs/*.log
/ProgramData/USOShared/Logs/*.etl
ll,/ProgramData/USOPrivate
ll,/ProgramData/USOShared
```

### diagnostic-orchestrator-healthtools-windowsupdate
```
/ProgramData/Microsoft/Windows/UpdateHealthTools/*.log
/ProgramData/Microsoft/Windows/UpdateHealthTools/*.etl
ll,/ProgramData/Microsoft/Windows/UpdateHealthTools
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Updates not scanning | `orchestrator-uso-windowsupdate` |
| Updates stuck pending | `orchestrator-uso-windowsupdate` |
| WU service issues | `orchestrator-uso-windowsupdate` + `orchestrator-healthtools-windowsupdate` |
| Update Health alerts | `orchestrator-healthtools-windowsupdate` |

## Notes

- USO (Update Session Orchestrator) replaced the legacy WU service in Windows 10+
- UpdateStore contains pending update state
- Update Health Tools are used by Microsoft to diagnose WU issues remotely
