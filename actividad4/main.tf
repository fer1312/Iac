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

resource "aws_instance" "fer_server_terr" {
  ami           = "ami-0cfde0ea8edd312d4"
  instance_type = "t3.micro"

  tags = {
    Name = "FerServerTerraform"
  }
}

output "server_name" {
  value = aws_instance.fer_server_terr.tags.Name
}