locals{
    instance_count = 2
    instance_name = act6-fer-julia
}
resource "aws+instance" "ferjulia_server_terr" {
    count = local.instance_count
    ami = "ami-0cfde0ea8edd312d4"
    instance_type = "t3.micro"
    
    tags = {
        Name = local.instance_name
    } 
}

output "server_name" {
    value = aws_instance.ferjulia_server_terr.tags.Name
  
}