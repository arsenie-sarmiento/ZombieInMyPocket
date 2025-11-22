# gametime.py
from ..interfaces.i_game_time import GameTimeInterface

class GameTime(GameTimeInterface):
    """Concrete GameTime implementation storing current hour"""
    
    def __init__(self, hour: int = 9):
        self._hour = hour

    def get_hour(self) -> int:
        return self._hour

    def increase_hour(self) -> None:
        self._hour += 1
