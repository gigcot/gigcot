# LANGUAGE: Python
# DOCSTRING: Main entry point of the application.
#
# This file serves as the starting point for the roll dice app. It sets up the GUI and handles user interactions.
import tkinter as tk
from ddd import Domain, Entity
class RollDiceApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Roll Dice App")
        self.domain = Domain()
        # Create GUI widgets
        self.dice_label = tk.Label(self.root, text="Roll the dice!")
        self.roll_button = tk.Button(self.root, text="Roll", command=self.roll_dice)
        self.result_label = tk.Label(self.root, text="")
        # Layout GUI widgets
        self.dice_label.pack()
        self.roll_button.pack()
        self.result_label.pack()
    def roll_dice(self):
        # Create a new dice entity and roll it
        dice_entity = self.domain.create_entity("Dice", 0)
        result = dice_entity.roll()
        # Update the result label with the rolled value
        self.result_label.config(text=f"You rolled: {result}")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = RollDiceApp()
    app.run()