# dice_app.py
'''The GUI application for rolling dice.'''
import tkinter as tk  # Import tkinter correctly
from tkinter import ttk, Frame, Label, Button  # Correctly import necessary widgets
from roll_dice_controller import DiceRoller
class DiceApp(tk.Frame):  # Use tk.Frame instead of just Frame
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = DiceRoller()
        self.init_ui()
    def init_ui(self):
        self.header_label = Label(self, text="Roll Dice App", font=("Arial", 16))
        self.header_label.pack(fill=X)
        self.roll_button = Button(self, text="Roll", command=self.on_roll)  # Correctly import Button
        self.roll_button.pack(fill=X)
        self.result_label = Label(self, text="Result: ", font=("Arial", 12))  # Correctly import Label
        self.result_label.pack(fill=X)
    def on_roll(self):
        result = self.controller.roll_dice()
        self.result_label['text'] = f"Result: {result}"
# Rest of your code remains the same...