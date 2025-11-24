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