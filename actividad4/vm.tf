resource "aws_instance" "fer_server_terr" {
  ami           = "ami-0360c520857e3138f"
  instance_type = "t3.micro"

  tags = {
    Name = "FerServerTerraform3"
  }
}

output "server_name" {
  value = aws_instance.fer_server_terr.tags.Name
}