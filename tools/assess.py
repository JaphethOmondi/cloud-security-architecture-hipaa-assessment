#!/usr/bin/env python3
"""Validate data/findings.yaml and generate the docs/ markdown + CSV exports.

Usage:
    python tools/assess.py            # validate, print summary, regenerate docs
    python tools/assess.py --check    # validate only (used in CI); non-zero exit on error
"""
import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "findings.yaml"
DOCS = ROOT / "docs"
SCORES = {"implemented": 1.0, "partial": 0.5, "missing": 0.0}
LABEL = {"implemented": "Implemented", "partial": "Incomplete", "missing": "Missing"}
PRIORITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
HEADER = "> Generated from `data/findings.yaml` by `tools/assess.py`. Do not edit by hand.\n\n"


def load():
    with DATA.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate(d):
    errors = []
    rec_ids = {r["id"] for r in d["recommendations"]}
    prac_ids = {p["id"] for p in d["practices"]}
    for p in d["practices"]:
        if p["status"] not in SCORES:
            errors.append(f"{p['id']}: invalid status '{p['status']}'")
        if p["evidence"] not in {"stated", "assumed"}:
            errors.append(f"{p['id']}: evidence must be stated|assumed")
        if p["status"] != "implemented" and p.get("recommendation") not in rec_ids:
            errors.append(f"{p['id']}: gap has no valid recommendation")
    for r in d["recommendations"]:
        if r["priority"] not in PRIORITY_ORDER:
            errors.append(f"{r['id']}: invalid priority")
        for a in r["addresses"]:
            if a not in prac_ids:
                errors.append(f"{r['id']}: unknown practice {a}")
    return errors


def esc(s):
    return str(s).replace("|", "\\|")


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def score(d):
    ps = d["practices"]
    return sum(SCORES[p["status"]] for p in ps) / len(ps) * 100


def write(name, text):
    DOCS.mkdir(exist_ok=True)
    (DOCS / name).write_text(text, encoding="utf-8")


def render(d):
    write("01-shared-responsibility.md",
          "# Shared Responsibility Analysis\n\n" + HEADER
          + table(["Component", "Cloud Provider", "Healthcare Organization"],
                  [[r["component"], r["provider"], r["organization"]] for r in d["shared_responsibility"]]))

    rows = [[p["id"], p["name"], LABEL[p["status"]], p["evidence"], p["gap"], p["impact"]] for p in d["practices"]]
    write("02-best-practices-checklist.md",
          "# Best Practices Checklist\n\n" + HEADER
          + f"**Posture score: {score(d):.0f}%** (Implemented = 1, Incomplete = 0.5, Missing = 0)\n\n"
          "`evidence: assumed` means the scenario did not state it; the finding rests on absence of evidence "
          "and should be validated in a real engagement.\n\n"
          + table(["ID", "Best practice", "Status", "Evidence", "Gap", "Impact"], rows))

    write("03-hipaa-mapping.md",
          "# HIPAA Security Rule Mapping\n\n" + HEADER
          + table(["Safeguard", "Requirement", "Citation", "Current practice", "Action needed", "Evidence"],
                  [[h["type"], h["requirement"], h["cite"], h["current"], h["action"], h["evidence"]]
                   for h in d["hipaa"]]))

    recs = sorted(d["recommendations"], key=lambda r: (PRIORITY_ORDER[r["priority"]], r["target_days"]))
    write("04-recommendations.md",
          "# Recommendations and Roadmap\n\n" + HEADER
          + table(["ID", "Priority", "Target (days)", "Recommendation", "HIPAA ref", "Addresses", "Rationale"],
                  [[r["id"], r["priority"], r["target_days"], r["title"], r["refs"],
                    ", ".join(r["addresses"]) or "HIPAA gap", r["rationale"]] for r in recs]))

    (ROOT / "reports").mkdir(exist_ok=True)
    with (ROOT / "reports" / "practices.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "practice", "status", "evidence", "gap", "impact", "recommendation"])
        for p in d["practices"]:
            w.writerow([p["id"], p["name"], p["status"], p["evidence"], p["gap"], p["impact"], p["recommendation"]])


def main():
    d = load()
    errors = validate(d)
    if errors:
        print("Validation failed:\n  " + "\n  ".join(errors))
        sys.exit(1)
    counts = {s: sum(p["status"] == s for p in d["practices"]) for s in SCORES}
    print(f"Practices: {counts} | posture score {score(d):.0f}%")
    if "--check" in sys.argv:
        print("OK")
        return
    render(d)
    print("Docs regenerated in docs/ and reports/practices.csv")


if __name__ == "__main__":
    main()
