# Hybrid Cloud Security Architecture & HIPAA Assessment

A security assessment of a fictional healthcare organization running a hybrid (on-premises + cloud)
environment that processes Protected Health Information (PHI).

**Author:** Japheth Omondi · **Date:** June 2026

## What this project does

1. Maps **shared responsibility** between the cloud provider and the organization
2. Assesses **8 cloud security best practices** (Implemented / Incomplete / Missing)
3. Maps current practices to the **HIPAA Security Rule** administrative, physical, and technical safeguards
4. Produces a **prioritized, time-boxed remediation roadmap** (10 recommendations)

## Key findings

- **0 of 8** best practices fully implemented, **5 incomplete**, **3 missing** (posture score about 31%)
- Highest-risk gaps: no MFA, unencrypted cloud backups, fragmented key management
- Top 30-day actions: MFA for all accounts and AES-256 encryption of backups

| Priority | Actions |
|---|---|
| Critical (30 days) | MFA, backup encryption |
| High (60-90 days) | Central KMS/HSM, vulnerability management, SIEM, NGFW + segmentation |
| Medium (45-90 days) | DR testing, access lifecycle (IGA), awareness training, file integrity monitoring |

## Repository layout

```
data/findings.yaml      Single source of truth (practices, HIPAA map, recommendations)
tools/assess.py         Validates the data and generates the docs + CSV
docs/                   00 architecture · 01 shared responsibility · 02 checklist · 03 HIPAA map · 04 roadmap
reports/                Final PDF report and practices.csv export
.github/workflows/      CI: validates findings and checks docs are in sync
```

## Usage

```bash
pip install -r requirements.txt
python tools/assess.py          # validate and regenerate docs/
python tools/assess.py --check  # validate only
```

To reuse for another environment, edit `data/findings.yaml` and rerun the script.

## Method and limitations

- Each finding is tagged `evidence: stated` (given in the lab scenario) or `assumed` (inferred from absence,
  e.g. no MFA or vulnerability program mentioned). Assumed items would need validation in a real engagement.
- HIPAA marks some specifications as *addressable* rather than required, and the Security Rule does not name
  MFA specifically; MFA is presented here as the standard means of meeting 164.312(d).
- This is a coursework exercise on a fictional scenario, not legal or compliance advice.

## Frameworks referenced

HIPAA Security Rule (45 CFR 164.308, 164.310, 164.312) · Shared Responsibility Model

## License

MIT
