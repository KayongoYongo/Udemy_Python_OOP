#!/bin/python3

class Car:
    def __init__(self, name):
        self.name = name

# First instance of a car
mazda = Car()

# Second instance of a car
honda = Car()

print(mazda)
print(honda)

"""
After printing, the two instances will be
stored in separate areas of memory. These two instances
of a car are considered different by default.
"""

print(f'{honda.__name__} == {mazda.__name__} : Result{honda == mazda}')
