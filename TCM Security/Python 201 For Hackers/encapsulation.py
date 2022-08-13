#!/usr/bin/env python3

class Person:
    'Person base class'
    # This is still cringe ..
    wants_to_hack = True

    def __init__(self, name, age):
        # The double underscore means that this is a "private" variable /
        # attribute, for lack of a better wording.
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def print_name(self):
        print(f"My name is {self.name}")

    def print_age(self):
        print(f"My age is {self.__age}")

    def birthday(self):
        self.__age += 1

bob = Person("age", 30)
print(bob.get_age())

# Circumvent the encapsulation
print(bob.__dict__)
bob._Person__age = 50
print(bob.get_age())
