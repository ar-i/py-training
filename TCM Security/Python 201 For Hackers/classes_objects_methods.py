#!/usr/bin/env python3

class Person:

    # .. cringe.
    wants_to_hack = true

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f"My name is {self.name}.")

    def print_age(self):
        print(f"My name is {self.age}.")

    def birthday(self):
        self.age += 1

bob = Person("Bob", 30)
alice = Person("Alice", 20)
malory = Person("Malory", 50)
