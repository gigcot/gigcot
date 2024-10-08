# LANGUAGE: Python
# DOCSTRING: Entity class implementation.
#
# This file contains the Entity class implementation.
class Entity:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        # Initialize a history list to store previous states of the entity
        self.history = [value]
    def roll(self):
        # Simulate a roll by returning a random number between 1 and 6
        return (self.value + 5) % 6 + 1
    def update_history(self, new_value):
        # Update the entity's history list with the new state
        self.history.append(new_value)
    def get_previous_states(self):
        # Return a list of previous states of the entity
        return self.history