from ..interfaces import IGamePieces, IGamePiecesFactory, IDevCard, ITile
from src.enums_and_types import *
from .board import Board

class GamePieces(IGamePieces):

    def __init__(self, factory: IGamePiecesFactory) -> None:
        self._factory = factory
        self.setup()

    def setup(self) -> None:
        # All creation now comes from the factory
        self._board = self._factory.create_board()
        self._dev_cards = self._factory.create_dev_cards()
        self._indoor_tiles = self._factory.create_indoor_tiles()
        self._outdoor_tiles = self._factory.create_outdoor_tiles()

        # Place the foyer tile (top indoor tile before shuffling)
        foyer_tile = self._indoor_tiles.pop()
        self._board.place_tile(
            foyer_tile,
            Direction.NORTH,
            None,
            Direction.SOUTH
        )

        # Shuffle via factory abstraction
        self._factory.shuffle_tiles(self._indoor_tiles)
        self._factory.shuffle_tiles(self._outdoor_tiles)

    def draw_dev_card(self) -> IDevCard:
        return self._dev_cards.pop()

    def dev_cards_remaining(self) -> int:
        return len(self._dev_cards)

    def draw_indoor_tile(self) -> ITile:
        return self._indoor_tiles.pop()

    def indoor_tiles_remaining(self) -> int:
        return len(self._indoor_tiles)

    def draw_outdoor_tile(self) -> ITile:
        return self._outdoor_tiles.pop()

    def outdoor_tiles_remaining(self) -> int:
        return len(self._outdoor_tiles)

    def tiles_remaining(self) -> int:
        return self.indoor_tiles_remaining() + self.outdoor_tiles_remaining()

    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        return self._board.can_place_tile(new_tile, new_exit,
                                          placed_tile, placed_tile_exit)

    def can_move_to_new_tile(self, placed_tile: ITile,
                             placed_tile_exit: Direction) -> bool:
        return self._board.can_move_to_new_tile(placed_tile, placed_tile_exit)

    def place_tile(self, new_tile: ITile, new_exit: Direction,
                   placed_tile: ITile, placed_tile_exit: Direction) -> None:
        self._board.place_tile(new_tile, new_exit, placed_tile,
                               placed_tile_exit)

    def get_tile(self, position: Position) -> ITile | None:
        return self._board.get_tile(position)

    def is_stuck(self) -> bool:
        return self._board.is_stuck() and self.tiles_remaining() > 0

    def get_tile_position(self, tile: ITile) -> Position:
        return self._board.get_tile_position(tile)