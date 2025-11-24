from abc import ABCMeta, abstractmethod

class GameTimeComponent(metaclass=ABCMeta):
    """Core Component: Abstract base for GameTime and decorators."""

    @abstractmethod
    def get_time(self) -> int:
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def increase_time(self) -> None:
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def display_time(self) -> str:
        raise NotImplementedError("Not implemented")