variable "region" {
  type    = string
  default = "us-east-1"
}

variable "environment" {
  type    = string
  default = "lab"
}

variable "audit_bucket_name" {
  type        = string
  description = "Globally unique S3 bucket name for CloudTrail logs"
}
