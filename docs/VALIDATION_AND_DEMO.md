# Multi-cloud validation, interactive demo and security evidence

## Review and run

The [offline IAM control explorer](../demo/multicloud-posture.html) uses checked-in sample compliance data. Open it locally; select AWS/Azure/GCP mappings and filter by example assessment status, severity or control name. It is a **source-backed demonstration**, not a real-time posture scan.

The source-of-truth files live in the IAM Compliance program:

- [10 illustrative IAM statuses](../01-identity-access-management-platform/compliance/cross-cloud/audit/control-status.csv)
- [10 conceptual AWS / Azure / GCP control mappings](../01-identity-access-management-platform/compliance/cross-cloud/control-mappings/control-matrix.csv)
- [Five example risks](../01-identity-access-management-platform/compliance/cross-cloud/risk-register/risk-register.csv)

`tests/test_security_explorer.py` checks that every embedded row matches the original CSVs exactly and that the offline browser UI renders values safely.

## Local source validation

Use Python 3.12:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_multicloud.py
python -m pytest -q tests 01-identity-access-management-platform/compliance/tests
python 01-identity-access-management-platform/compliance/scripts/python/score_controls.py 01-identity-access-management-platform/compliance/cross-cloud/audit/control-status.csv
python 01-identity-access-management-platform/compliance/scripts/python/build_executive_dashboard.py 01-identity-access-management-platform/compliance/cross-cloud/audit/control-status.csv --output reports/sample-iam-score.json
```

`scripts/validate_multicloud.py` checks HCL syntax with python-hcl2 in **all 15 Terraform roots** (5 each for AWS, Azure, GCP), parses repository JSON, and verifies that sample assessment IDs and severities match the mapping table. It fails closed on unknown statuses, missing mappings, malformed HCL, or invalid JSON. These are **offline syntax checks**, not cloud provider API validation or completed deployment.

## Scoring and its limits

The command-line scorer and generated JSON dashboard now share the same validated formula:

```text
severity weight = Critical 5, High 3, Medium 2, Low 1
Compliant = 1.0; Partially Compliant = 0.5; Noncompliant = 0.0
Not Applicable = excluded from numerator and denominator
score = 100 * weighted achieved / weighted possible
if weighted possible == 0: score is N/A (not 100%)
```

Historical `Assessment Date` and `Assessor` fields are copied from the sample CSV only. An example `Compliant` status must **not** be represented as a verified present-day cloud security finding, live audit evidence, regulatory compliance certification or AWS/Azure/GCP configuration confirmation.

## GitHub Actions and security boundaries

[The CI workflow](../.github/workflows/multicloud-security-ci.yml) contains:
- **Evidence**: 15-root HCL parse, JSON/CSV validation, Python regression tests, source-backed explorer parity and a scored sample dashboard.
- **Terraform provider validation**: three **IAM compliance** roots, one each for AWS, Azure and GCP. Initializes pinned-compatible providers and runs `terraform validate` with `-backend=false`; **no `plan`, `apply` or cloud credentials**.
- **Secrets**: SHA256-verified Gitleaks scan of reachable Git commit history.

The remaining 12 Terraform roots are syntax-checked, **not provider-schema validated** in this first CI phase. Add separate provider validation and policy-as-code evaluation for the other roots before claiming that all infrastructure is deployable. Review and commit generated `.terraform.lock.hcl` files once provider updates are approved.

## Advisory static IaC security findings (first run: 2026-11-01)

The `iac-policy` job runs Checkov over all Terraform roots and uploads both the raw `checkov-findings.json` and a summary. **This job is advisory, not a security pass gate.** In [GitHub Actions run #41339673947](https://github.com/JamieChristian22/multi-cloud-security-engineering-platform/actions/runs/41339673947), Checkov evaluated **101 policy checks: 60 passed and 41 failed**. The findings require security review, not automatic acceptance or claims that the IaC is fully hardened. The Checkov output did not provide severities for these checks, so the summary correctly labels them `UNSPECIFIED` instead of inventing a risk rating.

Download the `multicloud-iac-security-findings` artifact from that Actions run and triage each failure by file, rule, relevant risk and required action. Where a rule is intentionally inapplicable, document a specific exception and reviewer; do not globally suppress the security scan. A future promotion gate should make resolved findings blocking and add provider-schema validation for the remaining 12 roots.

## Risks and future work

Cloud security settings in this repository are **reference designs**. Deployment needs independent reviews of least privilege, S3/Blob/GCS public access, logs, encryption, identity trust, alert delivery, account/tenant/project ownership and cost limits. Some source configurations could be incomplete or unsafe for production; do not deploy them unchanged.

Future upgrade gates: validate remaining 12 provider roots, add genuinely blocking IaC security-policy checks with explicit baselines, run provider-authenticated read-only compliance assertions only in authorized sandboxes, record timestamped evidence and measured risk remediation. No live cloud resources were accessed in this upgrade.
