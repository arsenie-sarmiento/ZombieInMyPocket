from abc import ABC, abstractmethod

class GameTimeComponent(ABC):
    """Core Component: Abstract base for GameTime and decorators."""
    
    @abstractmethod
    def get_time(self) -> int:
        pass

    @abstractmethod
    def increase_time(self) -> None:
        pass

    @abstractmethod
    def display_time(self) -> str:
        pass