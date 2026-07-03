terraform {
  required_version = ">= 1.5.0"
  required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } }
}
provider "aws" { region = var.aws_region }

resource "aws_iam_group" "security_auditors" { name = "security-auditors" }
resource "aws_iam_group" "cloud_engineers" { name = "cloud-engineers" }

resource "aws_iam_policy" "auditor_read_only" {
  name        = "SecurityAuditorReadOnlyPolicy"
  description = "Read-only access for security audit review."
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{ Effect="Allow", Action=["iam:Get*","iam:List*","cloudtrail:LookupEvents","config:Get*","config:List*","securityhub:Get*","guardduty:Get*"], Resource="*" }]
  })
}
resource "aws_iam_group_policy_attachment" "auditor_attach" { group=aws_iam_group.security_auditors.name policy_arn=aws_iam_policy.auditor_read_only.arn }
resource "aws_iam_role" "break_glass_admin" {
  name = "break-glass-admin-role"
  assume_role_policy = jsonencode({Version="2012-10-17",Statement=[{Effect="Allow",Principal={AWS=var.break_glass_principal_arn},Action="sts:AssumeRole",Condition={Bool={"aws:MultiFactorAuthPresent"="true"}}}]})
}
resource "aws_iam_role_policy_attachment" "break_glass_admin" { role=aws_iam_role.break_glass_admin.name policy_arn="arn:aws:iam::aws:policy/AdministratorAccess" }
