#!/usr/bin/env python3
# https://codechalleng.es/bites/102/

VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    while True:
        tmp = input("Input, please: ")
        if tmp == "quit":
            print("bye")
            break
        elif tmp in VALID_COLORS:
            print(tmp.lower())
        else:
            print("Not a valid color")
            continue


