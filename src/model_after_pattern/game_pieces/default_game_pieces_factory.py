from random import shuffle
from ..interfaces import IGamePiecesFactory
from .board import Board
from .dev_card import DevCard
from .tile import Tile

class DefaultGamePiecesFactory(IGamePiecesFactory):
    """ Concrete Factory that implements the IGamePiecesFactory interface
    to create game pieces: Board, Dev Cards, Indoor and Outdoor Tiles,"""

    def create_board(self):
        return Board()

    def create_dev_cards(self):
        return DevCard.get_dev_cards()

    def create_indoor_tiles(self):
        return Tile.get_indoor_tiles()

    def create_outdoor_tiles(self):
        return Tile.get_outdoor_tiles()

    def shuffle_tiles(self, tiles: list) -> None:
        shuffle(tiles)