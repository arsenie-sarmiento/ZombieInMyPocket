from .base_decorator import GameTimeDecorator
from ..interfaces import GameTimeComponent

class MessageDecorator(GameTimeDecorator):
    """Adds a custom message to the time display."""
    
    def __init__(self, component: GameTimeComponent, message: str):
        super().__init__(component)
        self._message = message

    def display_time(self) -> str:
        base_time = self._component.display_time()
        return f"{self._message} {base_time}"
# from ..interfaces import IGameTime
# from .time_formatter import TimeFormatter

# class GameTimeDisplay:
#     """Decorator that formats and presents a GameTime using a formatter"""
    
#     def __init__(self, game_time: IGameTime, formatter: TimeFormatter):
#         self.game_time = game_time
#         self.formatter = formatter

#     def __str__(self) -> str:
#         return "The time is now " + self.formatter.format(self.game_time.get_hour())
