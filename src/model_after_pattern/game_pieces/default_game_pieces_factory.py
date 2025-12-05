from typing import List, Tuple
from random import shuffle

from ..interfaces.i_game_pieces import IGamePiecesFactory
from ..interfaces.i_dev_card import IDevCard
from ..interfaces.i_tile import ITile
from ..board import Board
from ..dev_card import DevCard
from ..tile import Tile
from src.enums_and_types import Direction


class DefaultGamePiecesFactory(IGamePiecesFactory):

    def create_game_pieces(self) -> Tuple[
        Board, List[IDevCard], List[ITile], List[ITile]
    ]:

        board = Board()
        dev_cards = DevCard.get_dev_cards()
        indoor_tiles = Tile.get_indoor_tiles()
        outdoor_tiles = Tile.get_outdoor_tiles()

        # Place the foyer tile (top tile before shuffle)
        foyer = indoor_tiles.pop()
        board.place_tile(
            foyer, 
            Direction.NORTH,
            None,
            Direction.SOUTH
        )

        # Shuffle decks
        shuffle(indoor_tiles)
        shuffle(outdoor_tiles)

        return board, dev_cards, indoor_tiles, outdoor_tiles
