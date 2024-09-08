#!/bin/python3

class Car:
    door = 4
    wheel = 5

    def drive(self):
        return f'This car is red'

Mercedes = Car()

print(Mercedes.drive())
