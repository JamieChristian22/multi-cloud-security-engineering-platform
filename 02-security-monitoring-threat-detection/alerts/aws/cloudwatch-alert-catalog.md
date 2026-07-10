# AWS CloudWatch Alert Catalog

| Alert | Signal | Severity | Action |
|---|---|---|---|
| High CPU | EC2 CPUUtilization > 80% | Medium | Notify operations |
| Lambda Errors | Errors > 0 | High | Notify security operations |
| Unauthorized API Calls | CloudTrail AccessDenied pattern | High | Investigate principal |
| CloudTrail Stopped | StopLogging/DeleteTrail | Critical | Restore logging |
| Root Account Use | Root user API event | Critical | Validate and contain |
| GuardDuty High Severity | Finding severity >= 7 | High | Start incident response |
