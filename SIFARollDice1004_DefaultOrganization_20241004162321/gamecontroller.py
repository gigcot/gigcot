# gamecontroller.py (Removed)
'''The controller for handling game logic and user interactions.'''
from dice import Dice
class GameController:
    def __init__(self):
        pass
    def roll_dice(self) -> int:
        num_dice = 2
        num_sides = 6
        dice = [Dice(num_sides) for _ in range(num_dice)]
        rolls = self.roll_dice_multiple(dice)
        result = sum(rolls)
        return result
    def roll_dice_multiple(self, dice: list) -> list:
        # Simplified using a list comprehension
        return [d.roll() for d in dice]
    def calculate_result(self, rolls: list) -> int:
        return sum(rolls)
    def generate_roll_history(self) -> str:
        num_dice = 10
        num_sides = 6
        dice = [Dice(num_sides) for _ in range(num_dice)]
        rolls = self.roll_dice_multiple(dice)
        roll_history = "\n".join(map(str, rolls))
        return f"Roll History:\n{roll_history}"