# 03 Zero Trust Data Protection Platform

This project demonstrates a multi-cloud zero trust and data protection architecture across AWS, Azure, and Google Cloud.

## Objective

Implement a security model that protects sensitive data using least privilege access, encryption, identity-based controls, private network access, audit logging, and policy enforcement across multiple cloud providers.

## Core Capabilities

- Identity-based access control
- Least privilege permissions
- Encryption at rest
- Encryption in transit
- Secret management
- Data storage protection
- Public access prevention
- Audit logging
- Policy enforcement
- Incident response runbooks
- Multi-cloud governance mapping

## Cloud Service Mapping

| Capability | AWS | Azure | Google Cloud |
|---|---|---|---|
| Identity | IAM | Microsoft Entra ID / RBAC | Cloud IAM |
| Secrets | Secrets Manager | Key Vault | Secret Manager |
| Encryption | KMS | Key Vault / Storage Encryption | Cloud KMS |
| Object Storage | S3 | Storage Accounts | Cloud Storage |
| Policy | IAM / SCP / Config | Azure Policy | Organization Policy |
| Logging | CloudTrail | Activity Log | Cloud Audit Logs |
| Security Posture | Security Hub | Defender for Cloud | Security Command Center |

## Folder Structure

```text
architecture/
docs/
evidence/
policies/
runbooks/
scripts/
terraform/
```
