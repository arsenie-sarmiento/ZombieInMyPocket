from abc import ABC, abstractmethod
from src.model_after_pattern.interfaces.i_encounter import IEncounter
from .i_item import IItem


class IDevCard(ABC):
    """Abstract interface for development cards in the game."""
    @abstractmethod
    def get_item(self) -> IItem:
        pass

    @abstractmethod
    def get_encounter(self, time: int) -> IEncounter:
        pass