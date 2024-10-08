# dice.py
'''A single die with its properties and methods.'''
class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self) -> int:
        import random
        return random.randint(1, self.num_sides)