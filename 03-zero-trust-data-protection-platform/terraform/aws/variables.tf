variable "aws_region" {
  description = "AWS region."
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Globally unique S3 bucket name for protected data."
  type        = string
}
