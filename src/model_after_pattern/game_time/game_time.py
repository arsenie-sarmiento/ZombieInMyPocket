
from ..interfaces import GameTimeComponent

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