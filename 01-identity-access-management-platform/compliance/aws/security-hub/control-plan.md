# AWS Security Hub IAM Control Plan

Enable Security Hub CSPM and applicable standards in all governed regions.

## Priority Findings

- IAM users with console access and no MFA
- Root account without MFA
- Unused credentials
- Overly permissive policies
- CloudTrail not enabled or not protected
- Access Analyzer findings for external access

## Workflow

1. Security Hub produces a finding.
2. EventBridge routes high and critical findings.
3. The assigned owner validates scope.
4. The owner remediates or submits an exception.
5. Evidence is exported to `aws/evidence`.
6. The risk register is updated when residual risk remains.
