variable "AWS_ACCESS_KEY" {

 
}

variable "AWS_SECRET_KEY" {

    

}

variable "AWS_REGION" {
    type = string
  default = "ap-south-1"
}


# variable "PATH_TO_PRIVATE_KEY" {
#   default = "levelup_key.pem"
# }

variable "customs_ami" {
  
}


variable "subnet_public" {
    description = "public_subnet"
    default = "subnet-0bf4cb471e70c04a2"
}