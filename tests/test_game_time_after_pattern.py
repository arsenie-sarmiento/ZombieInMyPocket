import unittest
from model_after_pattern import GameTime, FormatDecorator, MessageDecorator, GameTimeDecorator

class MockDecorator(GameTimeDecorator):
    """A minimal concrete decorator for testing delegation."""
    def display_time(self) -> str:
        return self._component.display_time()
    
class TestGameTime(unittest.TestCase):
    def setUp(self):
        self.game_time = GameTime()
        self.decorator = MockDecorator(self.game_time)
        self.format_decorator = FormatDecorator(self.game_time)

    def test_start_time(self):
        self.assertEqual(self.game_time.get_time(), 9)

    def test_get_time_delegation(self):
        # Delegation from decorator should match core component
        self.assertEqual(self.decorator.get_time(), self.game_time.get_time())
        self.assertEqual(self.format_decorator.get_time(), self.game_time.get_time())

    def test_increase_time_delegation(self):
        # Increment time through decorator should affect core component
        self.decorator.increase_time()
        self.assertEqual(self.game_time.get_time(), 10)

        self.format_decorator.increase_time()
        self.assertEqual(self.game_time.get_time(), 11)

    def test_display_time_delegation(self):
        # Dummy decorator should pass through display_time
        self.assertEqual(self.decorator.display_time(), self.game_time.display_time())
        
        # FormatDecorator should add AM/PM formatting
        formatted = self.format_decorator.display_time()
        print(formatted)
        self.assertIn("AM", formatted)  # since initial hour = 09
        self.assertTrue(formatted.startswith("09:00"))

    def test_format_12pm_boundary(self):
        # Test correct PM display at 12
        self.game_time._time = 12
        formatted = self.format_decorator.display_time()
        self.assertIn("PM", formatted)
        self.assertTrue(formatted.startswith("12:00"))

    def test_format_midnight_boundary(self):
        # Test correct AM display at 0
        self.game_time._time = 0
        formatted = self.format_decorator.display_time()
        self.assertIn("AM", formatted)
        self.assertTrue(formatted.startswith("12:00"))

    def test_initial_time_string(self):
        game_time = GameTime(9)
        custom_message = "The time is now"
        decorated_time = MessageDecorator(FormatDecorator(game_time), custom_message)
        self.assertEqual(decorated_time.display_time(), f"{custom_message} 09:00 AM")

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
