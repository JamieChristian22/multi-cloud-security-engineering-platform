terraform {
  required_version = ">= 1.6.0"
  required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } }
}
provider "aws" { region = var.aws_region }

resource "aws_config_config_rule" "s3_public_read_prohibited" {
  name = "enterprise-s3-public-read-prohibited"
  source {
    owner = "AWS"
    source_identifier = "S3_BUCKET_PUBLIC_READ_PROHIBITED"
  }
}

resource "aws_budgets_budget" "monthly" {
  name = "Enterprise-Monthly-Governance-Budget"
  budget_type = "COST"
  limit_amount = "50"
  limit_unit = "USD"
  time_unit = "MONTHLY"
}
