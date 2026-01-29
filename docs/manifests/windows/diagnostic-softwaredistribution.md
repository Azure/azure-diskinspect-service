# Windows Software Distribution Diagnostic Manifests

Modular manifests for Windows Update download cache and database.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-softwaredistribution-reporting-windowsupdate` | ReportingEvents.log | 1-10 MB | None |
| `diagnostic-softwaredistribution-do-windowsupdate` | Delivery Optimization logs | 5-50 MB | None |
| `diagnostic-softwaredistribution-plugins-windowsupdate` | WU Plugins directory | 1-5 MB | None |
| `diagnostic-softwaredistribution-download-windowsupdate` | Download metadata, SLS | 5-30 MB | None |
| `diagnostic-softwaredistribution-datastore-windowsupdate` | DataStore.edb database | 50-500 MB | None |

## File Locations

### diagnostic-softwaredistribution-reporting-windowsupdate
```
/Windows/SoftwareDistribution/ReportingEvents.log
```

### diagnostic-softwaredistribution-do-windowsupdate
```
/Windows/SoftwareDistribution/DeliveryOptimization*.log
/Windows/ServiceProfiles/NetworkService/AppData/Local/Microsoft/Windows/DeliveryOptimization/Logs/*.log
/Windows/ServiceProfiles/NetworkService/AppData/Local/Microsoft/Windows/DeliveryOptimization/Logs/*.etl
```

### diagnostic-softwaredistribution-plugins-windowsupdate
```
ll,/Windows/SoftwareDistribution/Plugins
```

### diagnostic-softwaredistribution-download-windowsupdate
```
ll,/Windows/SoftwareDistribution/Download
/Windows/SoftwareDistribution/Download/*.log
/Windows/SoftwareDistribution/SLS/*.log
```

### diagnostic-softwaredistribution-datastore-windowsupdate
```
/Windows/SoftwareDistribution/DataStore/DataStore.edb (noscan)
/Windows/SoftwareDistribution/DataStore/Logs/*.log
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Update history | `softwaredistribution-reporting-windowsupdate` |
| Download failures | `softwaredistribution-do-windowsupdate` + `softwaredistribution-download-windowsupdate` |
| WU database corruption | `softwaredistribution-datastore-windowsupdate` |
| P2P download issues | `softwaredistribution-do-windowsupdate` |

## Size Warnings

| Manifest | Warning |
|----------|---------|
| `diagnostic-softwaredistribution-datastore-windowsupdate` | DataStore.edb can be 50-500 MB |

## Notes

- ReportingEvents.log contains history of all update operations
- DataStore.edb is the Windows Update database
- Delivery Optimization handles P2P and CDN downloads
