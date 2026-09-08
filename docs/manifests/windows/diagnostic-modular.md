# Windows Diagnostic Manifests - Modular Reference

This document provides an overview of modular Windows diagnostic manifests for the Azure Disk Inspect Service.

The split is domain-based, not a literal copy of the current `diagnostic` section headers. That matters because the existing Windows manifest has broad headers and mixed sections: for example, the later `Plug and Play` block is FSLogix, and the `MSRDCollect` block includes RDInfra, identity, AppX/system, RDP, device-management, and PowerShell event logs.

## Naming Convention

**Format:** `diagnostic-<domain>-<subdomain>`

- Domain-first names group manifests by troubleshooting intent.
- Workload-specific modules use the workload name, for example `diagnostic-fslogix`.
- `diagnostic-wga-gap-closure` is intentionally an add-on for `min-diagnostic`, not part of the full-diagnostic lossless split.

## Quick Reference

| Manifest | Area | Description | PII Risk |
|----------|------|-------------|----------|
| `diagnostic-registry-core` | Core | SOFTWARE/SYSTEM hives and transaction logs | Medium |
| `diagnostic-events-core` | Events | System, Application, Windows Azure, Security, Setup | Medium |
| `diagnostic-events-rdp` | Events | RDP, Remote Desktop Services, Terminal Services | Medium |
| `diagnostic-events-network-security` | Events | Network, SMB, Schannel, firewall, OpenSSH, NTLM | Medium |
| `diagnostic-events-directory-services` | Events | AD DS, DFS, DNS Server, DNS Client | Medium |
| `diagnostic-events-identity` | Events | AAD, Hello for Business, Group Policy, Kerberos, SmartCard, Workplace Join | Medium |
| `diagnostic-events-system-services` | Events | AppX/AppLocker, PowerShell, WMI, Task Scheduler, WER, Winlogon, device management | Medium |
| `diagnostic-events-storage` | Events | NTFS and VHDMP operational logs | Medium |
| `diagnostic-events-azure` | Events | Azure Guest Agent, Azure Status, ASR, Service Fabric event logs | Low |
| `diagnostic-provisioning` | Provisioning | CustomData, Panther, WaSetup, unattend, sysprep, setup logs | Medium |
| `diagnostic-pnp-appinstall` | Provisioning | setupapi, netcfg ETL, app install setupapi | Low |
| `diagnostic-domainjoin` | Domain | NetSetup, DCPROMO, netlogon, domain join debug logs | Medium |
| `diagnostic-dotnet` | Core | .NET machine.config files | Low |
| `diagnostic-guest-agent-core` | Guest agent | WaAppAgent, TransparentInstaller, aggregate status, telemetry | Low |
| `diagnostic-extensions-core` | Extensions | Generic plugin command/install/update/heartbeat/state files | Medium |
| `diagnostic-extensions-azure` | Extensions | Azure extension-specific diagnostics, Key Vault, VMAccess, DSC, monitoring, security, backup files | Medium |
| `diagnostic-extensions-aadlogin` | Extensions | AADLoginForWindows logs | Medium |
| `diagnostic-extensions-servicefabric` | Extensions | Service Fabric extension manifests and logs | Medium |
| `diagnostic-extensions-thirdparty` | Extensions | Symantec, TrendMicro, ESET extension logs/files | Medium |
| `diagnostic-windows-update` | Update | Servicing sessions, CBS, DISM, WindowsUpdate, WindowsUpdateClient event log | Medium |
| `diagnostic-proxyagent` | Guest agent | Guest ProxyAgent and eBPF logs | Low |
| `diagnostic-avd-rdinfra` | Workloads | Azure Virtual Desktop/RDInfra/MSRDC logs and probes | Medium |
| `diagnostic-msrdcollect` | Workloads | tssesdir XML files used by MSRDCollect scenarios | Medium |
| `diagnostic-fslogix` | Workloads | FSLogix logs, rules, and event logs | Medium |
| `diagnostic-arc` | Workloads | Azure Connected Machine Agent and Guest Configuration logs | Medium |
| `diagnostic-blobfuse` | Workloads | BlobFuse logs | Medium |
| `diagnostic-hpc` | Workloads | HPC/NVIDIA/HPCSetup logs and HPC event logs | Medium |
| `diagnostic-hpc-pack-2019` | Workloads | HPC Pack 2019 directory probes | None |
| `diagnostic-hpc-pack-2016` | Workloads | HPC Pack 2016 directory probes | None |
| `diagnostic-diskinfo` | Core | Disk and partition inventory | None |
| `diagnostic-misc` | Core | ScriptLog and Windows IME directory probes that do not fit a larger domain module | Low |
| `diagnostic-wga-gap-closure` | WGA | Targeted add-on for known min-diagnostic WGA gaps | Medium |


## Selection by Issue Type

### Cannot RDP / Terminal Services
```
diagnostic-registry-core
diagnostic-events-core
diagnostic-events-rdp
diagnostic-events-network-security
diagnostic-guest-agent-core
diagnostic-diskinfo
```

### Windows Guest Agent or WireServer
```
diagnostic-registry-core
diagnostic-events-core
diagnostic-events-azure
diagnostic-guest-agent-core
diagnostic-extensions-core
diagnostic-provisioning
diagnostic-proxyagent
diagnostic-diskinfo
```

### Extension failure
```
diagnostic-registry-core
diagnostic-guest-agent-core
diagnostic-extensions-core
diagnostic-extensions-azure
```

Add specific extension modules when applicable:
```
diagnostic-extensions-aadlogin
diagnostic-extensions-servicefabric
diagnostic-extensions-thirdparty
```

### Windows Update or in-place upgrade
```
diagnostic-registry-core
diagnostic-events-core
diagnostic-windows-update
diagnostic-provisioning
diagnostic-pnp-appinstall
diagnostic-diskinfo
```

### Domain join, domain trust, or domain controller promotion
```
diagnostic-registry-core
diagnostic-events-core
diagnostic-events-directory-services
diagnostic-events-identity
diagnostic-domainjoin
diagnostic-provisioning
```

### Networking, firewall, SMB, WinRM, or OpenSSH
```
diagnostic-registry-core
diagnostic-events-core
diagnostic-events-network-security
diagnostic-proxyagent
```

### Azure Virtual Desktop / FSLogix
```
diagnostic-events-rdp
diagnostic-avd-rdinfra
diagnostic-fslogix
```

### Azure Arc / Guest Configuration
```
diagnostic-events-identity
diagnostic-arc
```

### HPC Pack
```
diagnostic-hpc
diagnostic-hpc-pack-2019
# or
diagnostic-hpc-pack-2016
```

### Starting from `min-diagnostic` for Windows Guest Analyzer coverage
```
diagnostic-wga-gap-closure
```

The full set of Windows modules, excluding `diagnostic-wga-gap-closure`, is a lossless partition of the existing Windows `diagnostic` manifest operations.
