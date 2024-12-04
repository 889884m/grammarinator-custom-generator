import time
import subprocess
import os
import shutil
import json
import random
import heapq
import argparse
import matplotlib.pyplot as plt
from pathlib import Path

import customIPV6Generator


IPV6_EXEC_BASH       = './ipv6_gram_gen_script_auto.sh'
IPV6_GRAM_TEST_DIR   = 'tests/grammarinator_output'
IPV6_CUST_TEST_DIR   = 'tests/customgen_output'
IPV6_TEST_PACKET_DIR = 'tests/packets'

IPV6_PROCESS_BASH_LINE = \
f"""
main_dir=$(dirname "$(realpath "$0")")  
grammarinator-process ipv6.g4 -o "$main_dir"
"""


class IPV6_Eval():
    def __init__(self, 
                 gen_choice: bool,
                 debug: bool         = False, 
                 num_packets: int    = 1, 
                 address: str | None = None,
                 sleep_time: float   = 0.1
                ) -> None:
        """
            Init function for IPV6_Eval.
            Parameters:
                gen_choice  (bool)  : generator choice. 
                debug       (bool)  : debug flag.                      Default is False.
                num_packets (int)   : number of packets for testing.   Default is 1.
                address     (str)   : hardcoded address for debugging. Default is None.
                sleep_time  (float) : sleep time between packets.      Default is 0.1.
            Output: None
        """
        self.gen_choice = gen_choice

        self.debug       = debug
        self.num_packets = num_packets

        # self.true_start_time = time.perf_counter()
        self.true_start_time = 0
        self.true_print_time = 0

        # self.start_time = self.true_start_time
        self.start_time = 0
        self.print_time = 0
        self.generator_time  = 0

        self.packet_id      = 0
        self.addresses      = []
        self.ipv4_address   = None
        self.expand_address = None

        self.packet_dest = ''

        self.num_groups = 8
        self.sleep_time = sleep_time

        self.total_time = 0
        self.average_time = 0
        self.gen_time = 0

        self.packet_total_path = None

        self.grammarinator_gen_bash_line = f'grammarinator-generate ipv6Generator.ipv6Generator -r start -o "{IPV6_GRAM_TEST_DIR}/test_%d.txt" -n {self.num_packets} --sys-path "$main_dir"'

    def execute(self):
        """
            Main execution function.
            Parameters: None
            Output: None
        """
        self.cleanup()
        self.initialize()

        self.true_start_time = time.perf_counter()
        self.start_time = self.true_print_time

        self.grammarinator() if self.gen_choice == 0 else self.custom_generator()
        self.read_grammarinator_txt()

        for packet_id in range(self.num_packets):
            if self.debug: print()
            if self.debug: print(f"========= Packet {self.packet_id} =========")

            self.decode_ipv6()
            self.send_packet()
            
            # time.sleep(self.sleep_time)
            if self.debug: self.report_time()

            self.packet_id = packet_id + 1
            self.reset()

        if self.debug: print()
        self.report_time(final=True)

        self.cleanup()

        return [self.total_time, self.average_time, self.gen_time]

    def initialize(self):
        if not (os.path.exists(IPV6_GRAM_TEST_DIR) or os.path.isdir(IPV6_GRAM_TEST_DIR)): os.makedirs(IPV6_GRAM_TEST_DIR)
        if self.debug: print(f"Directory created: {IPV6_GRAM_TEST_DIR}")

        if not (os.path.exists(IPV6_CUST_TEST_DIR) or os.path.isdir(IPV6_CUST_TEST_DIR)): os.makedirs(IPV6_CUST_TEST_DIR)
        if self.debug: print(f"Directory created: {IPV6_CUST_TEST_DIR}")

        if not (os.path.exists(IPV6_TEST_PACKET_DIR) or os.path.isdir(IPV6_TEST_PACKET_DIR)): os.makedirs(IPV6_TEST_PACKET_DIR)
        if self.debug: print(f"Directory created: {IPV6_TEST_PACKET_DIR}")

    def grammarinator(self):
        """
            Call grammarinator wrapper.
            Parameters: None
            Output: None
        """
        try:
            with open(IPV6_EXEC_BASH, 'w') as bash_file:
                bash_file.write(IPV6_PROCESS_BASH_LINE + self.grammarinator_gen_bash_line)
            os.chmod(IPV6_EXEC_BASH, 0o755)

            gen_start_time = time.perf_counter()
            result = subprocess.run(["bash", IPV6_EXEC_BASH], check=True, text=True, capture_output=True)
            self.generator_time += time.perf_counter() - gen_start_time
            
            if self.debug: 
                start = time.perf_counter()
                print(f"Script output: {result.stdout}")
                self.print_time += time.perf_counter() - start

        except subprocess.CalledProcessError as e:
            print(f"Script failed with error: {e.stderr}")
            exit()

    def custom_generator(self):
        """
            Call CustomGenerator.
            Parameters: None
            Output: None
        """
        arguments = {'num': self.num_packets,
                     'output': Path(IPV6_CUST_TEST_DIR),
                     'groups': []}
        gen_start_time = time.perf_counter()
        customIPV6Generator.main(arguments)
        self.generator_time += time.perf_counter() - gen_start_time

    def read_grammarinator_txt(self):
        """
            Read grammarinator output file and save content.
            Parameters: None
            Output: None
        """
        try:
            # Open the file and read all its content
            for packet_id in range(self.num_packets):
                file_path = f'{IPV6_GRAM_TEST_DIR if self.gen_choice == 0 else IPV6_CUST_TEST_DIR}/test_{packet_id}.txt'
                with open(file_path, "r") as file:
                    self.addresses.append(file.read())
                if os.path.exists(file_path):
                    os.remove(file_path)
            # if self.debug: 
            #     start = time.perf_counter()
            #     print(f"Grammarinator Output: {self.address}")
            #     self.print_time += time.perf_counter() - start

        except Exception as e:
            print(f"An error occurred: {e}")
            exit()

    def decode_ipv6(self):
        """
            Uncompress IPv6 address string if needed.
            Parameters: None
            Output: None
        """
        # return if uncompressed already
        self.address = self.addresses[self.packet_id]
        self.expand_address = self.address.split(":")
        if len([group for group in self.address.split(':') if len(group) > 0]) == 8:            return
        if '.' in self.address                                                           and\
           len([group for group in self.address.split(':')[:-1] if len(group) > 0]) == 6 and\
           len(self.address.split(':')[-1].split('.')) == 4:                                    return 
        
        if '.' in self.address:  # if ipv4-mapped
            self.address, self.ipv4_address = ''.join([group + ':' for group in self.address.split(':')[:-1]]).rstrip(':'), self.address.split(':')[-1]
            self.num_groups = 6

        self.expand_address = [newgroup for newgroup in self.address.split('::')[0].split(':') +\
                                                        ['0000' for _ in range(self.num_groups - len([group for group in self.address.split(':') if len(group) > 0]))] +\
                                                        self.address.split('::')[1].split(':')
                                        if len(newgroup) > 0]
        self.expand_address = [''.join(['0' for _ in range(4-len(group))]+[group]) for group in self.expand_address]
        self.expand_address += [self.ipv4_address] if self.ipv4_address else []
        
        if self.debug: 
            start = time.perf_counter()
            print(f"Clean IPv6 String: {self.expand_address}")
            self.print_time += time.perf_counter() - start


    def send_packet_via_astar(self):
        def heuristic(current, goal):
            """
            Manhattan distance heuristic for 8D space.
            """
            return sum(abs(current[i] - goal[i]) for i in range(len(current)))

        def generate_neighbors(position):
            """
            Generate all neighbors of an 8D position.
            """
            neighbors = []
            deltas = [-1, 0, 1]
            for delta in [(dx1, dx2, dx3, dx4, dx5, dx6, dx7, dx8) for dx1 in deltas for dx2 in deltas
                        for dx3 in deltas for dx4 in deltas for dx5 in deltas for dx6 in deltas
                        for dx7 in deltas for dx8 in deltas]:
                if any(delta):  # Skip the point itself
                    neighbors.append(tuple(position[i] + delta[i] for i in range(8)))
            return neighbors

        # TEMP HARDCODED IPV6
        source_pure = ['A953', '006D', '0FAA', '0088', '000A', '0005', '878D', '6B51']
        destin_pure = ['A95E', '0061', '0FA1', '008A', '0A02', '0A0C', '8A81', '6A5B']
        # destin_pure = ["2001", "0DB8", "85A3", "0000", "0000", "8A2E", "0370", "7334"]

        start = tuple([int(group, 16) for group in source_pure])
        goal =  tuple([int(group, 16) for group in destin_pure])
        print(f"START ====== {start}")
        print(F"GOAL  ====== {goal}")

        start_node = Node(start)
        goal_node = Node(goal)

        open_set = []
        open_set_dict = {}
        closed_set = {}

        # Initialize the open set with the start node
        heapq.heappush(open_set, start_node)
        open_set_dict[start_node.position] = start_node

        counter = 0
        while open_set:
            current_node = heapq.heappop(open_set)
            open_set_dict.pop(current_node.position, None)
            counter += 1
            if counter % 100 == 0:
                print(f"{counter}:::{current_node.position}")

            if current_node == goal_node:
                # Reconstruct the path
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]  # Reverse the path

            closed_set[current_node.position] = current_node

            # Generate neighbors
            for neighbor_position in generate_neighbors(current_node.position):
                if neighbor_position in closed_set:
                    continue

                neighbor_node = Node(neighbor_position, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_position, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_position in open_set_dict:
                    # Skip if a better path already exists in the open set
                    existing_node = open_set_dict[neighbor_position]
                    if neighbor_node.g < existing_node.g:
                        existing_node.g = neighbor_node.g
                        existing_node.f = neighbor_node.f
                        existing_node.parent = current_node
                else:
                    heapq.heappush(open_set, neighbor_node)
                    open_set_dict[neighbor_position] = neighbor_node

        return None  # No path found

    def report_time(self,
                    final: bool = False):
        """
            Prints execution time.
            Parameters: 
                final (bool) : Final flag
            Output: None
        """
        self.total_time = f"{(time.perf_counter()-self.true_start_time-self.true_print_time):.1f}"
        self.average_time = f"{(time.perf_counter()-self.true_start_time-self.true_print_time)/(self.num_packets):.1f}"
        self.gen_time = f"{self.generator_time:.1f}"
        print(f"Time elapsed: {(time.perf_counter()-self.start_time-self.print_time):.6f} seconds" if not final else\
                f"Total time  : {(time.perf_counter()-self.true_start_time-self.true_print_time):.6f} seconds \nAverage time: {(time.perf_counter()-self.true_start_time-self.true_print_time)/(self.num_packets):.6f} seconds\nGenerator time: {self.generator_time:.6f} seconds\n") 

    def reset(self):
        """
            Resets parameters between packets.
            Parameters: None
            Output: None    
        """
        # if self.packet_total_path: os.remove(self.packet_total_path)
        if os.path.exists(IPV6_TEST_PACKET_DIR + '/' + ''.join([self.expand_address[0]])) and\
           os.path.isdir(IPV6_TEST_PACKET_DIR + '/' + ''.join([self.expand_address[0]])):
           shutil.rmtree(IPV6_TEST_PACKET_DIR + '/' + ''.join([self.expand_address[0]]))
           if self.debug: print(f"Deleted {IPV6_TEST_PACKET_DIR + '/' + ''.join([self.expand_address[0]])}")

        self.true_print_time += self.print_time

        self.start_time = time.perf_counter()
        self.print_time = 0

        self.address = None
        self.ipv4_address = None
        self.expand_address = None

        self.num_groups = 8

        self.packet_dest = ''

        self.grammarinator_gen_bash_line = f'grammarinator-generate ipv6Generator.ipv6Generator  -r start -o "{IPV6_GRAM_TEST_DIR}/test_{self.packet_id}.txt" -n 1 --sys-path "$main_dir"'


    def cleanup(self):
        """
            Clean up for directories.
            Parameters: None
            Output: None
        """
        if os.path.exists(IPV6_GRAM_TEST_DIR) and os.path.isdir(IPV6_GRAM_TEST_DIR):
            shutil.rmtree(IPV6_GRAM_TEST_DIR)
            if self.debug: print(f"All files removed from {IPV6_GRAM_TEST_DIR}")

        if os.path.exists(IPV6_CUST_TEST_DIR) and os.path.isdir(IPV6_CUST_TEST_DIR):
            shutil.rmtree(IPV6_CUST_TEST_DIR)
            if self.debug: print(f"All files removed from {IPV6_CUST_TEST_DIR}")

        if os.path.exists(IPV6_TEST_PACKET_DIR) and os.path.isdir(IPV6_TEST_PACKET_DIR): 
            shutil.rmtree(IPV6_TEST_PACKET_DIR)
            if self.debug: print(f"All files removed from {IPV6_TEST_PACKET_DIR}")


class Node:
    def __init__(self, position, parent=None):
        self.position = position  # 8D position as a tuple
        self.parent = parent      # Parent node for path reconstruction
        self.g = 0                # Cost from start to current node
        self.h = 0                # Heuristic (estimated cost to goal)
        self.f = 0                # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def main(args):
    number_of_packets = [1,10,100,1000,2000,4000,6000,8000,10000,50000,100000,500000,1000000]
    # number_of_packets = [1,10,100,1000]
    total_execution_time = []
    average_execution_time = []
    generator_execution_time = []
    for n in number_of_packets:
        print(f"--------------------- {n} Packets ---------------------")
        ipv6_eval = IPV6_Eval(gen_choice  = args.generator,
                              debug       = args.debug,    
                              num_packets = n)
        total, average, generator = ipv6_eval.execute()
        total_execution_time.append(total)
        generator_execution_time.append(generator)

        ipv6_eval.cleanup()

    print(total_execution_time)
    # print(generator_execution_time)
    # plt.figure(figsize=(8, 5))
    # plt.plot(number_of_packets, total_execution_time, marker='o', linestyle='-', color='blue', label='Execution Time')
    # # plt.plot(number_of_packets, generator_execution_time, marker='o', linestyle='-', color='blue', label='Generation Time')

    # # Add labels and title
    # plt.xlabel('Number of Packets')
    # plt.ylabel('Execution Time (s)')
    # plt.title('Execution Time vs. Number of Packets')
    # # plt.ylabel('Generation Time (s)')
    # # plt.title('Generation Time vs. Number of Packets')
    # plt.legend()

    # # Display grid and show the plot
    # plt.grid(True)
    # plt.show()

    # Create the first graph
    plt.figure(figsize=(10, 5))  # Set the figure size
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st graph
    plt.plot(number_of_packets, total_execution_time, marker='o', label='Execution Time', color='blue')
    plt.title("Execution Time vs. Number of Packets")
    plt.xlabel('Number of Packets')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)

    # Create the second graph
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd graph
    plt.plot(number_of_packets, generator_execution_time, marker='s', label='Generation Time', color='green')
    plt.title("Generation Time vs. Number of Packets")
    plt.xlabel('Number of Packets')
    plt.ylabel('Generation Time (s)')
    plt.legend()
    plt.grid(True)

    # Show both graphs
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-g', '--generator',   
        type=int, 
        default=0, 
        help='Specify generator: 0-Grammarinator, 1-CustomGenerator. Default is 0')
    
    parser.add_argument(
        '-d', '--debug',      
        type=int, 
        default=0, 
        help='Specify debug flag: 0-False, 1-True. Default is 0')
    
    parser.add_argument(
        '-e', '--evaluation',      
        type=int, 
        default=0, 
        help='Specify evaluation method: 0-Directory, 1-AStar. Default is 0')
    
    parser.add_argument(
        '-p', '--packets',     
        type=int, 
        default=1, 
        help='Specify number of packets. Default is 1')
    
    args = parser.parse_args()
    # main(args)

    
    ipv6_eval = IPV6_Eval(gen_choice  = args.generator,
                            debug       = args.debug,    
                            num_packets = args.packets)
    path = ipv6_eval.send_packet_via_astar()
    print(path)
    print(len(path))