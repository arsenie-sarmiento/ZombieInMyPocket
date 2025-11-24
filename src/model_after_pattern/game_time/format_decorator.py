from .base_decorator import GameTimeDecorator

class FormatDecorator(GameTimeDecorator):
    """
    Decorator that formats GameTime display with AM/PM.
    Extensible for other formatting strategies if needed.
    """

    AM = "AM"
    PM = "PM"

    def display_time(self) -> str:
        """
        Return the time in 12-hour format with an AM/PM suffix.
        """
        hour = self._get_hour()
        display_hour = self._convert_to_12_hour(hour)
        suffix = self._get_suffix(hour)
        return f"{display_hour:02d}:00 {suffix}"

    def _get_hour(self) -> int:
        """Return the raw hour from the wrapped GameTime component."""
        return self._component.get_time()

    def _convert_to_12_hour(self, hour: int) -> int:
        """Convert 24-hour input into 12-hour format."""
        return hour % 12 or 12

    def _get_suffix(self, hour: int) -> str:
        """Return AM or PM depending on the hour."""
        return self.AM if hour < 12 else self.PM