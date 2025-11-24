import unittest
from src.model_after_pattern import GameTime, FormatDecorator, MessageDecorator, GameTimeDecorator

class MockDecorator(GameTimeDecorator):
    """A minimal concrete decorator for testing delegation."""
    def display_time(self) -> str:
        return self._component.display_time()
    
class TestGameTime(unittest.TestCase):
    def setUp(self):
        self.game_time = GameTime()
        self.mock_decorator = MockDecorator(self.game_time)
        self.format_decorator = FormatDecorator(self.game_time)

    # ----------------------------------------------------------------------
    # BASIC GAME TIME TESTS
    # ----------------------------------------------------------------------

    def test_initial_time(self):
        expected = 9
        self.assertEqual(self.game_time.get_time(), expected)

    def test_get_current_time(self):
        game_time = GameTime(10)
        self.assertEqual(game_time.get_time(), 10)

    def test_time_increase(self):
        self.game_time.increase_time()
        self.assertEqual(self.game_time.get_time(), 10)

    def test_time_validity(self):
        game_time = GameTime(9, 12)
        self.assertTrue(game_time.is_time_valid())
        game_time._time = 12
        self.assertFalse(game_time.is_time_valid())

    # ----------------------------------------------------------------------
    # DECORATOR DELEGATION TESTS
    # ----------------------------------------------------------------------

    def test_get_time_delegation(self):
        # Delegation from decorator should match core component
        self.assertEqual(self.mock_decorator.get_time(), self.game_time.get_time())
        self.assertEqual(self.format_decorator.get_time(), self.game_time.get_time())

    def test_increase_time_delegation(self):
        # Increment time through decorator should affect core component, starting time defaults to 9
        self.mock_decorator.increase_time()
        
        expected_time = 10
        new_time = self.game_time.get_time()
        self.assertEqual(new_time, expected_time)

        self.format_decorator.increase_time()
        
        expected_time = 11
        new_time = self.game_time.get_time()
        self.assertEqual(new_time, expected_time)

    def test_display_time_delegation(self):
        # The mock decorator should pass through display_time
        self.assertEqual(self.mock_decorator.display_time(), self.game_time.display_time())
        
        # FormatDecorator should add AM/PM formatting
        formatted = self.format_decorator.display_time()
        print(formatted)
        self.assertIn("AM", formatted)
        self.assertTrue(formatted.startswith("09:00"))

    # ----------------------------------------------------------------------
    # FORMAT DECORATOR TESTS
    # ----------------------------------------------------------------------

    def test_format_decorator_output(self):
        """Basic formatted output for default start time 9."""
        formatted = self.format_decorator.display_time()
        expected = "09:00 AM"
        self.assertEqual(formatted, expected)
        
    def test_format_12pm_boundary(self):
        """12 should be displayed as 12:00 PM."""
        self.game_time._time = 12
        formatted = self.format_decorator.display_time()
        self.assertEqual(formatted, "12:00 PM")

    def test_format_midnight_boundary(self):
        """0 should display as 12:00 AM."""
        self.game_time._time = 0
        formatted = self.format_decorator.display_time()
        self.assertEqual(formatted, "12:00 AM")

    def test_format_afternoon_conversion(self):
        """13 should become 01:00 PM."""
        self.game_time._time = 13
        formatted = self.format_decorator.display_time()
        self.assertEqual(formatted, "01:00 PM")

    # ----------------------------------------------------------------------
    # MESSAGE DECORATOR COMBINATION TEST
    # ----------------------------------------------------------------------

    def test_initial_time_string(self):
        game_time = GameTime(9)
        custom_message = "The time is now"
        decorated_time = MessageDecorator(FormatDecorator(game_time), custom_message)
        self.assertEqual(decorated_time.display_time(), f"{custom_message} 09:00 AM")

    def test_am_pm_boundary(self):
        game_time = GameTime(12)
        decorated_time = FormatDecorator(game_time)
        self.assertIn("PM", decorated_time.display_time())
        game_time._time = 11
        self.assertIn("AM", decorated_time.display_time())

if __name__ == "__main__":
    unittest.main()
