#!/usr/bin/env python3
# https://codechalleng.es/bites/104/

MESSAGE = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=MESSAGE):
	tmp = message.split("\n")
	return "|".join(tmp)
