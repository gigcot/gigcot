# dashboard.py
'''
Dashboard File
-----------------
This file contains the implementation of the interactive dashboard.
'''
import tkinter as tk
class Dashboard:
    def __init__(self, master):
        self.master = master
        # Create a frame for the dashboard
        self.frame = tk.Frame(self.master)
        # Add widgets to the frame
        self.score_label = tk.Label(self.frame, text="Score:")
        self.score_value = tk.Label(self.frame, text="")
        # Pack the widgets
        self.frame.pack(fill="both", expand=True)
        self.score_label.pack()
        self.score_value.pack()
    def update_score(self, result):
        # Update the score label and value
        self.score_value.config(text=str(result))