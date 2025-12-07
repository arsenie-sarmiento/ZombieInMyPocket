from abc import ABC, abstractmethod
from typing import List
from .i_dev_card import IDevCard
from .i_tile import ITile
from .i_board import IBoard

class IGamePiecesFactory(ABC):

    @abstractmethod
    def create_board(self) -> IBoard:
        pass

    @abstractmethod
    def create_dev_cards(self) -> List[IDevCard]:
        pass

    @abstractmethod
    def create_indoor_tiles(self) -> List[ITile]:
        pass

    @abstractmethod
    def create_outdoor_tiles(self) -> List[ITile]:
        pass