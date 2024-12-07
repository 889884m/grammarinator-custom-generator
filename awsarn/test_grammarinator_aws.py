import subprocess
import time
import sys

def run_command(command):
    """
    Runs a command in bash and measures the time taken to execute it.

    Args:
        command (str): The bash command to be executed.

    Returns:
        int: The return code from the subprocess.
    """
    start_time = time.time()  # Record the start time

    try:
        # Run the command in a subprocess
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time

        # Print output and error (if any)
        print("Output:")
        print(result.stdout.decode())
        if result.stderr:
            print("Errors:")
            print(result.stderr.decode())

        print(f"Command executed in {execution_time:.4f} seconds")
        return result.returncode
    except subprocess.CalledProcessError as e:
        end_time = time.time()  # Record end time even on error
        execution_time = end_time - start_time
        print(f"Error executing command: {e.stderr.decode()}")
        print(f"Command failed in {execution_time:.4f} seconds")
        return e.returncode

if __name__ == "__main__":
    # Check if the user passed a command as an argument
    if len(sys.argv) < 1:
        print("Usage: python measure_time.py '<bash_command>'")
        sys.exit(1)

    # Join the command passed as arguments
    bash_command = """
    grammarinator-process awsarn/awsarn.g4 -o awsarn/
    
    grammarinator-generate awsarnGenerator.awsarnGenerator  -r start -o tests/awsarn/test_%d.txt -n 10 --sys-path $main_dir/awsarn
    """
    run_command(bash_command)
