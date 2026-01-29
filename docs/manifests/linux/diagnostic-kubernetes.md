# Kubernetes and AKS Diagnostic Manifests

Modular manifests for Kubernetes and AKS node troubleshooting.

## General Kubernetes

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-kubernetes-common` | kubelet, containerd, pod logs | **Medium** |

## AKS-Specific Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-probing-aks` | AKS directory listings | None |
| `diagnostic-provision-aks` | Cluster provisioning scripts | Low |
| `diagnostic-kubernetes-aks` | kubelet, containerd, journal logs | **Medium** |
| `diagnostic-pods-aks` | kube-system, calico, tigera pod logs | **Medium** |
| `diagnostic-networking-aks` | CNI, VNET, IPAM, CNS, NPM logs | None |

## Issue Type Selection

### General AKS Issues
```
diagnostic-probing-aks
diagnostic-provision-aks
diagnostic-kubernetes-aks
diagnostic-pods-aks
diagnostic-networking-aks
```

### AKS Node Provisioning Issues
```
diagnostic-probing-aks
diagnostic-provision-aks
diagnostic-cloudinit-common
diagnostic-azure-agent-logs
```

### AKS Networking Issues
```
diagnostic-networking-aks
diagnostic-pods-aks
diagnostic-netconfig-<distro>
diagnostic-dns-common
```

### Kubelet Issues
```
diagnostic-kubernetes-aks
diagnostic-syslog-common
diagnostic-kernlog-common
```

### Pod Scheduling Issues
```
diagnostic-pods-aks
diagnostic-kubernetes-aks
diagnostic-syslog-common
```

### Container Runtime Issues
```
diagnostic-kubernetes-aks
diagnostic-kernlog-common
diagnostic-syslog-common
```

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-kubernetes-common | 5-50 MB |
| diagnostic-probing-aks | < 100 KB |
| diagnostic-provision-aks | 1-5 MB |
| diagnostic-kubernetes-aks | 5-50 MB |
| diagnostic-pods-aks | 5-50 MB |
| diagnostic-networking-aks | 1-10 MB |

