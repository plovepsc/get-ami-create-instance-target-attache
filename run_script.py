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
command_to_run = "cd /home/ubuntus/terarom/get-ami/collect_instance_id && python3 script.py"  # Replace this with your desired command
run_command_with_delay(command_to_run)


# multiplier capacity

def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for few seconds...")
    time.sleep(delay_seconds)
    print("Executing the command now.")
    
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
command_to_run = "cd /home/ubuntus/terarom/get-ami/create-instance-amis && python3 script.py"  # Replace this with your desired command
delay_seconds = 5  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)



def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for few seconds...")
    time.sleep(delay_seconds)
    print("Executing the command now.")
    
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
command_to_run = "cd /home/ubuntus/terarom/get-ami/create-instance && python3 script.py"  # Replace this with your desired command
delay_seconds = 5  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)