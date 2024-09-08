#!/bin/python3

class Car:
    door = 2
    wheels = 4

# __dict__ is an internal dictionary that stores the attributes (or variables) of an object.
print(Car.__dict__)

Car.door = 5
Car.make = 'Toyota'
print(Car.__dict__)
