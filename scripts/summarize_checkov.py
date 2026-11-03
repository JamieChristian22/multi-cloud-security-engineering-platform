#!/usr/bin/env python3
"""Count actual Checkov IaC findings without converting warnings into a security pass."""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path

def summarize(raw):
    entries = raw if isinstance(raw, list) else [raw]
    checks = 0
    failures = 0
    passed = 0
    severity_counts = Counter()
    for item in entries:
        if not isinstance(item, dict) or not isinstance(item.get("results"), dict):
            raise ValueError("Unexpected Checkov output: expected results object")
        results = item["results"]
        bad = results.get("failed_checks")
        good = results.get("passed_checks")
        if not isinstance(bad, list) or not isinstance(good, list):
            raise ValueError("Unexpected Checkov result lists")
        failures += len(bad)
        passed += len(good)
        checks += len(bad) + len(good)
        for finding in bad:
            severity_counts[str(finding.get("severity") or "UNSPECIFIED").upper()] += 1
    return {
        "status": "ADVISORY_FINDINGS_REPORTED",
        "scope": "Checkov static IaC checks; does not establish live security posture or absence of vulnerabilities",
        "checks_evaluated": checks,
        "passed_checks": passed,
        "failed_checks": failures,
        "failed_by_severity": dict(severity_counts),
        "all_policy_checks_pass": failures == 0,
        "blocking_ci_gate": False,
        "next_action": "Review each finding, remediate genuine risks and justify accepted exceptions before promoting this IaC.",
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = summarize(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
