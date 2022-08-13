#!/usr/bin/env python3

class Person:
    'Person base class'
    # This is still cringe ..
    wants_to_hack = True

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.getter
    def age(self):
        return self.__age

    @age.deleter
    def age(self):
        del self.__age

    # 'cls' is an important keyword here because it allows for accessing class
    # attributes
    @classmethod
    def wants_to(cls):
        return cls.want_to_hack

    @classmethod
    def bob_factory(cls):
        return cls("bob", 30)

    # A static method does not take any input because it does not know anything
    # about the class, nor does it even need to
    @staticmethod
    def static_print():
        print("I am the same!")

    def print_name(self):
        print(f"My name is {self.name}")

    def print_age(self):
        print(f"My age is {self.__age}")

    def birthday(self):
        self.__age += 1

bob = Person("bob", 30)
print(bob.age)

# Static methods can either be called directly or by / for an instance of a
# class
Person.static_print()
bob.static_print()
