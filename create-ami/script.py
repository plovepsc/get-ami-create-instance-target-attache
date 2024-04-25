
import subprocess



def run_terraform_command(command_args):
    try:
        # Execute the terraform command with provided arguments
        result1 = subprocess.run(["terraform"] + command_args, capture_output=True, text=True)
        
        # Check the result
        if result1.returncode == 0:
            print("Terraform command executed successfully.")
            print(result1.stdout)
        else:
            print("Terraform command failed.")
            print(result1.stderr)
    
    except FileNotFoundError:
        print("Terraform binary not found. Make sure Terraform is installed and in PATH.")

# Example usage: Run 'terraform apply'
command_arguments = ["apply", "-auto-approve"]
run_terraform_command(command_arguments)


# Run terraform output command and capture the result
result = subprocess.run(["terraform", "output", "ami_id"], capture_output=True, text=True)

# Extract the output value from the result
output_value = result.stdout.strip()

# Write the output value to a text file
with open("/home/ubuntus/terarom/get-ami/create-instance/terraform.tfvars", "w") as file:
        file.write("customs_ami = "+ str(output_value))

        print(f"Output value '{output_value}' captured to outputfile")