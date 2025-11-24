import unittest
from src.model import GameTime

class TestGameTime(unittest.TestCase):

    def test_initial_time_string(self):
        game_time = GameTime(9)
        self.assertEqual(str(game_time), "The time is now 09:00PM")

    def test_get_current_time(self):
        game_time = GameTime(10)
        self.assertEqual(game_time.get_current_time(), 10)

    def test_time_increase(self):
        game_time = GameTime(9)
        game_time.increase_time()
        self.assertEqual(game_time.get_current_time(), 10)

    def test_time_validity(self):
        game_time = GameTime(9, 12)
        self.assertTrue(game_time.is_time_valid())
        game_time._time = 12
        self.assertFalse(game_time.is_time_valid())

    def test_am_pm_boundary(self):
        game_time = GameTime(12)
        self.assertIn("AM", str(game_time))
        game_time._time = 11
        self.assertNotIn("AM", str(game_time))


if __name__ == "__main__":
    unittest.main()
