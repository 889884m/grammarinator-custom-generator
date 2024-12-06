import time
import subprocess
import matplotlib.pyplot as plt

# Command to run
command = "grammarinator-generate urlGenerator.urlGenerator --sys-path /Users/brooke_s/grammarinator-custom-generator/url_grammarinator_files -r url -d 20 -n "

# Function to time the command and store results for plotting
def time_command(number_run):
    times = []  # List to store times for each trial
    for i in number_run:
        command_run = command + str(i) 
        print(command_run)
        start_time = time.time()  # Record start time
        subprocess.run(command_run, shell=True, check=True)  # Run the command
        end_time = time.time()  # Record end time
        times.append(end_time - start_time)  # Append time taken for this trial
    return times

# Get the times for running the command
input_sizes = list(range(2, 30000, 1000))
print(input_sizes)
execution_times = time_command(input_sizes)

# Plot the times for each trial
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b')
plt.title('Command Execution Time for grammarinator-generate')
plt.ylabel('Time (seconds)')
plt.xlabel('Number Tests Generated')
plt.grid(True)
plt.show()

