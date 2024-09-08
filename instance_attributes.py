#!/usr/bin/python3

# A car class
class Car:

    def __init__(self, make, color, doors):
        self.make = make
        self.color = color
        self.doors = doors

    def drive(self):
        return f"The car is a {self.color}, {self.make}.It has {self.doors} doors."

toyota = Car("Toyota", "Black", 2)
honda = Car("Hyundai", "White", 4)

print(toyota.drive())
print(honda.drive())
