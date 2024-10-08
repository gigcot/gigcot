# roll_dice_controller.py
'''The controller for rolling dice.'''
class DiceRoller:
    def roll_dice(self):
        import random  # Import necessary module
        return random.randint(1, 6)