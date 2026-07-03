terraform { required_providers { aws = { source="hashicorp/aws", version="~> 5.0" } } }
provider "aws" { region = var.aws_region }
resource "aws_s3_bucket" "cloudtrail_logs" { bucket = "security-monitoring-cloudtrail-logs-123456" }
resource "aws_cloudtrail" "org_trail" { name="security-org-trail" s3_bucket_name=aws_s3_bucket.cloudtrail_logs.id include_global_service_events=true is_multi_region_trail=true enable_logging=true }
resource "aws_guardduty_detector" "main" { enable = true }
resource "aws_securityhub_account" "main" {}
