from .base_decorator import GameTimeDecorator

class FormatDecorator(GameTimeDecorator):
    """
    Decorator that formats GameTime display with AM/PM.
    Extensible for other formatting strategies if needed.
    """

    _AM = "AM"
    _PM = "PM"

    def display_time(self) -> str:
        """
        Returns the time string with AM/PM formatting.
        Correctly handles 12-hour formatting:
        - 12:00 → PM
        - 0:00 → AM
        - 13:00 → 01:00 PM
        """
        hour = self._component.get_time()
        display_hour = hour % 12 or 12  # convert 0 or 12+ to 12-hour format
        suffix = self._AM if hour < 12 else self._PM
        base_time = f"{display_hour:02d}:00"
        return f"{base_time} {suffix}"
