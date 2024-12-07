import time
import matplotlib.pyplot as plt
from myUrlGenerator import myUrl

#Function to measure runtime for different input sizes
def time_function(input_sizes, depth, num_trials=1):
    urlGen = myUrl()
    times = []  # Store times for each input size
    for n in input_sizes:
        trial_times = []  # Store times for multiple trials for the same input size
        start_time = time.time()  # Record start time
        urlGen.generateURL(n, depth)  # Run the function
        end_time = time.time()  # Record end time
        times.append(end_time - start_time)  # Append average time to the list
    return times

# Define a range of input sizes to test
input_sizes = list(range(0, 10000, 1000))

# Get the times for the function
execution_times = time_function(input_sizes, 20)

# Plot the times
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b')
plt.title('Execution Time vs URL Depth')
plt.xlabel('URL Depth (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()