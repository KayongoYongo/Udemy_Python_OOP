#!/usr/bin/python3

class Fruit:
    """
    The fruit class is just an example. 
    This docstring is used to document the code.
    It is a pep8 standard.
    """

    seed = 1
    skin = 'Edible'

    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def flavor(self):
        return f"This fruit is a {self.name}. It is {self.taste}"

    @staticmethod
    def new_taste():
        return f"THere are 5 fruits of this kind"

    @classmethod
    def new_number(cls):
        return f"This fruit has {cls.seed} seed(s) and the skin is {cls.skin}"

banana = Fruit("Banana", "Yellow", "sweet")
lime = Fruit("Lime", "Green", "Bitter")

print(banana.flavor())
print(banana.new_taste())
print(lime.flavor())
print(lime.new_taste())
print(Fruit.new_number())
print(Fruit.__dict__)
