import time
import subprocess
import os
import shutil
import json
import random
import argparse
from pathlib import Path

import customIPV6Generator


IPV6_EXEC_BASH       = './ipv6_gram_gen_script_auto.sh'
IPV6_GRAM_TEST_DIR   = 'tests/grammarinator_output'
IPV6_CUST_TEST_DIR   = 'tests/customgen_output'
IPV6_TEST_PACKET_DIR = 'tests/packets'

IPV6_PROCESS_BASH_LINE = \
f"""
main_dir=$(dirname "$(realpath "$0")")  
grammarinator-process ipv6.g4 -o ipv6/
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

        self.true_start_time = time.perf_counter()
        self.true_print_time = 0

        self.start_time = self.true_start_time
        self.print_time = 0
        self.generator_time  = 0

        self.packet_id      = 0
        self.address        = address
        self.ipv4_address   = None
        self.expand_address = None

        self.packet_dest = ''

        self.num_groups = 8
        self.sleep_time = sleep_time

        self.grammarinator_gen_bash_line = f'grammarinator-generate ipv6Generator.ipv6Generator -r start -o "{IPV6_GRAM_TEST_DIR}/test_{self.packet_id}.txt" -n 1 --sys-path "$main_dir"'

    def execute(self):
        """
            Main execution function.
            Parameters: None
            Output: None
        """
        self.cleanup()

        for packet_id in range(self.num_packets):
            if self.debug: print()
            if self.debug: print(f"========= Packet {self.packet_id} =========")

            self.grammarinator() if self.gen_choice == 0 else self.custom_generator()
            self.read_grammarinator_txt()
            self.decode_ipv6()
            self.send_packet()
            
            time.sleep(self.sleep_time)
            if self.debug: self.report_time()

            self.packet_id = packet_id + 1
            self.reset()

        if self.debug: print()
        self.report_time(final=True)

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
        customIPV6Generator.main(arguments)

    def read_grammarinator_txt(self):
        """
            Read grammarinator output file and save content.
            Parameters: None
            Output: None
        """
        try:
            # Open the file and read all its content
            with open(F'{IPV6_GRAM_TEST_DIR if self.gen_choice == 0 else IPV6_CUST_TEST_DIR}/test_{self.packet_id}.txt', "r") as file:
                self.address = file.read()

            if self.debug: 
                start = time.perf_counter()
                print(f"Grammarinator Output: {self.address}")
                self.print_time += time.perf_counter() - start

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

    def send_packet(self):
        """
            Simulate sending packet over network given IP address.
            Parameters: None
            Output: None
        """
        self.packet_dest += IPV6_TEST_PACKET_DIR + '/' + ''.join([group + '/' for group in self.expand_address]).rstrip('/')

        if not (os.path.exists(self.packet_dest) or os.path.isdir(self.packet_dest)): os.makedirs(self.packet_dest)
        
        with open(self.packet_dest + '/storage.json', 'w') as packet_file:
            packet = {
                "packet_id": self.packet_id,
                "destination_ip": ''.join(self.expand_address),
                "payload_size": random.randint(20, 1500),
                "timestamp": time.time(),
            }
            
            packet_file.write(json.dumps(packet) + "\n")

    def report_time(self,
                    final: bool = False):
        """
            Prints execution time.
            Parameters: 
                final (bool) : Final flag
            Output: None
        """
        print(f"Time elapsed: {(time.perf_counter()-self.start_time-self.print_time):.6f} seconds" if not final else\
              f"Total time  : {(time.perf_counter()-self.true_start_time-self.true_print_time):.6f} seconds \nAverage time: {(time.perf_counter()-self.true_start_time-self.true_print_time)/(self.num_packets):.6f} seconds\nGenerator time: {self.generator_time:.6f} seconds\n") 

    def reset(self):
        """
            Resets parameters between packets.
            Parameters: None
            Output: None
        """
        self.true_print_time += self.print_time

        self.start_time = time.perf_counter()
        self.print_time = 0

        self.address = None
        self.ipv4_address = None
        self.expand_address = None

        self.num_groups = 8

        self.packet_dest = ''

        self.grammarinator_gen_bash_line = f'grammarinator-generate ipv6Generator.ipv6Generator  -r start -o "{IPV6_GRAM_TEST_DIR}/test_{self.packet_id}.txt" -n 1 --sys-path "$main_dir/ipv6"'

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

        os.makedirs(IPV6_GRAM_TEST_DIR)
        if self.debug: print(f"Directory created: {IPV6_GRAM_TEST_DIR}")

        os.makedirs(IPV6_CUST_TEST_DIR)
        if self.debug: print(f"Directory created: {IPV6_CUST_TEST_DIR}")

        os.makedirs(IPV6_TEST_PACKET_DIR)
        if self.debug: print(f"Directory created: {IPV6_TEST_PACKET_DIR}")


def main(args):
    ipv6_eval = IPV6_Eval(gen_choice  = args.generator,
                          debug       = args.debug,    
                          num_packets = args.packets)
    ipv6_eval.execute()


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
        '-p', '--packets',     
        type=int, 
        default=1, 
        help='Specify number of packets. Default is 1')
    
    args = parser.parse_args()
    main(args)
