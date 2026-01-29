# Windows Update Manifest Documentation

This document describes the `windowsupdate` manifest used for diagnosing Windows Update, OS upgrade, and OS reinstall failures on Azure VMs.

---

## Summary

| Category | Sections | Estimated Total Size |
|----------|----------|---------------------|
| **Windows Update (Patches)** | 10 sections | 100MB - 1GB |
| **OS Upgrade (Feature Updates)** | 8 sections | 50MB - 500MB |
| **Shared/Recovery** | 4 sections | 10MB - 100MB |
| **Total Estimated** | 22 sections | **200MB - 1.5GB** |

---

## Windows Update Sections

### Registry Hives

| File | Typical Size | Purpose |
|------|--------------|---------|
| `/Boot/BCD` | 256KB - 1MB | Boot Configuration Data - boot entries affected by updates |
| `/Windows/System32/config/SOFTWARE` | 50MB - 200MB | Windows Update policies, CBS state, installed updates registry |
| `/Windows/System32/config/SYSTEM` | 10MB - 50MB | Service configurations (wuauserv, BITS, TrustedInstaller) |

**Why Important:** Registry contains Windows Update agent configuration, pending update state, component store health, and service configurations critical for troubleshooting.

**Estimated Files:** 3 files | **Estimated Size:** 60MB - 250MB

---

### Event Logs (General)

| File | Typical Size | Purpose |
|------|--------------|---------|
| `System.evtx` | 20MB - 128MB | Windows Update service events, restart events, driver installs |
| `Application.evtx` | 20MB - 128MB | Application errors during/after updates, MSI events |
| `Setup.evtx` | 1MB - 20MB | OS setup/installation events during upgrades |

**Why Important:** Primary source for error codes, timestamps, and event sequences during update failures.

**Estimated Files:** 3 files | **Estimated Size:** 40MB - 275MB

---

### Provisioning

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/Setup/State/State.ini` | 1 | <1KB | Current setup state |
| `/Windows/Panther/*.xml` | 3-4 | 1-10KB each | Azure VM provisioning config |
| `/Windows/Panther/*.log` | 2-3 | 1-50MB each | Setup action logs |
| `/Windows/Panther/*.etl` | 1 | 5-50MB | Setup ETL traces |
| `/Windows/Panther/*/setupact.log` | 2-3 | 1-20MB each | Unattend and cleanup logs |
| `/Windows/System32/Sysprep/**/*` | 6-8 | 1-10MB each | Sysprep action files and logs |

**Why Important:** Tracks initial OS setup and Sysprep state - helps identify if provisioning issues cause update failures.

**Estimated Files:** 15-20 files | **Estimated Size:** 20MB - 150MB

---

### Windows Update - CBS and Servicing

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/Logs/CBS/*.log` | 5-20 | 5-50MB each | Component-Based Servicing logs (primary WU diagnostics) |
| `/Windows/Logs/CBS/*.cab` | 3-10 | 10-100MB each | CBS diagnostic cab files (compressed logs) |
| `/Windows/Logs/DISM/*.log` | 1-3 | 1-20MB each | DISM operations log |
| `/Windows/WinSxS/pending.xml` | 1 | 1KB - 5MB | Pending servicing operations |
| `/Windows/WinSxS/poqexec.log` | 1 | 1-10MB | Post-reboot queue execution |
| `/Windows/servicing/sessions/*` | 2-10 | 1-50MB total | Servicing session history |

**Why Important:** CBS logs are the **primary diagnostic source** for Windows Update failures. Contains detailed error codes, package states, and installation sequences.

**⚠️ Size Warning:** CBS cab files can be very large (10-100MB each). Consider requesting tool enhancement for `latest:N` syntax.

**Estimated Files:** 15-40 files | **Estimated Size:** 50MB - 500MB

---

