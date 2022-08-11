#!/usr/bin/env python3

def prettify(function):
    def pretty():
        print("*" * 10)
        function()
        print("*" * 10)
    return pretty

@prettify
def print_string():
    print("Hey!")

# Relying on the @notation ..
print_string()

# Calling prettify() directly ..
prettify(print_string())
