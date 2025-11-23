from abc import ABC, abstractmethod

class TimeFormatter(ABC):
    """Abstraction for time formatting strategies"""
    
    @abstractmethod
    def format(self, hour: int) -> str:
        pass


class AmPmFormatter(TimeFormatter):
    """12-hour AM/PM formatting"""
    
    def format(self, hour: int) -> str:
        suffix = "AM" if 0 <= hour < 12 else "PM"
        display_hour = hour if 1 <= hour <= 12 else hour % 12 or 12
        return f"{display_hour:02d}:00{suffix}"

class MilitaryFormatter(TimeFormatter):
    """24-hour military formatting"""
    
    def format(self, hour: int) -> str:
        return f"{hour:02d}:00"
