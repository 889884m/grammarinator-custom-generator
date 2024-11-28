import time
import subprocess
import matplotlib.pyplot as plt

# Command to run
command = "grammarinator-generate urlGenerator.urlGenerator --sys-path /Users/brooke_s/grammarinator-custom-generator/url_grammarinator_files -r url -n 5 -d "

input_sizes = list(range(2, 5000, 100))
# Function to time the command and store results for plotting
def time_command(depth):
    times = []  # List to store times for each trial
    for i in depth:
        command_run = command + f"{i}" 
        start_time = time.time()  # Record start time
        subprocess.run(command_run, shell=True, check=True)  # Run the command
        end_time = time.time()  # Record end time
        times.append(end_time - start_time)  # Append time taken for this trial
    return times

# Get the times for running the command
execution_times = time_command(input_sizes)

# Plot the times for each trial
plt.plot(execution_times, input_sizes, marker='o', linestyle='-', color='b')
plt.title('Command Execution Time for grammarinator-generate')
plt.ylabel('Depth')
plt.xlabel('Time (seconds)')
plt.grid(True)
plt.show()

