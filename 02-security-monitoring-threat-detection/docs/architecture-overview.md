# Architecture Overview

The security monitoring platform is designed around five core functions:

1. Collect security and operational telemetry.
2. Normalize logs and security findings.
3. Detect suspicious activity and misconfiguration.
4. Alert the correct response channel.
5. Provide dashboards and reports for visibility.

## AWS

AWS uses CloudWatch, CloudTrail, EventBridge, SNS, GuardDuty, Security Hub, and Inspector.

## Azure

Azure uses Azure Monitor, Activity Log, Action Groups, Defender for Cloud, Azure Policy, and optional Log Analytics.

## Google Cloud

Google Cloud uses Cloud Monitoring, Cloud Logging, Cloud Audit Logs, Security Command Center, Alerting Policies, and Notification Channels.
