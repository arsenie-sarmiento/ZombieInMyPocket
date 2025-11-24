import unittest
from model_after_pattern import GameTime, FormatDecorator, MessageDecorator

class TestGameTime(unittest.TestCase):

    def test_initial_time_string(self):
        game_time = GameTime(9)
        decorated_time = MessageDecorator(FormatDecorator(game_time), "The time is now")
        self.assertEqual(decorated_time.display_time(), "The time is now 09:00 AM")

    def test_get_current_time(self):
        game_time = GameTime(10)
        self.assertEqual(game_time.get_time(), 10)

    def test_time_increase(self):
        game_time = GameTime(9)
        game_time.increase_time()
        self.assertEqual(game_time.get_time(), 10)

    def test_time_validity(self):
        game_time = GameTime(9, 12)
        self.assertTrue(game_time.is_time_valid())
        game_time._time = 12
        self.assertFalse(game_time.is_time_valid())

    def test_am_pm_boundary(self):
        game_time = GameTime(12)
        decorated_time = FormatDecorator(game_time)
        self.assertIn("PM", decorated_time.display_time())
        game_time._time = 11
        self.assertIn("AM", decorated_time.display_time())

if __name__ == "__main__":
    unittest.main()
