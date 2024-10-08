# unittest
"""
This test case checks the roll_dice method in GameController class.
"""
import unittest
class TestGameController(unittest.TestCase):
    def test_roll_dice(self):
        # Arrange: Create a GameController instance
        game_controller = GameController()
        # Act: Call the roll_dice method and verify the returned value
        result = game_controller.roll_dice()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 12)
    def test_roll_dice_with_invalid_input(self):
        # Arrange: Create an invalid input (e.g., a string)
        invalid_input = "abc"
        # Act: Call the roll_dice method with the invalid input and verify the behavior
        with self.assertRaises(TypeError):
            GameController(invalid_input).roll_dice()