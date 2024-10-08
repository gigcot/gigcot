# python
'''
This file contains unit tests for the dice game module.
'''
import unittest
from dice_game import Player, Game
class TestPlayer(unittest.TestCase):
    def test_init(self):
        # Arrange: Create a new player instance with a name
        player = Player("John")
        # Act: Verify that the player's name is set correctly
        self.assertEqual(player.name, "John")
    def test_roll_dice(self):
        # Arrange: Create a new game instance with a player
        game = Game()
        game.add_player("Player 1")
        # Act: Roll the dice for the player
        result = game.roll_dice()
        # Assert: Verify that the rolled value is within the expected range
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
class TestGame(unittest.TestCase):
    def test_init(self):
        # Arrange: Create a new game instance with no players
        game = Game()
        # Act: Verify that the game has an empty list of players
        self.assertEqual(game.players, [])
    def test_add_player(self):
        # Arrange: Create a new game instance with one player
        game = Game()
        game.add_player("Player 1")
        # Act: Add another player to the game
        game.add_player("Player 2")
        # Assert: Verify that the game has two players
        self.assertEqual(game.players, ["Player 1", "Player 2"])