# Best Practices Checklist

> Generated from `data/findings.yaml` by `tools/assess.py`. Do not edit by hand.

**Posture score: 31%** (Implemented = 1, Incomplete = 0.5, Missing = 0)

`evidence: assumed` means the scenario did not state it; the finding rests on absence of evidence and should be validated in a real engagement.

| ID | Best practice | Status | Evidence | Gap | Impact |
|---|---|---|---|---|---|
| P1 | Data encryption at rest and in transit | Incomplete | stated | Cloud data is encrypted at rest and in transit, but cloud-stored backups are not encrypted. | A compromise of backup storage exposes unencrypted PHI and could constitute a reportable breach. |
| P2 | Centralized key management | Missing | stated | On-premises and cloud keys are managed in separate systems with no central control. | Complicates rotation, revocation, and auditing of key use; raises key-exposure risk. |
| P3 | Multi-factor authentication (MFA) | Missing | assumed | No MFA is described for cloud or on-premises access. | Stolen or guessed credentials alone grant access to ePHI (164.312(d) person/entity authentication). |
| P4 | Principle of least privilege | Incomplete | stated | Roles are manually managed, with no deactivation lifecycle and no periodic access reviews. | Dormant and over-privileged accounts persist and widen the attack surface. |
| P5 | Automated monitoring, logging, and alerting | Incomplete | stated | Provider monitoring exists, but hybrid logs are not centralized. | Cross-environment attacks (e.g. on-prem to cloud lateral movement) go undetected; audit controls weakened. |
| P6 | Network segmentation | Incomplete | stated | Cloud VMs are internet-exposed for admin (IP-restricted); on-prem firewalls are outdated, with no deep packet inspection. | Persistent exposed admin surface; encrypted threats pass the perimeter uninspected. |
| P7 | Regular vulnerability assessments | Missing | assumed | No vulnerability assessment program is described. | Unpatched systems and misconfigurations persist; weakens risk management under 164.308(a)(1). |
| P8 | Documented and tested disaster recovery plans | Incomplete | stated | Backups exist, but IR/DR plans do not account for hybrid cloud risks and are not documented or tested. | Recovery may fail during a real incident, causing downtime and data loss (164.308(a)(7)). |
