resource "null_resource" "remove_file" {
  
  # Use a local-exec provisioner to run a command
  provisioner "local-exec" {
    # Command to remove the file
    command = "rm -f /home/ubuntus/terarom/get-ami/create-instance-amis/terraform.tfstate"
  }
  
  # Trigger the provisioner when Terraform apply is executed
  triggers = {
    always_run = "${timestamp()}"
  }
}
resource  "aws_ami_from_instance" "custom-create-image" {
    name               = "elastic-search-beta-${formatdate("YYYY-MM-DD-HH-mm-ss", timestamp())}"
    source_instance_id = "${var.instance_id}"
    snapshot_without_reboot = true
    
  tags = {
      Name = "elastic-search-beta-${formatdate("YYYY-MM-DD-HH-mm-ss", timestamp())}"
  }

}
output "ami_id" {
    value = aws_ami_from_instance.custom-create-image.id
  
}

