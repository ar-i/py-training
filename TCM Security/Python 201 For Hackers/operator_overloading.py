#!/usr/bin/env python3

class Person:
    'Person base class'
    # This is still cringe ..
    wants_to_hack = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f"My name is {self.name}")

    def print_age(self):
        print(f"My age is {self.age}")

    def birthday(self):
        self.age += 1

    # This built-in function, in the default setting, represents the class
    # objects as a string - if it's not defined, then it defaults to the
    # __repr__ method, which returns a string that describes the pointer of the
    # object.
    #
    # Here it's modified so that it returns some attributes of / information
    # about the object instead.
    def __str__(self):
        return "My name is {} and I am {} years old.".format(self.name, self.age)

    # This overloads the "+"-operator so it returns the age of the instance
    # plus the age of another instance of the "Person"-class
    def __add__(self, other):
        return self.age + other.age
    
    # This overloads the "lt"-operator so the two instances of an object can be
    # compared based on their age.
    def __lt__(self, other):
        return self.age < other.age

bob = Person ("bob", 30)
alice = Person("alice", 35)
print(bob + alice)

# returns True
print (bob < alice)
# returns False
print (alice < bob)
