# dice_game.py
'''
Dice Game Core File
-------------------
This file contains the core logic of the game, including the Game class and its related methods.
'''
import random
class Player:
    def __init__(self, name):
        '''
        Initializes a new player with a given name.
        Args:
            name (str): The name of the player.
        '''
        self.name = name
        self.score = 0
    def roll_dice(self):
        '''
        Rolls a dice and returns the result.
        Returns:
            int: The result of the dice roll.
        '''
        return random.randint(1, 6)
    def win_round(self):
        '''
        Increments the player's score by 1.
        '''
        self.score += 1
class Game:
    def __init__(self):
        '''
        Initializes a new game with two players.
        Args:
            None
        '''
        self.current_player = Player("Player 1")
        self.dice_rolled = False
        self.round_score = 0
    def roll_dice(self):
        '''
        Rolls the dice for the current player and updates the round score.
        If a six is rolled, the player wins the round.
        Args:
            None
        Returns:
            int: The result of the dice roll.
        '''
        if not self.dice_rolled:
            result = self.current_player.roll_dice()
            print(f"{self.current_player.name} rolled a {result}.")
            # Update the dashboard with the new score
            self.dashboard.update_score(result)
            # Check for a six and update the round score accordingly
            if result == 6:
                self.current_player.win_round()
                self.round_score += 1
            # Switch to the next player
            self.switch_player()
            return result
    def switch_player(self):
        '''
        Switches the current player.
        Args:
            None
        '''
        self.current_player = Player("Player 2" if self.current_player == "Player 1" else "Player 1")
class Dashboard:
    def __init__(self, game):
        '''
        Initializes a new dashboard for a given game.
        Args:
            game (Game): The game instance.
        '''
        self.game = game
    def update_score(self, result):
        '''
        Updates the dashboard with the new score.
        Args:
            result (int): The result of the dice roll.
        '''
        # Update the score label and value
        self.dashboard_ui.update_score_label(result)
class DashboardUI:
    def __init__(self, master):
        '''
        Initializes a new dashboard UI for a given game.
        Args:
            master (tk.Frame): The parent frame.
        '''
        self.master = master
    def update_score_label(self, result):
        '''
        Updates the score label with the new value.
        Args:
            result (int): The result of the dice roll.
        '''
        # Update the score label and value
        self.score_value.config(text=str(result))