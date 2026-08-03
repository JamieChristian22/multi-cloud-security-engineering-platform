# 🛡️ Multi-Cloud Security Monitoring & Threat Detection Platform

![AWS](https://img.shields.io/badge/AWS-Security%20Monitoring-FF9900?logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Security%20Operations-0078D4?logo=microsoftazure&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Threat%20Detection-4285F4?logo=googlecloud&logoColor=white)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform)
![Security](https://img.shields.io/badge/Focus-Detection%20Engineering-red)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-darkred)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Executive Summary

The **Multi-Cloud Security Monitoring & Threat Detection Platform** is an enterprise-inspired security operations project that demonstrates how modern organizations collect, analyze, detect, investigate, and respond to security events across **Amazon Web Services (AWS)**, **Microsoft Azure**, and **Google Cloud Platform (GCP)**.

Rather than focusing solely on preventive controls, this project emphasizes operational security by implementing centralized monitoring, log collection, detection engineering, alert management, compliance validation, incident response workflows, and infrastructure automation.

The platform simulates the daily responsibilities of a Cloud Security Engineer, Security Operations Center (SOC) Analyst, Detection Engineer, or Cloud Infrastructure Engineer responsible for protecting multi-cloud environments.

---

# Project Goals

This project demonstrates how to:

- Design enterprise security monitoring architecture
- Implement centralized cloud logging
- Build detection rules
- Generate actionable security alerts
- Investigate suspicious cloud activity
- Perform incident response
- Document evidence
- Validate compliance controls
- Automate cloud security deployments using Terraform

---

# Business Problem

Organizations commonly operate workloads across AWS, Azure, and Google Cloud.

This creates several security challenges:

- Multiple logging systems
- Different IAM models
- Different security tools
- Alert fatigue
- Compliance requirements
- Lack of centralized visibility

This platform demonstrates how security teams can standardize monitoring, automate detection, document investigations, and improve operational response across cloud providers.

---

# Architecture

```
                +----------------------+
                |   Cloud Resources    |
                +----------+-----------+
                           |
        +------------------+------------------+
        |                  |                  |
      AWS               Azure               GCP
        |                  |                  |
 CloudTrail          Azure Monitor     Cloud Audit Logs
 GuardDuty           Defender          SCC
 Security Hub        Sentinel          Cloud Logging
        |                  |                  |
        +------------------+------------------+
                           |
                 Central Security Operations
                           |
        +---------------------------------------+
        | Detection Rules                       |
        | Threat Intelligence                   |
        | Dashboards                            |
        | Alert Correlation                     |
        | Investigation                         |
        | Incident Response                     |
        +---------------------------------------+
```

---

# Technology Stack

## Cloud Platforms

- Amazon Web Services
- Microsoft Azure
- Google Cloud Platform

## Infrastructure as Code

- Terraform

## Security Services

### AWS

- CloudTrail
- GuardDuty
- Security Hub
- CloudWatch
- EventBridge
- IAM Access Analyzer

### Azure

- Microsoft Sentinel
- Microsoft Defender for Cloud
- Azure Monitor
- Log Analytics
- Microsoft Entra ID

### Google Cloud

- Cloud Logging
- Security Command Center
- Cloud Monitoring
- Cloud Audit Logs

---

# Repository Structure

```
02-security-monitoring-threat-detection/

├── alerts/
├── architecture/
├── compliance/
├── dashboards/
├── detections/
├── docs/
├── evidence/
├── logs/
├── playbooks/
├── reports/
├── runbooks/
├── scripts/
├── terraform/
└── README.md
```

---

# Folder Overview

## alerts/

Contains cloud-generated security alerts including:

- High Severity Alerts
- Critical Alerts
- IAM Alerts
- Malware Alerts
- GuardDuty Findings
- Sentinel Incidents
- SCC Findings

---

## architecture/

Contains

- High-Level Architecture
- AWS Architecture
- Azure Architecture
- GCP Architecture
- Logging Pipeline
- Detection Pipeline
- Alert Flow
- Incident Response Workflow

---

## compliance/

Maps implemented controls against

- NIST CSF
- NIST 800-53
- CIS Benchmarks
- ISO 27001
- SOC 2
- PCI DSS
- HIPAA

---

## dashboards/

Security dashboards showing

- Authentication Events
- Failed Logins
- Privileged Access
- Threat Findings
- Compliance Status
- Security Health
- Alert Trends

---

## detections/

Contains detection documentation and detection logic.

Each detection includes:

- Description
- Severity
- MITRE ATT&CK Mapping
- Log Source
- Detection Logic
- Investigation Steps
- Response Actions
- Validation Evidence

Example detections include:

- Root Account Login
- New Administrator Created
- Privilege Escalation
- MFA Disabled
- Public Storage Exposure
- Security Group Open to Internet
- Impossible Travel Login
- Excessive Failed Logins
- Credential Abuse
- API Key Misuse

---

## docs/

Project documentation

- Security Design
- Architecture Notes
- Detection Standards
- Threat Models
- Deployment Guide

---

## evidence/

Contains deployment screenshots demonstrating successful implementation.

Examples include:

AWS

- GuardDuty Findings
- Security Hub
- CloudTrail Logs
- CloudWatch Dashboard

Azure

- Sentinel Incidents
- Defender Alerts
- Log Analytics

Google Cloud

- Security Command Center
- Cloud Logging
- Monitoring Dashboards

---

## logs/

Sample log data including

- Authentication
- IAM Changes
- API Calls
- Administrative Events
- Network Events
- Security Findings

---

## playbooks/

Incident response playbooks for

- Credential Theft
- Ransomware
- Privilege Escalation
- Public Storage
- Malware
- Insider Threat
- Data Exfiltration
- Account Compromise

---

## reports/

Contains

- Security Assessments
- Detection Validation
- Compliance Reports
- Investigation Reports
- Executive Summaries

---

## runbooks/

Operational procedures

Examples:

- Investigating GuardDuty Alerts
- Investigating Sentinel Alerts
- CloudTrail Investigation
- Security Hub Findings
- Azure Sign-in Investigation
- GCP SCC Investigation

---

## scripts/

Automation scripts for

- Log Collection
- Alert Validation
- Compliance Checks
- Evidence Collection
- Report Generation

---

## terraform/

Infrastructure-as-Code deployment for

AWS

- CloudTrail
- GuardDuty
- Security Hub
- CloudWatch
- EventBridge

Azure

- Sentinel
- Log Analytics
- Azure Monitor

Google Cloud

- Security Command Center
- Cloud Logging
- Monitoring

---

# Detection Engineering

The platform demonstrates security detections for common attack techniques.

| Detection | Cloud | Severity |
|-----------|-------|----------|
| Root Login | AWS | Critical |
| IAM Policy Change | AWS | High |
| New Administrator | AWS | High |
| MFA Disabled | AWS | High |
| Impossible Travel | Azure | High |
| Privileged Role Assignment | Azure | Critical |
| Suspicious Sign-in | Azure | High |
| Public Bucket | GCP | High |
| IAM Policy Modification | GCP | High |
| Service Account Abuse | GCP | Critical |

---

# MITRE ATT&CK Coverage

| Technique | ID |
|------------|----|
| Valid Accounts | T1078 |
| Create Account | T1136 |
| Account Discovery | T1087 |
| Cloud Administration Command | T1651 |
| Modify Authentication Process | T1556 |
| Exfiltration | T1020 |
| Defense Evasion | T1562 |
| Persistence | T1098 |

---

# Incident Response Workflow

```
Threat Activity

↓

Cloud Logs Generated

↓

Detection Rule Triggered

↓

Security Alert Created

↓

SOC Investigation

↓

Evidence Collection

↓

Containment

↓

Eradication

↓

Recovery

↓

Lessons Learned
```

---

# Validation Testing

| Test | Expected | Result |
|------|----------|--------|
| Root Login Detection | Alert Generated | ✅ PASS |
| IAM Policy Change | Alert Generated | ✅ PASS |
| MFA Disabled | Alert Generated | ✅ PASS |
| Impossible Travel | Alert Generated | ✅ PASS |
| Public Storage | Alert Generated | ✅ PASS |
| Privilege Escalation | Alert Generated | ✅ PASS |

---

# Compliance Coverage

The platform demonstrates controls aligned with

- NIST Cybersecurity Framework
- CIS Benchmarks
- ISO 27001
- SOC 2
- PCI DSS
- HIPAA
- Cloud Security Alliance CCM

---

# Security Best Practices Demonstrated

- Least Privilege
- Zero Trust
- Defense in Depth
- Centralized Logging
- Threat Detection
- Continuous Monitoring
- Automated Alerting
- Incident Response
- Security Automation
- Infrastructure as Code
- Compliance Validation
- Audit Logging

---

# Skills Demonstrated

## Cloud Security

- AWS Security
- Azure Security
- Google Cloud Security

## Detection Engineering

- Log Analysis
- Alert Development
- Threat Hunting
- Detection Validation

## Security Operations

- Incident Response
- Investigation
- Evidence Collection
- Root Cause Analysis

## DevSecOps

- Terraform
- Infrastructure Automation
- Security as Code

---

# Resume Highlights

- Designed and implemented a multi-cloud security monitoring platform spanning AWS, Azure, and Google Cloud.
- Built enterprise-style threat detection workflows, alerting, incident response documentation, and compliance reporting.
- Automated cloud security deployments using Terraform and Infrastructure as Code principles.
- Created security monitoring dashboards, investigation playbooks, validation reports, and operational runbooks.
- Demonstrated knowledge of cloud-native security services including GuardDuty, Security Hub, Microsoft Sentinel, Defender for Cloud, and Security Command Center.

---

# Future Enhancements

- Sigma Rules
- Detection-as-Code
- GitHub Actions CI/CD
- Automated Threat Hunting
- SOAR Integration
- Threat Intelligence Feeds
- YARA-L Rules
- Cross-Cloud Correlation Engine
- SIEM Integration
- Security Scorecards

---

# Author

**Jamie Christian**

GitHub: https://github.com/JamieChristian22

---

# License

This project is provided for educational and portfolio purposes to demonstrate enterprise cloud security engineering, detection engineering, and security operations capabilities.
