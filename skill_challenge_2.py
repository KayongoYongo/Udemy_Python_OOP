#!/usr/bin/python3

import random
import string

class Password:
    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length
        self.password = self.generate_password()
    
    def generate_password(self):
        letters = string.ascii_letters
        digits = string.digits
        punctuations = string.punctuation

        # Set maximum lengths for each strength
        max_lengths = {
            "low": 8,    # Maximum length for low strength
            "mid": 12,    # Maximum length for mid strength
            "high": 16    # Maximum length for high strength
        }

        # Check if the specified length exceeds the maximum allowed
        if self.length is not None and self.length > max_lengths.get(self.strength, 20):
            return f"Password length exceeded for the specified strength"

        if self.strength == "low":
            self.length = self.length or 8
            return ''.join(random.choice(letters) for _ in range(self.length))

        if self.strength == "mid":
            self.length = self.length or 12
            return ''.join(random.choice(letters + digits) for _ in range(self.length))

        if self.strength == "high":
            self.length = self.length or 16
            return ''.join(random.choice(letters + digits + punctuations) for _ in range(self.length))

    def show_input_universe(self):
        letters = string.ascii_letters
        digits = string.digits
        punctuations = string.punctuation

        letters_dict = {"letters": list(letters)}
        digits_dict = {"digits": list(digits)}
        punctuations = {"punctuations": list(punctuations)}

        # Combine all dictionaries into one
        return {**letters_dict, **digits_dict, **punctuations_dict}

    def get_password(self):
        return self.password

# Example usage
p1 = Password()
print(p1.get_password())

p2 = Password("low", 6)
print(p2.get_password())

p3 = Password("mid", 13)
print(p3.get_password())

p4 = Password("high", 15)
print(p4.get_password())

