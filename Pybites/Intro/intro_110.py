#!/usr/bin/env python3
# https://codechalleng.es/bites/110/

def divide_numbers(numerator, denominator):
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError as e:
        print(e)
        raise ValueError()
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 0
			
print(divide_numbers(10,"1"))
