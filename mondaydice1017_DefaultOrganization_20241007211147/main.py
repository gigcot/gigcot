# dice_game.py
'''
Dice Game File
-----------------
This file contains the implementation of the dice game logic.
'''
import threading
class Player:
    def __init__(self):
        self.score = 0
        self.lock = threading.Lock()
    def roll_dice(self):
        with self.lock:  # Acquire the lock before modifying score
            return self._roll_dice()
    def _roll_dice(self):
        # Simulate dice rolling logic here...
        return 1
class Game:
    def __init__(self):
        self.player = Player()
        self.score = 0
        self.lock = threading.Lock()
    def roll_dice(self):
        with self.lock:  # Acquire the lock before modifying score
            result = self.player.roll_dice()
            if result == 6:
                return "You won the round!"
            else:
                return f"You rolled a {result}"
if __name__ == "__main__":
    game = Game()
    print(game.roll_dice())