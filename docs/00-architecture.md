# Current vs Target Architecture

## Current state

```mermaid
flowchart LR
  subgraph ONPREM[On-premises]
    A[PHI systems] --> FW[Outdated firewall<br/>no DPI]
    K1[Key system A]
  end
  subgraph CLOUD[Cloud provider]
    VM[Admin-exposed VMs<br/>IP-restricted]
    BK[(Unencrypted backups)]
    K2[Key system B]
    LG[Native logs only]
  end
  FW --- VM
  A -. backups .-> BK
```

## Target state

NGFW + segmentation, bastion/VPN for admin, one KMS/HSM for all keys, encrypted backups,
MFA everywhere, and a single SIEM ingesting on-prem, cloud, and identity logs.

```mermaid
flowchart LR
  subgraph ONPREM[On-premises]
    A[PHI segment] --> NG[NGFW + DPI]
  end
  subgraph CLOUD[Cloud provider]
    VPC[PHI VPC] --- BH[Bastion / VPN]
    BK[(AES-256 backups)]
  end
  NG --- BH
  KMS[Central KMS / HSM] --> A
  KMS --> BK
  IDP[IdP + MFA + IGA] --> A
  IDP --> VPC
  A --> SIEM[(Central SIEM)]
  VPC --> SIEM
  IDP --> SIEM
```
