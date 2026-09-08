# HPC Diagnostic Manifests

Modular manifests for High Performance Computing troubleshooting.

## Available Manifests

| Manifest | Description | PII Risk |
|----------|-------------|----------|
| `diagnostic-hpc-common` | InfiniBand, Slurm, PBS, SGE, NVIDIA | **Medium** |

## Contents

The `diagnostic-hpc-common` manifest collects:

### InfiniBand
- `/sys/class/infiniband/` directory listing
- mlx5_ib0-7 port state, rate, phys_state, pkeys

### Job Schedulers
- Slurm: `/etc/slurm/*`, slurmctld.log, slurmd.log
- PBS: `/etc/pbs.conf`, mom_logs, sched_logs
- SGE: install_logs, spool files

### GPU/NVIDIA
- `/var/log/cuda-installer.log`
- `/var/log/nvidia-installer.log`

### System Limits
- `/etc/security/limits.conf`

## Issue Type Selection

### InfiniBand Connectivity
```
diagnostic-hpc-common
diagnostic-kernlog-common
diagnostic-udev-common
```

### GPU/NVIDIA Issues
```
diagnostic-hpc-common
diagnostic-kernlog-common
diagnostic-syslog-common
```

### Slurm Job Failures
```
diagnostic-hpc-common
diagnostic-syslog-common
diagnostic-authlog-common
```

### PBS/SGE Issues
```
diagnostic-hpc-common
diagnostic-syslog-common
```

## Estimated Sizes

| Manifest | Size Range |
|----------|------------|
| diagnostic-hpc-common | 5-50 MB |

## Azure VM Series

This manifest is primarily useful for:
- H-series (HB, HC, HBv2, HBv3, HBv4)
- N-series (NC, ND, NV)
- VMs with InfiniBand or GPU

