"""Verify offline posture explorer against the checked-in illustrative evidence."""
import csv
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPLIANCE = ROOT / "01-identity-access-management-platform/compliance"
HTML = ROOT / "demo/multicloud-posture.html"
FILES = {
    "controls": "cross-cloud/audit/control-status.csv",
    "mappings": "cross-cloud/control-mappings/control-matrix.csv",
    "risks": "cross-cloud/risk-register/risk-register.csv",
}

def payload():
    source = HTML.read_text(encoding="utf-8")
    match = re.search(r'<script type="application/json" id="sample-data">(.*?)</script>', source, re.DOTALL)
    assert match
    return json.loads(match.group(1))

def test_embedded_compliance_evidence_matches_every_source_csv():
    data = payload()
    assert data["schema_version"] == 1
    assert "no live cloud" in data["source"].lower()
    for name, relative in FILES.items():
        with (COMPLIANCE / relative).open(encoding="utf-8-sig", newline="") as f:
            original = list(csv.DictReader(f))
        assert data[name] == original
    ids = [row["Control ID"] for row in data["controls"]]
    assert len(ids) == len(set(ids)) == 10
    assert set(ids) == {row["Control ID"] for row in data["mappings"]}
    assert len(data["risks"]) == 5

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.labels = set()
        self.external_js = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            assert a["id"] not in self.ids
            self.ids.add(a["id"])
        if tag == "label" and "for" in a:
            self.labels.add(a["for"])
        if tag == "script" and "src" in a:
            self.external_js.append(a["src"])

def test_explorer_is_accessible_and_does_not_fetch_external_resources():
    page = HTML.read_text(encoding="utf-8")
    inspector = Inspector();inspector.feed(page)
    assert {"query", "provider", "status", "severity"}.issubset(inspector.ids)
    assert {"query", "provider", "status", "severity"}.issubset(inspector.labels)
    assert 'aria-live="polite"' in page
    assert "textContent" in page
    assert "replaceChildren" in page
    assert "innerHTML" not in page and "fetch(" not in page
    assert not inspector.external_js
    for cloud in ("AWS", "Azure", "GCP"):
        assert cloud in page
    assert "no cloud accounts are queried" in page.lower()
