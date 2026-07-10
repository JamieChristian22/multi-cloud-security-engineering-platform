output "protected_bucket_name" {
  value = aws_s3_bucket.protected_data.bucket
}

output "kms_key_arn" {
  value = aws_kms_key.data_protection.arn
}
