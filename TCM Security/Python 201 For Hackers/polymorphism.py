#!/usr/bin/env python3

# Same function, different input
print(len("string"))
print(len(['l', 'i', 's', 't']))

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

class Hacker(Person):
    # This means "Person" is an "argument" - Hacker is referencing it
    def __init__(self, name, age, cves):
        # super() allows accessing the method from the parent class without
        # explicitly calling it .. although I don't quite yet know what that
        # exactly means on a technical level
        super().__init__(name, age)
        self.cves = cves

        # This "overrides" the "print_name" method defined in the parent class.
        def print_name(self):
            print(f"My name is {self.name} and I have {self.cves} CVES.")

        def total_cves(self):
            return self.cves

def obj_dump(object):
    object.print_name()
    print(object.age)
    object.birthday()
    print(object.age)
    print(object.__class__)
    print(object.__class__.__name__)

bob = Person("bob", 30)
alice = Hacker("alice", 25, 10)

# Different objects are being put into the function; the function does not
# care
obj_dump(bob)
obj_dump(alice)
