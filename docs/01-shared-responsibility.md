# Shared Responsibility Analysis

> Generated from `data/findings.yaml` by `tools/assess.py`. Do not edit by hand.

| Component | Cloud Provider | Healthcare Organization |
|---|---|---|
| Data Encryption | Provides encryption-at-rest capabilities for cloud storage and TLS for data in transit across the provider network. | Manages keys for on-premises and cloud; defines rotation policy; classifies data; verifies cloud backups are encrypted. |
| Access Control | Provides IAM tooling, RBAC frameworks, and APIs for provisioning. | Defines and enforces roles; implements MFA; runs periodic access reviews; sets account lifecycle policy incl. deactivation. |
| Monitoring and Incident Response | Maintains cloud-native logging, infrastructure monitoring dashboards, and physical security event logging. | Integrates hybrid logs into a central system; configures alerting; builds and tests IR plans covering hybrid-specific risks. |
| Network Security | Secures physical network layers and backbone routing; provides virtual isolation primitives (security groups, VPCs). | Configures security group rules; segments on-prem from cloud; restricts admin access; upgrades on-prem firewalls. |
| Backup and Recovery | Offers automated backup services, geo-redundant storage, and backup infrastructure availability. | Tests and documents DR plans; encrypts backups before storage; validates integrity; defines RTO/RPO. |
