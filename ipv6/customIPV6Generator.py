#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate random IPv6 addresses."""

import argparse
import ipaddress
import random
from pathlib import Path


class myIPV6():
    def __init__(self):
        self.chars = '0123456789abcdef'

    def IPV6_group(self, ):
        gr = ''
        for x in range(4):
            gr = gr + random.choice(self.chars)

        if gr == "0000":
            gr = ":"

        return gr

    def generateAddress(self, num=1, *groups):
        ls = []
        pre = ''
        count = 0
        for x in groups:
            st = ""
            if len(x) == 4:
                for char in x:
                    if char not in self.chars:
                        break
                    else:
                        st = st + char

                    if len(st) == 4:
                        if st == "0000":
                            pre = pre + ":"
                        else:
                            pre = pre + st + ":"
                        count += 1

        for x in range(num):
            addr = ''
            for x in range((7-count)):
                group = self.IPV6_group()
                addr = addr + group + ":"

            addr = addr + self.IPV6_group()
            try:
                ipaddress.IPv6Address(addr)
            except ipaddress.AddressValueError:
                num = num + 1

            addr = pre + addr
            ls.append(addr)

        return ls


# parser = argparse.ArgumentParser(description=__doc__)

# parser.add_argument(
#     "-n", "--num",
#     type=int,
#     default=1,
#     help="number of IP addresses to generate (default: 1)",
# )

# _suggested_output_directory = Path.cwd() / "tests" / "custom_generator"
# parser.add_argument(
#     "-o", "--output",
#     type=Path,
#     nargs="?",
#     const=_suggested_output_directory,
#     help="output directory for generated IP addresses. If flag is not "
#          "present, no files are written. If flag is present without an "
#          "argument, a default output directory is used: "
#          f"{_suggested_output_directory}. Else, the argument is used as "
#          "the output directory.",
# )

# parser.add_argument(
#     "-g", "--groups",
#     type=str,
#     nargs="*",
#     default=[],
#     help="groups to include in the generated IP addresses. Each group "
#          "should be a 4-character hexadecimal string. If not provided, "
#          "random groups are generated. Invalid groups are ignored.",
# )


def main(args=None) -> None:
    # args = parser.parse_args()
    num_tests:        int         = args['num']
    output_directory: Path | None = args['output']
    digit_groups:     list[str]   = args['groups']

    ip = myIPV6()
    addresses = ip.generateAddress(num_tests, *digit_groups)

    if output_directory is None:
        for address in addresses:
            print(address)
        return

    output_directory.mkdir(parents=True, exist_ok=True)
    for test_index, address in enumerate(addresses):
        test_num = test_index
        output_path = output_directory / f"test_{test_num}.txt"
        output_path.write_text(address)
        print(address, output_path, sep="\t")


if __name__ == "__main__":
    
    arguments = {'num': 1,
                    'output': Path('tests/customgen_output'),
                    'groups': []}
    main(arguments)
