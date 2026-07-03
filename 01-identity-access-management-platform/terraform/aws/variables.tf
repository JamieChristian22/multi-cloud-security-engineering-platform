variable "aws_region" { default = "us-east-1" }
variable "break_glass_principal_arn" { description = "Trusted emergency principal ARN" type = string default = "arn:aws:iam::123456789012:root" }
