from ..interfaces import GameTimeComponent

class GameTimeDecorator(GameTimeComponent):
    """Decorator Base class for all decorators."""
    
    def __init__(self, component: GameTimeComponent):
        self._component = component

    def get_time(self) -> int:
        return self._component.get_time()

    def increase_time(self) -> None:
        self._component.increase_time()

    def display_time(self) -> str:
        return self._component.display_time()
