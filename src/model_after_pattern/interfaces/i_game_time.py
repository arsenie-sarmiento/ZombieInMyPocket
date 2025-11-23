from abc import ABC, abstractmethod

class IGameTime(ABC):
    """Abstraction for any GameTime implementation"""
    @abstractmethod
    def get_hour(self) -> int:
        ...
    @abstractmethod
    def increase_hour(self) -> None:
        ...
