#!/usr/bin/env python3
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[2]

required = [
    "README.md",
    "cross-cloud/control-mappings/control-matrix.csv",
    "cross-cloud/risk-register/risk-register.csv",
    "cross-cloud/audit/control-status.csv",
    "runbooks/credential-compromise.md",
    "terraform/aws/main.tf",
    "terraform/azure/main.tf",
    "terraform/gcp/main.tf",
]

missing = [p for p in required if not (ROOT / p).exists()]
invalid = []
for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        invalid.append(f"{path}: {exc}")

if missing or invalid:
    print("Validation failed")
    for item in missing:
        print(f"Missing: {item}")
    for item in invalid:
        print(f"Invalid JSON: {item}")
    sys.exit(1)

print("Repository validation passed")
