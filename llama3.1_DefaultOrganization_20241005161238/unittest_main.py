import unittest
class TestPlayer(unittest.TestCase):
    def test_add_player_roll(self):
        player = Player()
        rolls = [1, 2, 3]
        player.add_rolls(rolls)
        self.assertEqual(player.calculate_sum(), sum(rolls))
    def test_add_player_roll_empty_input(self):
        player = Player()
        with self.assertRaises(ValueError):
            player.add_roll([])
    def test_add_player_roll_non_integer_values(self):
        player = Player()
        rolls = ['a', 4]
        with self.assertRaises(ValueError):
            player.add_rolls(rolls)
    def test_add_player_roll_invalid_type(self):
        player = Player()
        rolls = "hello"
        with self.assertRaises(TypeError):
            player.add_rolls(rolls)
    def test_calculate_sum(self):
        player = Player()
        rolls = [1, 2, 3]
        player.add_rolls(rolls)
        self.assertEqual(player.calculate_sum(), sum(rolls))
if __name__ == "__main__":
    unittest.main()