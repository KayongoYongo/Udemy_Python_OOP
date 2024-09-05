#!/bin/python3

class Car:
    def __init__(self, name):
        self.name = name
# A class is a blueprint that represents a type of object
# Even the simplest class has state and behaviour
# Calling the class creates instances of that class

# First instance of a car
mazda = Car("Mazda")

# Second instance of a car
honda = Car("Honda")

print(mazda)
print(honda)

"""
After printing, the two instances will be
stored in separate areas of memory. These two instances
of a car are considered different by default.
"""

print(f'{honda.name} == {mazda.name} : Result{honda == mazda}')
