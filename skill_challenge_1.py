#!/usr/bin/python3
import random

class Student:
    educational_platform = "Udemy"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        greetings = [f"Hi, I'm {self.name}", 
                f"Hey there, my name is {self.name}",
                f"Hi. Oh my name is {self.name}"]

        return random.choice(greetings)

sam = Student("sam", 24)
mary = Student("Mary", 23)
arnold = Student("Arnold", 22)
alex = Student("Alex", 25)

print(sam.greet())
print(mary.greet())
print(arnold.greet())
print(alex.greet())
