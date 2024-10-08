# dice.py
'''
Core domain entity classes for the dice rolling game.
'''
class Dice:
    '''
    Represents a single six-sided die.
    Attributes:
        faces (int): The number of sides on the die (default=6).
        result (int): The outcome of a roll (None by default).
    '''
    def __init__(self):
        self.faces = 6
        self.result = None
    def roll(self):
        import random
        self.result = random.randint(1, self.faces)
class Roll:
    '''
    Represents a set of dice rolls.
    Attributes:
        dice_count (int): The number of dice in the roll.
        results (list): A list of individual roll outcomes.
    '''
    def __init__(self, dice_count):
        self.dice_count = dice_count
        self.results = [None] * dice_count
    def add_roll(self, result):
        if len(self.results) < self.dice_count:
            self.results.append(result)
        else:
            raise ValueError("Maximum number of rolls reached")
class Player:
    '''
    Represents a player's collection of rolls.
    Attributes:
        rolls (list): A list of individual roll outcomes.
    '''
    def __init__(self):
        self.rolls = []
    def add_roll(self, roll):
        self.rolls.append(roll)
    def calculate_sum(self):
        return sum([x for x in self.rolls if isinstance(x, int)])