terraform { required_providers { aws = { source="hashicorp/aws", version="~> 5.0" } } }
provider "aws" { region = var.aws_region }
resource "aws_kms_key" "data" { description="KMS key for sensitive portfolio lab data" enable_key_rotation=true }
resource "aws_secretsmanager_secret" "app_secret" { name="zero-trust/app/secret" kms_key_id=aws_kms_key.data.arn }
resource "aws_vpc" "secure" { cidr_block="10.30.0.0/16" enable_dns_hostnames=true tags={Name="zero-trust-secure-vpc"} }
resource "aws_subnet" "private" { vpc_id=aws_vpc.secure.id cidr_block="10.30.10.0/24" map_public_ip_on_launch=false }
resource "aws_vpc_endpoint" "s3" { vpc_id=aws_vpc.secure.id service_name="com.amazonaws.${var.aws_region}.s3" vpc_endpoint_type="Gateway" }
