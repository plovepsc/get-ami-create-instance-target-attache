
resource "aws_instance" "elastic-create-insance" {
    ami = "${var.customs_ami}"
    instance_type = "t2.micro"
    count = 2
    subnet_id = "${var.subnet_public}"
    security_groups = [ "sg-0200855d6ab6ad5db" ]
    key_name = "levelup-key"
    tags = {
      Name = "elastic-spa-prod"
    }

provisioner "file" {
    source      = "script.sh"
    destination = "/tmp/script.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/script.sh",
      "sudo /tmp/script.sh"
    ]
  }

   connection {
     host = coalesce(self.public_ip)
     type = "ssh"
     user = "ubuntu"
     private_key = file("levelup-key.pem")
   }

}


resource "null_resource" "delay" {
  provisioner "local-exec" {
    command = "sleep 90"  # Delay for 60 seconds
  }
  
  # Specify a dependency on the first resource
  depends_on = [ aws_instance.elastic-create-insance ]
}

resource "aws_lb_target_group_attachment" "my_target_group_attachment" {
  count           = length(aws_instance.elastic-create-insance.*.id)
  target_group_arn = "your_targetarn"
  target_id       = aws_instance.elastic-create-insance[count.index].id
}

