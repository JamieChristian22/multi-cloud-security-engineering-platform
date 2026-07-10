# AWS GuardDuty Response Playbook

1. Validate finding severity and confidence.
2. Identify affected account, region, principal, and resource.
3. Review CloudTrail and VPC Flow Logs.
4. Disable compromised credentials.
5. Isolate affected EC2 instance or workload.
6. Preserve snapshots and logs.
7. Notify stakeholders through SNS.
8. Document root cause and remediation.
