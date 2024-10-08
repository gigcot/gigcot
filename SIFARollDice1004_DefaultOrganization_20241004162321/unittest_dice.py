# unittest
"""
This test case checks the roll method in Dice class.
"""
import unittest
class TestDice(unittest.TestCase):
    def test_roll(self):
        # Arrange: Create a Dice instance
        dice = Dice()
        # Act: Call the roll method and verify the returned value
        result = dice.roll()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
    def test_roll_with_invalid_input(self):
        # Arrange: Create an invalid input (e.g., a string)
        invalid_input = "abc"
        # Act: Call the roll method with the invalid input and verify the behavior
        with self.assertRaises(TypeError):
            Dice(invalid_input).roll()