### Windows Update - WaaS Medic

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/Logs/waasmedic/*.etl` | 1-5 | 1-20MB each | Windows Update auto-repair diagnostics |

**Why Important:** Shows if Windows tried to self-heal broken WU components and what it found/fixed.

**Estimated Files:** 1-5 files | **Estimated Size:** 1MB - 100MB

---

### Windows Update - Setup API

| File | Typical Size | Purpose |
|------|--------------|---------|
| `/Windows/INF/setupapi.dev.log` | 5MB - 50MB | Device/driver installation during updates |

**Why Important:** Driver installation failures during updates cause many issues - this log captures all driver operations.

**Estimated Files:** 1 file | **Estimated Size:** 5MB - 50MB

---

### Windows Update - Logs and ETL

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/windowsupdate*.log` | 1-2 | 1-10MB | Legacy WU log (pre-1709) |
| `/Windows/Logs/WindowsUpdate/*.etl` | 2-10 | 5-50MB each | Modern WU ETL traces |
| `/Windows/Logs/SIH/*.etl` | 1-5 | 1-10MB each | Server-Initiated Healing (MS-pushed fixes) |
| `/Windows/Logs/dpx/*.log` | 1-3 | 1-5MB each | Package expansion logs |
| `/WindowsUpdateVerbose.etl` | 0-1 | 10-100MB | Verbose WU trace (if enabled) |

**Why Important:** ETL traces contain detailed Windows Update client operations not visible in event logs.

**Estimated Files:** 5-20 files | **Estimated Size:** 20MB - 200MB

---

### Windows Update - SoftwareDistribution

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `ReportingEvents.log` | 1 | 1-10MB | Update reporting history |
| `DeliveryOptimization/SavedLogs/*` | 2-10 | 1-20MB each | DO download logs |
| `Plugins/*/*.log` | 1-3 | 1-5MB each | Token/auth plugin logs |
| `Plugins/*/*.cache` | 1-3 | <1MB each | Plugin cache |
| `Download/*/*/*.xml` | 0-20 | <100KB each | Download metadata |
| `Download/*/*/*.log` | 0-10 | 1-5MB each | Download logs |
| `datastore/DataStore.edb` | 1 | 50MB - 500MB | Windows Update database |

**Why Important:** Contains the Windows Update download cache, update history database, and delivery optimization state.

**⚠️ Size Warning:** DataStore.edb can be 50-500MB.

**Estimated Files:** 10-50 files | **Estimated Size:** 60MB - 600MB

---

### Windows Update - Update Orchestrator and Store

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/ProgramData/UsoPrivate/UpdateStore/*.xml` | 1-5 | 1-10MB each | Update orchestrator store |
| `/ProgramData/USOShared/Logs/*.etl` | 2-10 | 5-50MB each | USO operation logs |
| `/ProgramData/USOShared/*.etl` | 1-5 | 5-20MB each | UUP (Unified Update Platform) logs |

**Why Important:** USO controls update scheduling, download orchestration, and reboot coordination.

**Estimated Files:** 5-20 files | **Estimated Size:** 15MB - 200MB

---

### Windows Update - Update Health Tools

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/ProgramData/Microsoft/UpdateHealthTools/*.log` | 1-5 | 1-10MB each | Update health diagnostics (Win10 2004+) |

**Why Important:** Microsoft's update health monitoring - shows blocked updates and remediation attempts.

**Estimated Files:** 1-5 files | **Estimated Size:** 1MB - 50MB

---

### Windows Update - Delivery Optimization

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `DeliveryOptimization/Logs/*.etl` | 2-10 | 5-20MB each | Peer-to-peer download logs |
| `WSLicense/tokens.dat` | 1 | <1MB | Licensing tokens |

**Why Important:** Delivery Optimization issues can cause download failures - especially in restricted network environments.

**Estimated Files:** 3-11 files | **Estimated Size:** 10MB - 200MB

---

### Windows Update - Event Logs

| Event Log | Typical Size | Purpose |
|-----------|--------------|---------|
| `Microsoft-Windows-WindowsUpdateClient%4Operational.evtx` | 1-20MB | WU client operations |
| `Microsoft-Windows-TaskScheduler%4Operational.evtx` | 5-50MB | Scheduled update tasks |
| `Microsoft-Windows-Bits-Client%4Operational.evtx` | 1-20MB | BITS download operations |
| `Microsoft-Windows-Servicing%4Admin.evtx` | 1-10MB | CBS/servicing events |
| `Microsoft-Windows-CAPI2%4Operational.evtx` | 5-50MB | Certificate/signing issues |
| `*AppX*.evtx` | 1-10MB each | AppX package updates |
| `Microsoft-WS-Licensing%4Admin.evtx` | 1-5MB | Licensing events |
| `Microsoft-Windows-Kernel-PnP%4Configuration.evtx` | 1-10MB | PnP device events |
| `Microsoft-Windows-Store%4Operational.evtx` | 5-20MB | Store update events |
| `Microsoft-Windows-DeliveryOptimization%4Operational.evtx` | 1-20MB | DO events |
| `Microsoft-Windows-WUSA%4Operational.evtx` | 1-5MB | Standalone installer (MSU) |
| `Microsoft-Windows-Kernel-Power%4Operational.evtx` | 5-50MB | Unexpected reboots during updates |
| `Microsoft-Windows-GroupPolicy%4Operational.evtx` | 5-50MB | GP affecting WU settings |

**Why Important:** Comprehensive event coverage for all Windows Update subsystems.

**Estimated Files:** 13-15 files | **Estimated Size:** 30MB - 300MB

---

### Azure Update Manager

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `WindowsPatchExtension/*/*.log` | 2-10 | 1-10MB each | Extension operation logs |
| `WindowsPatchExtension/*/status/*.status` | 1-5 | <100KB each | Status files |
| `WindowsPatchExtension/*/RuntimeSettings/*.settings` | 1-3 | <100KB each | Configuration |
| `WindowsPatchExtension/*/config.txt` | 1 | <10KB | Config |
| `WindowsPatchExtension/*/*.json` | 2 | <50KB each | Handler manifests |

**Why Important:** Required for Azure Update Manager troubleshooting - shows extension-initiated patching operations.

**Estimated Files:** 7-20 files | **Estimated Size:** 5MB - 100MB

---

## Recovery Sections

### Startup Repair

| File | Typical Size | Purpose |
|------|--------------|---------|
| `/Windows/System32/LogFiles/Srt/SrtTrail.txt` | 10KB - 1MB | Startup repair diagnostic trail |
| `/Windows/System32/LogFiles/Srt/*.log` | 1-5MB | Startup repair logs |
| `/Windows/bootstat.dat` | 64KB | Boot status/failure tracking |
| `/Windows/System32/Recovery/ReAgent.xml` | 5KB - 50KB | WinRE configuration |

**Why Important:** When updates cause boot failures, these logs show recovery attempts and boot failure reasons.

**Estimated Files:** 3-5 files | **Estimated Size:** 1MB - 10MB

---

### Windows Error Reporting

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/ProgramData/Microsoft/Windows/WER/ReportArchive/*/*.wer` | 0-50 | 1-100KB each | Archived crash reports |
| `/ProgramData/Microsoft/Windows/WER/ReportQueue/*/*.wer` | 0-20 | 1-100KB each | Pending crash reports |

**Why Important:** Captures crashes that occurred during update installation.

**Estimated Files:** 0-70 files | **Estimated Size:** 1MB - 10MB

---

### Post-Setup Scripts

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/setupcomplete.log` | 0-1 | 1KB - 1MB | Post-setup script output |
| `/Windows/Setup/Scripts/*` | 0-5 | 1KB - 1MB each | Custom setup scripts |

**Why Important:** Custom post-upgrade scripts may fail and cause issues.

**Estimated Files:** 0-6 files | **Estimated Size:** <5MB

---

## OS Upgrade Sections

### OS Upgrade - Compatibility Appraiser

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/appcompat/Programs/Appraiser/*.xml` | 1-5 | 1-10MB each | App compatibility assessment |
| `/Windows/appcompat/Programs/Appraiser/*.bin` | 1-3 | 10-50MB each | Compatibility data |

**Why Important:** Shows what applications/drivers blocked the upgrade.

**Estimated Files:** 2-8 files | **Estimated Size:** 10MB - 100MB

---

### OS Upgrade - Setup API

| File | Typical Size | Purpose |
|------|--------------|---------|
| `/Windows/INF/setupapi.upgrade.log` | 5MB - 100MB | Driver migration during upgrade |

**Why Important:** Driver compatibility is the #1 cause of upgrade failures.

**Estimated Files:** 1 file | **Estimated Size:** 5MB - 100MB

---

### OS Upgrade - MoSetup

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `/Windows/Logs/MoSetup/*.log` | 3-10 | 1-20MB each | Modern Setup orchestrator logs |
| `/Windows/Logs/mosetup/bluebox.log` | 1 | 1-10MB | Feature update orchestration |

**Why Important:** MoSetup orchestrates the entire feature update process.

**Estimated Files:** 4-11 files | **Estimated Size:** 5MB - 100MB

---

### OS Upgrade - Event Logs

| Event Log | Typical Size | Purpose |
|-----------|--------------|---------|
| `Microsoft-Windows-Setup%4Operational.evtx` | 1-20MB | Setup operations |
| `Microsoft-Windows-Upgrade-Diagnostics%4Operational.evtx` | 1-10MB | Upgrade-specific diagnostics |

**Why Important:** Upgrade-specific events with error codes and phase information.

**Estimated Files:** 2 files | **Estimated Size:** 2MB - 30MB

---

### OS Upgrade - Staging Folder ($Windows.~BT)

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `scanresult.xml` | 1 | 100KB - 5MB | Compatibility scan results |
| `CompatData*.xml` | 1-3 | 100KB - 2MB each | Compatibility data |
| `setupact.log` | 1 | 10-100MB | Main setup action log |
| `setuperr.log` | 1 | 1KB - 10MB | Setup errors |
| `miglog.xml` | 1 | 1-50MB | Migration log |
| `PreDownload*.log` | 0-2 | 1-5MB each | Pre-download phase |
| `NewOs*.log` | 0-2 | 1-5MB each | New OS phase |
| `DDACLSys.log` | 0-1 | 1-5MB | Driver compatibility |
| `actionlist.xml` | 0-1 | 100KB - 1MB | Pending actions |

**Why Important:** The **primary diagnostic source** for feature update failures. setupact.log contains the full upgrade sequence.

**Estimated Files:** 7-13 files | **Estimated Size:** 20MB - 200MB

---

### OS Upgrade - Rollback

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `setuperr.log` | 1 | 1KB - 10MB | Rollback errors |
| `diagerr.xml` | 1 | 100KB - 5MB | Diagnostic errors |
| `diagwrn.xml` | 1 | 100KB - 5MB | Diagnostic warnings |
| `setupact.log` | 1 | 1-20MB | Rollback actions |

**Why Important:** When upgrades fail and rollback, these logs explain why.

**Estimated Files:** 4 files | **Estimated Size:** 2MB - 40MB

---

### OS Upgrade - SafeOS Phase

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `SafeOS/Panther/setupact.log` | 1 | 1-20MB | WinRE upgrade phase actions |
| `SafeOS/Panther/setuperr.log` | 1 | 1KB - 5MB | WinRE phase errors |

**Why Important:** SafeOS (WinRE) phase failures are common upgrade blockers.

**Estimated Files:** 2 files | **Estimated Size:** 1MB - 25MB

---

### OS Upgrade - Alternative Staging ($Windows.~WS)

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `setupact.log` | 1 | 1-20MB | Alternative staging actions |
| `setuperr.log` | 1 | 1KB - 5MB | Errors |
| `miglog.xml` | 1 | 1-20MB | Migration log |

**Why Important:** Some upgrades use `$Windows.~WS` instead of `$Windows.~BT`.

**Estimated Files:** 3 files | **Estimated Size:** 3MB - 45MB

---

### OS Upgrade - Setup Cleanup

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `SetupCleanupTask/setupact.log` | 1 | 1-10MB | Post-upgrade cleanup |
| `SetupCleanupTask/setuperr.log` | 1 | 1KB - 1MB | Cleanup errors |

**Why Important:** Cleanup failures can leave the system in a bad state.

**Estimated Files:** 2 files | **Estimated Size:** 1MB - 11MB

---

### OS Upgrade - Previous OS (Windows.old)

| File Pattern | Est. Files | Typical Size | Purpose |
|--------------|------------|--------------|---------|
| `mosetup/bluebox.log` | 1 | 1-10MB | Pre-upgrade orchestration |
| `WindowsUpdate/*.etl` | 1-5 | 5-20MB each | Pre-upgrade WU state |
| `SoftwareDistribution/ReportingEvents.log` | 1 | 1-5MB | Pre-upgrade WU history |
| `USOPrivate/UpdateStore` | 1 | 1-10MB | Pre-upgrade USO state |
| `USOShared/Logs` | 1-5 | 1-10MB each | Pre-upgrade USO logs |
| `Panther/setupact.log` | 1 | 1-50MB | Pre-upgrade setup log |
| `Panther/setuperr.log` | 1 | 1KB - 5MB | Pre-upgrade errors |
| `Panther/miglog.xml` | 1 | 1-20MB | Pre-upgrade migration |

**Why Important:** Contains the state of the system before the upgrade - essential for comparing before/after.

**Estimated Files:** 8-15 files | **Estimated Size:** 15MB - 150MB

---

## Size Summary by Section

| Section | Est. Files | Min Size | Max Size |
|---------|------------|----------|----------|
| Registry Hives | 3 | 60MB | 250MB |
| Event Logs (General) | 3 | 40MB | 275MB |
| Provisioning | 15-20 | 20MB | 150MB |
| CBS and Servicing | 15-40 | 50MB | 500MB |
| WaaS Medic | 1-5 | 1MB | 100MB |
| Setup API (WU) | 1 | 5MB | 50MB |
| Logs and ETL | 5-20 | 20MB | 200MB |
| SoftwareDistribution | 10-50 | 60MB | 600MB |
| Update Orchestrator | 5-20 | 15MB | 200MB |
| Update Health Tools | 1-5 | 1MB | 50MB |
| Delivery Optimization | 3-11 | 10MB | 200MB |
| WU Event Logs | 13-15 | 30MB | 300MB |
| Azure Update Manager | 7-20 | 5MB | 100MB |
| Startup Repair | 3-5 | 1MB | 10MB |
| Windows Error Reporting | 0-70 | 1MB | 10MB |
| Post-Setup Scripts | 0-6 | 0MB | 5MB |
| Compatibility Appraiser | 2-8 | 10MB | 100MB |
| Setup API (Upgrade) | 1 | 5MB | 100MB |
| MoSetup | 4-11 | 5MB | 100MB |
| OS Upgrade Event Logs | 2 | 2MB | 30MB |
| Staging ($Windows.~BT) | 7-13 | 20MB | 200MB |
| Rollback | 4 | 2MB | 40MB |
| SafeOS Phase | 2 | 1MB | 25MB |
| Alt Staging ($Windows.~WS) | 3 | 3MB | 45MB |
| Setup Cleanup | 2 | 1MB | 11MB |
| Previous OS (Windows.old) | 8-15 | 15MB | 150MB |
| **TOTAL** | **115-360** | **~400MB** | **~3.5GB** |

---

## Recommendations

### Size Optimization

1. **CBS Cab Files** - Consider tool enhancement for `latest:3` to limit cab collection
2. **DataStore.edb** - 50-500MB single file; consider making optional
3. **Event Logs** - Generally acceptable sizes
4. **ETL Files** - Binary traces; compress well

### Splitting Recommendations

For smaller packages, consider splitting into:

| Manifest | Contents | Est. Size |
|----------|----------|-----------|
| `windowsupdate-min` | Event logs + CBS logs only | 100-400MB |
| `windowsupdate` | Full WU troubleshooting | 200-800MB |
| `windowsupdate-osupgrade` | OS upgrade specific | 100-500MB |
| `windowsupdate-full` | Everything | 400MB-1.5GB |

