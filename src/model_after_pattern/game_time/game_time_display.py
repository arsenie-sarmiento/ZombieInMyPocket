from ..interfaces import IGameTime
from .time_formatter import TimeFormatter

class GameTimeDisplay:
    """Decorator that formats and presents a GameTime using a formatter"""
    
    def __init__(self, game_time: IGameTime, formatter: TimeFormatter):
        self.game_time = game_time
        self.formatter = formatter

    def __str__(self) -> str:
        return "The time is now " + self.formatter.format(self.game_time.get_hour())
