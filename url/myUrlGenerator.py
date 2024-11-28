import random
import timeit
import json
import random
import rstr
import os

from os.path import dirname, join

# TLD list from ICANN
with open(join(dirname(__file__), "../tld_list.json")) as f:
    tld_list = json.load(f)

# Schemes from IANA
with open(join(dirname(__file__), "../tld_list.json")) as f:
    schemes = json.load(f)

### switch to calling ICANN api instead? That way list is up to date


class myUrl():
    def __init__(self):
        self.chars = 'qwertyuioplkjhgfdsazxcvbnm1234567890-'


    def tld(self, parent=None):
            return random.choice(tld_list)

    def scheme(self, parent=None):
        return random.choice(schemes) + "://"

    def body_generator(self, depth, parent=None):
        body_depth  = random.randrange(1, depth)
        body_text = ''
        for x in range(body_depth):
            new_char = random.choice(self.chars)
            body_text += new_char
        return body_text + '.'

    def phrase(self, depth, parent=None):
        path_depth  = random.randrange(1, depth)
        path_text = ''
        for x in range(path_depth):
            new_char = random.choice(self.chars)
            path_text += new_char
        return path_text

    def generateURL(self, number=1, depth=10, scheme=None, subdomain=None, body=None, tld=None, path=None):
        lis = []
        for x in range(number):
            up_scheme = scheme or self.scheme()
            curr_scheme = up_scheme.lower()
            curr_subdomain = subdomain or "www."
            curr_body = body or self.body_generator(depth)
            if curr_body[-1] != '.':
                curr_body += '.'
            up_tld = tld or self.tld()
            curr_tld = up_tld.lower()
            curr_path = '/' + self.phrase(depth)
            curr_url = curr_scheme + curr_subdomain + curr_body + curr_tld + curr_path
            lis.append(curr_url)

        return lis


#print(urls)

import time
import matplotlib.pyplot as plt


# Function to measure runtime for different input sizes
def time_function(input_sizes, num_trials=1):
    urlGen = myUrl()
    times = []  # Store times for each input size
    for n in input_sizes:
        trial_times = []  # Store times for multiple trials for the same input size
        for _ in range(num_trials):
            start_time = time.time()  # Record start time
            urlGen.generateURL(n, 10)  # Run the function
            end_time = time.time()  # Record end time
            trial_times.append(end_time - start_time)  # Append time taken for this trial
        avg_time = sum(trial_times) / len(trial_times)  # Average time for the given input size
        times.append(avg_time)  # Append average time to the list
    return times

# Define a range of input sizes to test
input_sizes = list(range(0, 5000, 100))

# Get the times for the function
execution_times = time_function(input_sizes)

# Plot the times
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b')
plt.title('Execution Time vs URL Depth')
plt.xlabel('URL Depth (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()