# Windows OS Upgrade Staging Diagnostic Manifests

Modular manifests for Windows Feature Update staging folders.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-staging-bt-osupgrade` | $Windows.~BT staging | 10-100 MB | None |
| `diagnostic-staging-ws-osupgrade` | $Windows.~WS rollback | 10-100 MB | None |
| `diagnostic-staging-safeos-osupgrade` | SafeOS DU phase | 5-30 MB | None |

## File Locations

### diagnostic-staging-bt-osupgrade
```
ll,/$Windows.~BT
/$Windows.~BT/Sources/Panther/setupact.log
/$Windows.~BT/Sources/Panther/setuperr.log
/$Windows.~BT/Sources/Panther/miglog.xml
/$Windows.~BT/Sources/Panther/cbs_unattend.log
```

### diagnostic-staging-ws-osupgrade
```
ll,/$Windows.~WS
/$Windows.~WS/Sources/Panther/setupact.log
/$Windows.~WS/Sources/Panther/setuperr.log
```

### diagnostic-staging-safeos-osupgrade
```
ll,/$Windows.~BT/Sources/SafeOS/SafeOS.Mount
/$Windows.~BT/Sources/SafeOS/setupact.log
/$Windows.~BT/Sources/SafeOS/setuperr.log
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Feature update download phase | `staging-bt-osupgrade` |
| Feature update installation | `staging-bt-osupgrade` + `staging-safeos-osupgrade` |
| Rollback occurred | `staging-ws-osupgrade` + `staging-bt-osupgrade` |
| SafeOS boot failures | `staging-safeos-osupgrade` |

## Folder Descriptions

| Folder | Purpose |
|--------|---------|
| `$Windows.~BT` | Feature update staging - downloaded content and setup logs |
| `$Windows.~WS` | Windows Setup rollback data |
| `SafeOS` | WinRE-based phase for applying updates |

## Notes

- These folders exist only during/after feature updates
- `$Windows.~BT` is created during download phase
- `$Windows.~WS` contains rollback information if upgrade fails
- SafeOS is used for the "Installing updates" phase at reboot
