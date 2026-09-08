# diagnostic-hpc-common Manifest Documentation

## Summary

| Attribute | Value |
|-----------|-------|
| **Manifest** | `diagnostic-hpc-common` |
| **Platform** | Linux (All Distributions) |
| **Purpose** | Collect HPC (High Performance Computing) diagnostic data |
| **Total Items** | ~45 entries |
| **Estimated Size** | 5-50 MB (varies with HPC workload) |

## Description

This manifest collects diagnostic data specific to High Performance Computing (HPC) environments on Azure, including GPU/NVIDIA drivers, job schedulers (Slurm, PBS, SGE), and InfiniBand networking status. This is a modular manifest designed to be combined with distro-specific manifests.

## Sections

### Probing HPC Directories
| Path | Type | X |
|------|------|---|
| `/sys/class/infiniband/` | ll | |
| `/sched/sge/` | ll | |
| `/var/log/slurmctld/` | ll | |
| `/var/log/slurmd/` | ll | |
| `/var/spool/pbs/` | ll | |

### NVIDIA/CUDA Installer Logs
| Path | Type | X |
|------|------|---|
| `/var/log/cuda-installer.log` | copy | |
| `/var/log/nvidia-installer.log` | copy | |

### Slurm Files
| Path | Type | X |
|------|------|---|
| `/etc/slurm/*` | copy | |
| `/var/log/slurmctld/slurmctld.log` | copy | X |
| `/var/log/slurmd/slurmd.log` | copy | X |

### PBS Files
| Path | Type | X |
|------|------|---|
| `/etc/pbs.conf` | copy | |
| `/var/spool/pbs/mom_logs/*` | copy | X |
| `/var/spool/pbs/sched_logs/*` | copy | X |

### SGE Files
| Path | Type | X |
|------|------|---|
| `/sched/sge/sge-2011.11/default/common/install_logs/*` | copy | |
| `/sched/sge/sge-2011.11/default/spool/*` | copy | X |

### System Limits
| Path | Type | X |
|------|------|---|
| `/etc/security/limits.conf` | copy,noscan | |

### InfiniBand State
| Path | Type | X |
|------|------|---|
| `/sys/class/infiniband/mlx5_ib[0-7]/ports/1/state` | copy,noscan | |
| `/sys/class/infiniband/mlx5_ib[0-7]/ports/1/rate` | copy,noscan | |
| `/sys/class/infiniband/mlx5_ib[0-7]/ports/1/phys_state` | copy,noscan | |
| `/sys/class/infiniband/mlx5_ib[0-7]/ports/1/pkeys` | copy,noscan | |

*Note: InfiniBand entries cover 8 adapters (mlx5_ib0 through mlx5_ib7) with 4 attributes each (32 total sysfs entries)*

## PII Indicators

| Symbol | Meaning |
|--------|---------|
| X | May contain PII (job names, usernames, hostnames) |
| (blank) | No PII expected |

## Usage Notes

- **Modular Design**: Combine with distro-specific manifests (e.g., `diagnostic-ubuntu` + `diagnostic-hpc`)
- **HPC VMs**: Primarily useful for H-series and N-series VMs with InfiniBand or GPU
- **Extension Logs**: For HPC extension logs (`/var/log/azure/ib-vmext-status/`, `/var/log/azure/nvidia-vmext-status/`), use the `azure-extensions` manifest
- **InfiniBand**: The 8 adapter entries (mlx5_ib0-7) cover most Azure HB/HC/NDv2/NDv4 configurations

## Potentially Missing Items

| Path | Description |
|------|-------------|
| `/var/log/mlnx_*` | Mellanox driver logs |
| `/etc/libibverbs.d/*` | InfiniBand verbs configuration |
| `/etc/rdma/*` | RDMA configuration files |
| `/var/log/nvidia-smi.log` | NVIDIA SMI output logs |
| `/etc/nvidia/*` | NVIDIA configuration files |
| `/var/log/dcgm/*` | NVIDIA Data Center GPU Manager logs |
| `/opt/intel/mpi/*/etc/*` | Intel MPI configuration |
| `/etc/openmpi/*` | OpenMPI configuration |
| `/var/spool/slurm/*` | Slurm spool files |
| `/etc/munge/*` | MUNGE authentication for Slurm |
