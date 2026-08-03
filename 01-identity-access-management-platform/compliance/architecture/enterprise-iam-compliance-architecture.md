# Enterprise IAM Compliance Architecture

```mermaid
flowchart LR
    U[Workforce Users] --> IDP[Enterprise Identity Provider]
    IDP --> AWS[AWS IAM Identity Center]
    IDP --> AZ[Microsoft Entra ID]
    IDP --> GCP[Google Cloud Identity]

    GH[GitHub Actions OIDC] --> AWS
    GH --> AZ
    GH --> GCP

    AWS --> AWSLOG[CloudTrail / Config / Security Hub]
    AZ --> AZLOG[Entra Logs / Azure Policy / Defender]
    GCP --> GCPLOG[Audit Logs / SCC / Org Policy]

    AWSLOG --> EVID[Evidence Pipeline]
    AZLOG --> EVID
    GCPLOG --> EVID

    EVID --> HASH[SHA-256 Manifest]
    HASH --> CTRL[Control Evaluation]
    CTRL --> RISK[Risk Register]
    RISK --> DASH[Executive Dashboard]
```

## Design Principles

- Federated workforce access
- Short-lived workload credentials
- Least privilege by default
- Automated evidence collection
- Policy-as-code enforcement
- Centralized control mapping
- Repeatable audit procedures
