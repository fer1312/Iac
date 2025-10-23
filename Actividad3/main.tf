terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "fer_bucket" {
  bucket = "fer-terraform-bucket"
  tags = {
    Name = "FerBucketTerraform"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.fer_bucket.bucket
}