#!/usr/bin/python3

import random
import string

class Password:
    def __init__(self, strength, length):
        self.strength = strength
        self.length = length
    
    def generate_password(self):
        letters = string.ascii_letters
        digits = string.digits
        punctuations = string.punctuation

        if self.strength == "low" and self.length is None:
            self.length = 8
            return ''.join(random.choice(letters) for _ in range(self.length))

        if self.strength == "mid" and self.length is None:
            self.length = 12
            return ''.join(random.choice(letters + digits) for _ in range(self.length))

        if self.strength == "high" and self.length is None:
            self.length = 16
            return ''.join(random.choice(letters + digits + punctutations) for _ in range(self.length))

    def show_input_universe():
        letters = string.ascii_letters
        digits = string.digits
        punctuations = string.punctuation

        letters_dict = {"letters": list(letters)}
        digits_dict = {"digits": list(digits)}
        punctuations = {"punctuations": list(punctuations)}

        # Combine all dictionaries into one
        return {**letters_dict, **digits_dict, **punctuations_dict}
