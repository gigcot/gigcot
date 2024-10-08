# main.py
'''The entry point of the application.'''
import tkinter as tk  # Import tkinter correctly
from dice_app import DiceApp
def run_app():
    root = tk.Tk()
    app = DiceApp(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
if __name__ == "__main__":
    run_app()