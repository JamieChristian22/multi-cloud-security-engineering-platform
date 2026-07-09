# AWS Detection: Unauthorized API Calls

## Signal

CloudTrail events with error codes such as `AccessDenied`, `UnauthorizedOperation`, or `Client.UnauthorizedOperation`.

## Detection Logic

Monitor CloudTrail event history and CloudWatch Logs for repeated authorization failures.

## Severity

Medium to High depending on the principal and target service.

## Response

1. Identify the IAM principal.
2. Review the source IP address.
3. Confirm whether the action was expected.
4. Check recent IAM policy changes.
5. Escalate if the principal appears compromised.
