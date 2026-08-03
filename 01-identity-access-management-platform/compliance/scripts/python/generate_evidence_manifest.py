#!/usr/bin/env python3
"""Generate a SHA-256 evidence manifest for a directory."""
from __future__ import annotations
import argparse
import csv
import hashlib
from pathlib import Path
from datetime import datetime, timezone

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_dir", type=Path)
    parser.add_argument("--output", type=Path, default=Path("evidence-hashes.csv"))
    args = parser.parse_args()

    if not args.evidence_dir.is_dir():
        raise SystemExit(f"Not a directory: {args.evidence_dir}")

    rows = []
    for path in sorted(p for p in args.evidence_dir.rglob("*") if p.is_file()):
        if path.resolve() == args.output.resolve():
            continue
        rows.append({
            "file": str(path.relative_to(args.evidence_dir)),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
            "collected_at_utc": datetime.now(timezone.utc).isoformat()
        })

    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file","sha256","bytes","collected_at_utc"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} records to {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
