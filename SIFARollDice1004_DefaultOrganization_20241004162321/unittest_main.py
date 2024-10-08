import unittest
from GameController import GameController
class TestGameController(unittest.TestCase):
    def setUp(self):
        self.controller = GameController()
    def test_init_ui(self):
        # Arrange: Set up the testing environment and initialize necessary inputs.
        self.controller.init_ui()
        # Act: Call the init_ui method to execute the behavior.
        self.controller.pack(fill="both", expand=True)
        # Assert: Verify that the actual results match the expected outcomes using assertions.
        self.assertIsNotNone(self.controller.game_label)
        self.assertIsNotNone(self.controller.roll_button)
        self.assertIsNotNone(self.controller.result_label)
    def test_on_roll(self):
        # Arrange: Set up the testing environment and initialize necessary inputs.
        result = self.controller.roll_dice()
        # Act: Call the on_roll method to execute the behavior.
        self.controller.on_roll()
        # Assert: Verify that the actual results match the expected outcomes using assertions.
        self.assertEqual(self.controller.result_label['text'], f"Result: {result}")
class TestDiceRoller(unittest.TestCase):
    def test_roll_dice(self):
        # Arrange: Set up the testing environment and initialize necessary inputs.
        dice_roller = GameController()
        # Act: Call the roll_dice method to execute the behavior.
        result = dice_roller.roll_dice()
        # Assert: Verify that the actual results match the expected outcomes using assertions.
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
class TestDice(unittest.TestCase):
    def test_roll(self):
        # Arrange: Set up the testing environment and initialize necessary inputs.
        dice = GameController()
        # Act: Call the roll method to execute the behavior.
        result = dice.roll()
        # Assert: Verify that the actual results match the expected outcomes using assertions.
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
class TestGameController(unittest.TestCase):
    def test_roll_dice(self):
        # Arrange: Set up the testing environment and initialize necessary inputs.
        game_controller = GameController()
        # Act: Call the roll_dice method to execute the behavior.
        result = game_controller.roll_dice()
        # Assert: Verify that the actual results match the expected outcomes using assertions.
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 12)
if __name__ == '__main__':
    unittest.main()