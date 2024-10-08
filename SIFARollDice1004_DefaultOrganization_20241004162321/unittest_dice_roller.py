# unittest
"""
This test case checks the roll_dice method in DiceRoller class.
"""
import unittest
class TestDiceRoller(unittest.TestCase):
    def test_roll_dice(self):
        # Arrange: Create a DiceRoller instance
        dice_roller = DiceRoller()
        # Act: Call the roll_dice method and verify the returned value
        result = dice_roller.roll_dice()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
    def test_roll_dice_with_invalid_input(self):
        # Arrange: Create an invalid input (e.g., a string)
        invalid_input = "abc"
        # Act: Call the roll_dice method with the invalid input and verify the behavior
        with self.assertRaises(TypeError):
            DiceRoller(invalid_input).roll_dice()