# Azure Agent Diagnostic Manifests

Modular manifests for Azure Linux Agent (waagent) diagnostics.

## Available Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-azure-agent-probing` | Directory listings for /var/log and /var/lib/waagent | None |
| `diagnostic-azure-agent-config` | waagent.conf configuration | None |
| `diagnostic-azure-agent-logs` | waagent log files | Low |
| `diagnostic-azure-agent-state` | Agent state, status, incarnation, history | None |
| `diagnostic-azure-agent-xml` | SharedConfig, GoalState, ExtensionsConfig XML | Low |
| `diagnostic-azure-agent-identity` | ManagedIdentity JSON files | **Medium** |
| `diagnostic-azure-agent-proxyagent` | Guest ProxyAgent logs | Low |

## Issue Type Selection

### General Azure Agent Issues
```
diagnostic-azure-agent-probing
diagnostic-azure-agent-config
diagnostic-azure-agent-logs
diagnostic-azure-agent-state
diagnostic-azure-agent-xml
```

### Managed Identity Issues
```
diagnostic-azure-agent-identity
diagnostic-azure-agent-logs
diagnostic-azure-agent-state
```

### ProxyAgent Issues
```
diagnostic-azure-agent-proxyagent
diagnostic-azure-agent-logs
```

### Provisioning Issues
```
diagnostic-azure-agent-probing
diagnostic-azure-agent-config
diagnostic-azure-agent-logs
diagnostic-azure-agent-state
diagnostic-azure-agent-xml
diagnostic-cloudinit-common
```

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-azure-agent-probing | < 50 KB |
| diagnostic-azure-agent-config | < 10 KB |
| diagnostic-azure-agent-logs | 1-50 MB |
| diagnostic-azure-agent-state | < 5 MB |
| diagnostic-azure-agent-xml | 100 KB - 5 MB |
| diagnostic-azure-agent-identity | < 100 KB |
| diagnostic-azure-agent-proxyagent | 1-10 MB |

