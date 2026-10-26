# Recommendations and Roadmap

> Generated from `data/findings.yaml` by `tools/assess.py`. Do not edit by hand.

| ID | Priority | Target (days) | Recommendation | HIPAA ref | Addresses | Rationale |
|---|---|---|---|---|---|---|
| R1 | Critical | 30 | Implement MFA for all accounts | 164.312(d) | P3 | Prefer TOTP or hardware tokens over SMS; enforce via conditional access. |
| R3 | Critical | 30 | Encrypt all backups before cloud storage (AES-256) | 164.312(a); 164.308(a)(7) | P1 | Protects PHI even if storage credentials are compromised; keys managed in central KMS. |
| R2 | High | 60 | Centralize encryption key management (KMS/HSM) | 164.312(a) | P2 | Enables unified rotation, revocation, and key-usage audit trail. |
| R5 | High | 60 | Establish a vulnerability management program | 164.308(a)(1) | P7 | Quarterly scans, annual third-party pen test, patch SLAs (Critical 72h / High 7d / Medium 30d). |
| R4 | High | 90 | Deploy a centralized SIEM | 164.312(b); 164.308(a)(6) | P5 | Correlate hybrid logs; alert on anomalous access and exfiltration. |
| R6 | High | 90 | Upgrade on-prem firewalls (NGFW) and segment the network | 164.312(a); 164.312(e) | P6 | Isolate PHI systems; replace internet-exposed admin with bastion host or VPN. |
| R9 | Medium | 45 | Security awareness and training program | 164.308(a)(5) | HIPAA gap | Recurring training and phishing simulation; keep completion records for audits. |
| R7 | Medium | 60 | Document and test hybrid DR plans | 164.308(a)(7) | P8 | Define RTO/RPO; quarterly tabletops; annual full recovery test. |
| R8 | Medium | 90 | Automate account lifecycle and access reviews (IGA) | 164.308(a)(3); 164.308(a)(4) | P4 | Quarterly attestation; auto-revoke dormant privileges. |
| R10 | Medium | 90 | File integrity monitoring on PHI systems | 164.312(c)(1) | HIPAA gap | Detect unauthorized change to ePHI and configs; feed alerts to the SIEM. |
