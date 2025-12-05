from typing import Protocol, Tuple, List
from . import IDevCard, ITile
from ..board import Board

class IGamePieces(Protocol):
    """
    Creates the core families of related game objects:
    - Board
    - Dev Cards
    - Indoor Tiles
    - Outdoor Tiles
    - Performs initial placement/shuffle rules
    """

    def create_game_pieces(self) -> Tuple[
        Board,
        List[IDevCard],
        List[ITile],
        List[ITile]
    ]:
        ...
