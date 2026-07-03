terraform { required_providers { aws = { source="hashicorp/aws", version="~> 5.0" } } }
provider "aws" { region = var.aws_region }
resource "aws_config_configuration_recorder" "main" { name="security-config-recorder" role_arn=var.config_role_arn }
resource "aws_config_config_rule" "s3_public_read_prohibited" { name="s3-bucket-public-read-prohibited" source { owner="AWS" source_identifier="S3_BUCKET_PUBLIC_READ_PROHIBITED" } }
resource "aws_budgets_budget" "security_budget" { name="security-lab-budget" budget_type="COST" limit_amount="50" limit_unit="USD" time_unit="MONTHLY" }
