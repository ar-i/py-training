#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Example Python CLI")

parser.add_argument("hacker_name", help="Enter the hacker name", type=str)
parser.add_argument("hacker_power", help="Enter the hacker name", type=int)
parser.add_argument("-bh", "--blackhat", required=False, default=False, action="store_true")
parser.add_argument("-wh", "--whitehat", required=False, default=True, action="store_true")
# The keyword "choices" allows for pre-definining valid choices for the
# argument
parser.add_argument("-ht", "--hackertype", choices=["whitehat", "blackhat",
"greyhat"])

args = parser.parse_args()
print(args)
print(args.hacker_name)
