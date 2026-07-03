# Threat Model

| Threat | Attack Path | Control |
|---|---|---|
| Credential theft | Stolen user keys used to access resources | MFA, conditional access, short-lived tokens |
| Data exposure | Public storage or unencrypted database | Private endpoints, encryption, policy deny rules |
| Lateral movement | Broad network access between workloads | Segmentation and private access |
| Secret leakage | Secrets stored in code | Secret managers and scanning |
