#!/usr/bin/env python3
# https://codechalleng.es/bites/107/

def filter_positive_even_numbers(numbers):
	results = [ x for x in numbers if x > 0 and x % 2 == 0 ]
	return results

""" Receives a list of numbers, and returns a filtered list of only the numbers
that are both positive and even (divisible by 2), try to use a list
comprehension."""
