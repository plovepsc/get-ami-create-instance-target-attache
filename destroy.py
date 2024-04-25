
import subprocess
import time
def run_command_with_delay(command):
    try:
        # Execute the command using subprocess
        result1 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command executed successfully.")
        print("Output:")
        print(result1.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print("Error output:")
        print(e.output)

# Example usage:
command_to_run = "cd /home/ubuntus/terarom/get-ami/collect_instance_id && terraform destroy --auto-approve"  # Replace this with your desired command
run_command_with_delay(command_to_run)

# def run_command_with_delay(command):
#     try:
#         # Execute the command using subprocess
#         result1 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
#         print("Command executed successfully.")
#         print("Output:")
#         print(result1.stdout)
#     except subprocess.CalledProcessError as e:
#         print(f"Command execution failed: {e}")
#         print("Error output:")
#         print(e.output)

# # Example usage:
# command_to_run = "cd /home/ubuntus/terarom/get-ami/create-instance-amis && terraform destroy --auto-approve"  # Replace this with your desired command
# run_command_with_delay(command_to_run)






def run_command_with_delay(command):
    try:
        # Execute the command using subprocess
        result1 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command executed successfully.")
        print("Output:")
        print(result1.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print("Error output:")
        print(e.output)

# Example usage:
command_to_run = "cd /home/ubuntus/terarom/get-ami/create-instance && terraform destroy --auto-approve"  # Replace this with your desired command
run_command_with_delay(command_to_run)



