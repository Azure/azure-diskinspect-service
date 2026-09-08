# Windows Guest Agent and Extension Manifests

| Manifest | Area | Description | PII Risk |
|----------|------|-------------|----------|
| `diagnostic-guest-agent-core` | Guest agent | WaAppAgent, TransparentInstaller, aggregate status, telemetry | Low |
| `diagnostic-extensions-core` | Extensions | Generic plugin command/install/update/heartbeat/state files | Medium |
| `diagnostic-extensions-azure` | Extensions | Azure extension-specific diagnostics, Key Vault, VMAccess, DSC, monitoring, security, backup files | Medium |
| `diagnostic-extensions-aadlogin` | Extensions | AADLoginForWindows logs | Medium |
| `diagnostic-extensions-servicefabric` | Extensions | Service Fabric extension manifests and logs | Medium |
| `diagnostic-extensions-thirdparty` | Extensions | Symantec, TrendMicro, ESET extension logs/files | Medium |
| `diagnostic-proxyagent` | Guest agent | Guest ProxyAgent and eBPF logs | Low |
