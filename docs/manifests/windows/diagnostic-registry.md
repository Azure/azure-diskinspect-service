# Windows Registry Diagnostic Manifests

Modular manifests for collecting Windows Registry hives.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-registry-bcd-common` | Boot Configuration Data | 1-5 MB | None |
| `diagnostic-registry-system-common` | SYSTEM hive | 20-80 MB | Low |
| `diagnostic-registry-software-common` | SOFTWARE hive | 50-200 MB | Medium |
| `diagnostic-registry-components-windowsupdate` | COMPONENTS hive (CBS) | 50-300 MB | None |

## File Locations

### diagnostic-registry-bcd-common
```
/Boot/BCD
```

### diagnostic-registry-system-common
```
/Windows/System32/config/SYSTEM
```

### diagnostic-registry-software-common
```
/Windows/System32/config/SOFTWARE
```

### diagnostic-registry-components-windowsupdate
```
/Windows/System32/config/COMPONENTS
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Boot failures | `registry-bcd-common` + `registry-system-common` |
| Service issues | `registry-system-common` |
| Windows Update | `registry-components-windowsupdate` + `registry-software-common` |
| CBS corruption | `registry-components-windowsupdate` |
| Driver issues | `registry-system-common` |

## Size Warnings

| Manifest | Warning |
|----------|---------|
| `diagnostic-registry-software-common` | Can be 50-200 MB |
| `diagnostic-registry-components-windowsupdate` | Can be 50-300 MB on systems with many updates |

## Notes

- All registry hives use `noscan` to prevent content scanning
- COMPONENTS hive grows significantly with installed updates
- SOFTWARE contains machine policies and application settings
- SYSTEM contains service configurations and driver settings
