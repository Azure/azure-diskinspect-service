# Windows Recovery Diagnostic Manifests

Modular manifests for Windows recovery and error reporting.

## Available Manifests

| Manifest | Description | Size Est. | PII |
|----------|-------------|-----------|-----|
| `diagnostic-recovery-startuprepair-osupgrade` | Startup Repair logs | 1-10 MB | None |
| `diagnostic-recovery-wer-osupgrade` | Windows Error Reporting | 5-30 MB | Low |
| `diagnostic-recovery-postsetup-osupgrade` | Post-setup action logs | 1-10 MB | None |

## File Locations

### diagnostic-recovery-startuprepair-osupgrade
```
/Windows/System32/LogFiles/Srt/SrtTrail.txt
/Windows/System32/LogFiles/Srt/srt-ui-*.txt
ll,/Windows/System32/LogFiles/Srt
```

### diagnostic-recovery-wer-osupgrade
```
ll,/ProgramData/Microsoft/Windows/WER/ReportQueue
/ProgramData/Microsoft/Windows/WER/ReportQueue/*/Report.wer
```

### diagnostic-recovery-postsetup-osupgrade
```
/Windows/Logs/mosetup/UpdateAgent.log
/Windows/Logs/MoSetup/BlueBox.log
```

## Use Cases

| Issue Type | Recommended Manifests |
|------------|----------------------|
| Boot loop after update | `recovery-startuprepair-osupgrade` |
| BSOD after update | `recovery-wer-osupgrade` |
| Upgrade completed but issues | `recovery-postsetup-osupgrade` |
| Automatic repair triggered | `recovery-startuprepair-osupgrade` |

## Key Files

| File | Purpose |
|------|---------|
| `SrtTrail.txt` | Startup Repair diagnostic trail |
| `Report.wer` | Windows Error Report details |
| `UpdateAgent.log` | Post-upgrade setup actions |
| `BlueBox.log` | Feature update completion tasks |

## Notes

- SrtTrail.txt is created when Startup Repair runs
- WER reports contain crash details and may identify failing components
- Post-setup logs show actions taken after feature update completes
