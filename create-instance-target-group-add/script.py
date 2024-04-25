
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