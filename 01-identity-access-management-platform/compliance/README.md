# Multi-Cloud IAM Compliance Program

This directory implements a complete compliance workstream for the Identity and Access Management Platform across AWS, Microsoft Azure, and Google Cloud.

## Objectives

- Establish measurable identity security controls across all three cloud providers.
- Map technical controls to NIST SP 800-53 Rev. 5, NIST CSF, CIS-aligned practices, SOC 2, and ISO 27001.
- Produce repeatable evidence for audits.
- Automate identity posture assessment and exception reporting.
- Maintain a risk register and remediation runbooks.

## Control Scope

The program covers:

- Multi-factor authentication
- Least privilege
- Privileged access
- Identity lifecycle management
- Workload identities
- Access logging
- Periodic access reviews
- Break-glass accounts
- Service account governance
- Federation and single sign-on
- Policy enforcement
- Audit evidence retention

## Operating Model

1. **Prevent** — Enforce baseline policy through cloud-native policy engines and Infrastructure as Code.
2. **Detect** — Continuously evaluate identity posture and flag deviations.
3. **Respond** — Execute documented remediation and exception workflows.
4. **Prove** — Collect evidence with timestamps, owners, hashes, and control references.
5. **Improve** — Review trends monthly and update controls quarterly.

## Repository Map

- `frameworks/` — framework-specific control narratives
- `aws/`, `azure/`, `gcp/` — provider implementation and evidence
- `cross-cloud/` — consolidated mappings, risks, and audit procedures
- `scripts/` — working assessment and evidence-generation tools
- `runbooks/` — operational remediation procedures

## Evidence Integrity

Evidence records include a SHA-256 hash so reviewers can verify that collected artifacts have not changed after capture.

## Portfolio Use

This package is written as an enterprise-grade implementation. Sample reports are clearly labeled as lab demonstration data and are not presented as production audit results.
