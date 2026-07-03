# Architecture

## Project

Cloud Security Governance & Compliance

## Goal

Create a repeatable multi-cloud security pattern that can be explained to recruiters, hiring managers, and technical interviewers.

## Design Principles

1. Identity-first security.
2. Least privilege by default.
3. Centralized logging and alerting.
4. Private access where possible.
5. Encryption at rest and in transit.
6. Compliance evidence collected continuously.
7. Separation of duties between admins, engineers, auditors, and emergency responders.

## AWS Components

- AWS Organizations
- IAM roles and policies
- CloudTrail
- CloudWatch
- Security Hub
- GuardDuty
- AWS Config
- KMS
- S3 evidence bucket

## Azure Components

- Microsoft Entra ID
- Azure RBAC
- Azure Policy
- Microsoft Defender for Cloud
- Log Analytics Workspace
- Microsoft Sentinel-ready logs
- Key Vault

## GCP Components

- Cloud IAM
- Organization Policies
- Cloud Logging
- Security Command Center
- Cloud KMS
- Secret Manager
- Cloud Asset Inventory

## Data Flow

1. Cloud control-plane activity is logged by each provider.
2. Logs flow into native monitoring systems.
3. Detection rules identify suspicious behavior.
4. Alerts are routed to security responders.
5. Evidence is stored for audit and compliance.
6. Findings are reviewed through runbooks and scorecards.
