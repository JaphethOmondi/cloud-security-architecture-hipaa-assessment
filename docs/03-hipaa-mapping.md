# HIPAA Security Rule Mapping

> Generated from `data/findings.yaml` by `tools/assess.py`. Do not edit by hand.

| Safeguard | Requirement | Citation | Current practice | Action needed | Evidence |
|---|---|---|---|---|---|
| Administrative | Security Management Process | 164.308(a)(1) | No periodic access reviews, no account lifecycle policy, no documented risk analysis. | Conduct formal risk analysis; document policies; implement access reviews and lifecycle policy. | assumed |
| Administrative | Assigned Security Responsibility | 164.308(a)(2) | Security duties appear informally distributed. | Designate a Security Officer; document roles and accountability. | assumed |
| Administrative | Workforce Security | 164.308(a)(3) | Manual role management; no deactivation lifecycle; no access reviews. | Automate provisioning/deprovisioning; quarterly reviews; role recertification. | stated |
| Administrative | Information Access Management | 164.308(a)(4) | PHI access not strictly role-governed; no MFA or central logging. | MFA, minimum-necessary RBAC, centralized access auditing. | assumed |
| Administrative | Security Awareness and Training | 164.308(a)(5) | No training program described. | Mandatory training with phishing simulation; document completion. | assumed |
| Administrative | Security Incident Procedures | 164.308(a)(6) | IR plans ignore hybrid cloud risks; no central logging. | Update IR plans; integrate logs into SIEM; quarterly tabletop exercises. | stated |
| Administrative | Contingency Plan | 164.308(a)(7) | Backups unencrypted; DR plans undocumented and untested. | Encrypt backups; document DR; define RTO/RPO; test annually. | stated |
| Administrative | Evaluation | 164.308(a)(8) | No periodic evaluations described. | Recurring evaluation schedule with documented remediation. | assumed |
| Physical | Facility Access Controls | 164.310(a)(1) | Provider covers its data centers; on-prem physical security assumed org-managed. | Verify on-prem physical access controls via periodic audits. | assumed |
| Physical | Workstation Security | 164.310(b) | Not described. | Document policy; screen locks; local-storage encryption. | assumed |
| Technical | Access Control | 164.312(a) | Data encrypted but keys fragmented; no MFA. | MFA; central KMS/HSM; automatic logoff. | stated |
| Technical | Audit Controls | 164.312(b) | Cloud logging not centralized or correlated with on-prem. | Central SIEM; automated alerting; defined log retention. | stated |
| Technical | Integrity | 164.312(c)(1) | No ePHI integrity mechanisms described. | File integrity monitoring; checksums/signatures; restrict write access. | assumed |
| Technical | Person or Entity Authentication | 164.312(d) | Single-factor credentials assumed. | MFA; strong password policy; PAM for admins. | assumed |
| Technical | Transmission Security | 164.312(e) | TLS in cloud; on-prem transmission security not described. | Verify TLS/IPsec on internal PHI traffic; retire vulnerable protocols. | stated |
