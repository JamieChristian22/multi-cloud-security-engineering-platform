output "cloudtrail_name" {
  value = aws_cloudtrail.iam_audit.name
}

output "audit_bucket" {
  value = aws_s3_bucket.audit_logs.id
}
