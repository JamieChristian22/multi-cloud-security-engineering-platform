# Remediation Plan

| Finding | Owner | Action | Target Date | Success Measure |
|---|---|---|---|---|
| Long-lived AWS workload key | Cloud Engineering | Replace with GitHub OIDC or IAM role | 2026-08-17 | No static access key remains |
| GCP service-account key | Cloud Engineering | Migrate to Workload Identity Federation | 2026-08-17 | Key inventory shows zero user-managed keys |
| External trust review | IAM Platform Owner | Complete recertification campaign | 2026-08-24 | All external principals approved or removed |
