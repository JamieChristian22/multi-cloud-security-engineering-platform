# Terraform Deployment

## Validation

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
```

## Security Scanning

```bash
checkov -d .
tfsec .
```

## Deployment Order

1. Deploy logging and evidence storage.
2. Deploy guardrails.
3. Deploy least-privilege audit identities.
4. Validate evidence collection.
5. Enable alerting.
