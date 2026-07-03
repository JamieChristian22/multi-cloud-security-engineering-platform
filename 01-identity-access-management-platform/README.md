# Identity & Access Management Platform

## Purpose

This project demonstrates IAM, RBAC, least privilege, federation, access reviews, break-glass controls across AWS, Azure, and GCP. It is written as an enterprise-style portfolio project for cloud security engineering roles.

## Business Problem

Organizations using multiple cloud providers often struggle with inconsistent security controls. Identity roles, logs, encryption, network rules, and compliance evidence are spread across platforms. This project provides a repeatable model for implementing consistent security practices across AWS, Azure, and GCP.

## Architecture Summary

- AWS environment using native security services and Terraform.
- Azure environment using RBAC, policy, monitoring, and Bicep/Terraform examples.
- GCP environment using IAM, organization policy, logging, and security services.
- Documentation that explains architecture, deployment, validation, and incident response.

## Folder Structure

```text
01-identity-access-management-platform/
├── architecture/
├── detections/
├── docs/
├── evidence/
├── policies/
├── reports/
├── runbooks/
├── scripts/
├── terraform/
└── .github/workflows/
```

## Skills Demonstrated

- Multi-cloud security engineering
- Cloud IAM and least privilege
- Infrastructure as Code
- Detection engineering
- Incident response
- Compliance mapping
- Security documentation
- Audit evidence collection

## How to Use

1. Review `docs/architecture.md`.
2. Review the Terraform/Bicep examples.
3. Run `scripts/validate.sh` to check folder and file quality.
4. Use the runbooks and evidence templates during cloud console demonstrations.
5. Add screenshots from actual AWS, Azure, and GCP deployments.

## Portfolio Rating

This project is designed to be interview-ready because it combines architecture, code, documentation, detection logic, governance, and operational procedures.
