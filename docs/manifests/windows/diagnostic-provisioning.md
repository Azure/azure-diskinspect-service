# Windows Provisioning Diagnostic Manifests

Modular manifests for Windows provisioning and setup diagnostics.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-provisioning-panther-osupgrade` | Panther setup logs | 10-50 MB | Low |
| `diagnostic-provisioning-sysprep-osupgrade` | Sysprep files and logs | 5-30 MB | Low |
| `diagnostic-provisioning-state-osupgrade` | Setup State.ini | 1-5 MB | None |
| `diagnostic-provisioning-firstboot-osupgrade` | First logon commands | 1-10 MB | None |

## File Locations

### diagnostic-provisioning-panther-osupgrade
```
/Windows/Panther/setupact.log
/Windows/Panther/setuperr.log
/Windows/Panther/UnattendGC/setupact.log
/Windows/Panther/UnattendGC/setuperr.log
/Windows/Panther/cbs_unattend.log
/Windows/Panther/DDACLSys.log
/Windows/Panther/UnattendedJoin/UnattendedJoinDCLocator.etl
/Windows/Panther/miglog.xml
```

### diagnostic-provisioning-sysprep-osupgrade
```
/Windows/System32/Sysprep/Panther/setupact.log
/Windows/System32/Sysprep/Panther/setuperr.log
/Windows/System32/Sysprep/Panther/IE/setupact.log
/Windows/System32/Sysprep/Sysprep_succeeded.tag
/Windows/System32/Sysprep/Unattend.xml
ll,/Windows/System32/Sysprep
```

### diagnostic-provisioning-state-osupgrade
```
/Windows/Setup/State/State.ini
ll,/Windows/Setup/State
```

### diagnostic-provisioning-firstboot-osupgrade
```
/Windows/Panther/FirstLogonCommands.log
/Windows/Panther/Specialize.log
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| VM provisioning failures | `provisioning-panther-osupgrade` + `provisioning-sysprep-osupgrade` |
| Sysprep failures | `provisioning-sysprep-osupgrade` |
| Setup stuck | `provisioning-state-osupgrade` + `provisioning-panther-osupgrade` |
| First boot issues | `provisioning-firstboot-osupgrade` |
| Azure VM generalization | `provisioning-sysprep-osupgrade` |

## Key Error Patterns

- setupact.log: Look for `Error`, `Warning`, `OOBE`
- setuperr.log: All entries are errors
- State.ini: Check `IMAGE_STATE` value
