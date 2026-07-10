terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_kms_key" "data_protection" {
  description             = "KMS key for sensitive data protection"
  deletion_window_in_days = 7
  enable_key_rotation     = true
}

resource "aws_s3_bucket" "protected_data" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_public_access_block" "protected_data" {
  bucket                  = aws_s3_bucket.protected_data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "protected_data" {
  bucket = aws_s3_bucket.protected_data.id

  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = aws_kms_key.data_protection.arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_secretsmanager_secret" "application_secret" {
  name = "enterprise/application/database-password"
}
