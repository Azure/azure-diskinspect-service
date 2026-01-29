# Windows OS Upgrade Additional Diagnostic Manifests

Modular manifests for OS Upgrade compatibility and cleanup.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-compat-appraiser-osupgrade` | Compatibility Appraiser | 5-50 MB | None |
| `diagnostic-previousos-osupgrade` | Windows.old folder | 10-50 MB | Low |
| `diagnostic-cleanup-osupgrade` | Disk Cleanup logs | 1-10 MB | None |

## File Locations

### diagnostic-compat-appraiser-osupgrade
```
/Windows/appcompat/Appraiser*.xml
/Windows/appcompat/Appraiser*.cab
ll,/Windows/appcompat/Programs
```

### diagnostic-previousos-osupgrade
```
ll,/Windows.old
/Windows.old/Windows/Panther/setupact.log
/Windows.old/Windows/Panther/setuperr.log
```

### diagnostic-cleanup-osupgrade
```
/Windows/Logs/DiskCleanup/DiskCleanup.log
ll,/Windows/Logs/DiskCleanup
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Compatibility blocks | `compat-appraiser-osupgrade` |
| Upgrade safeguard holds | `compat-appraiser-osupgrade` |
| Previous OS recovery | `previousos-osupgrade` |
| Disk space issues | `cleanup-osupgrade` |
| Rollback investigation | `previousos-osupgrade` |

## Component Descriptions

| Component | Purpose |
|-----------|---------|
| Appraiser | Evaluates system compatibility before feature updates |
| Windows.old | Contains previous Windows installation for rollback |
| Disk Cleanup | Handles removal of update cleanup files |

## Notes

- Appraiser data identifies compatibility blockers for feature updates
- Windows.old exists for 10 days after upgrade (by default)
- Cleanup logs show what was removed during update cleanup
