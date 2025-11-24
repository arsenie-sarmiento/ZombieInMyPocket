from ..interfaces import GameTimeComponent
# from .custom_message_decorator import MessageDecorator
# from .format_decorator import FormatDecorator

class GameTime(GameTimeComponent):
    """Concrete Component: Core game time logic without formatting."""
    
    _INCREMENT = 1

    def __init__(self, start_time: int = 9, end_time: int = 12):
        self._time = start_time
        self._start_time = start_time
        self._end_time = end_time

    def get_time(self) -> int:
        """Get the current game time."""
        return self._time

    def increase_time(self) -> None:
        """Increase the current game time by the defined increment."""
        self._time += self._INCREMENT

    def display_time(self) -> str:
        """Return the current game time as a formatted string"""
        return f"{self._time:02d}:00"

    def is_time_valid(self) -> bool:
        """Check if the current game time is within the valid range."""
        return self._start_time <= self._time < self._end_time


# # --- Example Usage ---
# if __name__ == "__main__":
#     # Core GameTime
#     game_time = GameTime()

#     # Add AM/PM formatting
#     game_time_with_ampm = FormatDecorator(game_time)

#     # Add custom message
#     game_time_with_message = MessageDecorator(game_time_with_ampm, "The time is now")

#     # Test output
#     print(game_time_with_message.display_time())  # "The time is now 09:00 AM"
#     game_time_with_message.increase_time()
#     print(game_time_with_message.display_time())  # "The time is now 10:00 AM"