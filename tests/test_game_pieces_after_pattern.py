import unittest
from unittest.mock import MagicMock
from src.game.game_pieces import GamePieces
from tests.factories.test_game_pieces_factory import TestGamePiecesFactory
from src.enums_and_types import Direction

class TestGamePiecesRefactored(unittest.TestCase):
    def setUp(self):
        # Deterministic tiles
        self.indoor_tiles = [MagicMock(name=f"Indoor{i}") for i in range(3)]
        self.outdoor_tiles = [MagicMock(name=f"Outdoor{i}") for i in range(2)]
        self.dev_cards = [MagicMock(name=f"Dev{i}") for i in range(4)]

        factory = TestGamePiecesFactory(
            indoor_tiles=self.indoor_tiles.copy(),
            outdoor_tiles=self.outdoor_tiles.copy(),
            dev_cards=self.dev_cards.copy()
        )

        self.gp = GamePieces(factory)

    def test_foyer_placement(self):
        # First indoor tile should be foyer
        foyer_tile = self.indoor_tiles[0]
        self.assertTrue(
            self.gp.get_tile_position(foyer_tile) is not None,
            "Foyer tile was not placed"
        )

    def test_draw_dev_card(self):
        initial = self.gp.dev_cards_remaining()
        self.gp.draw_dev_card()
        self.assertEqual(self.gp.dev_cards_remaining(), initial - 1)

    def test_draw_indoor_tile(self):
        initial = self.gp.indoor_tiles_remaining()
        self.gp.draw_indoor_tile()
        self.assertEqual(self.gp.indoor_tiles_remaining(), initial - 1)

    def test_draw_outdoor_tile(self):
        initial = self.gp.outdoor_tiles_remaining()
        self.gp.draw_outdoor_tile()
        self.assertEqual(self.gp.outdoor_tiles_remaining(), initial - 1)
    def test_tiles_remaining(self):
        expected = self.gp.indoor_tiles_remaining() + self.gp.outdoor_tiles_remaining()
        self.assertEqual(self.gp.tiles_remaining(), expected)

if __name__ == "__main__":
    unittest.main()

# import unittest

# from typing import List, Tuple
# from ..interfaces.i_game_pieces_factory import IGamePiecesFactory
# from ..interfaces.i_dev_card import IDevCard
# from ..interfaces.i_tile import ITile
# from ..board import Board
# from src.enums_and_types import Direction


# class TestGamePiecesFactory(IGamePiecesFactory, unittest.TestCase):
#     """
#     A deterministic, predictable factory for unit tests.
#     No shuffling; the first indoor tile becomes the foyer.
#     """

#     def __init__(
#         self,
#         indoor_tiles: List[ITile],
#         outdoor_tiles: List[ITile],
#         dev_cards: List[IDevCard]
#     ) -> None:
#         self._indoor = indoor_tiles
#         self._outdoor = outdoor_tiles
#         self._dev = dev_cards

#     def create_game_pieces(self) -> Tuple[
#         Board, List[IDevCard], List[ITile], List[ITile]
#     ]:
#         board = Board()

#         # First indoor tile becomes foyer
#         foyer = self._indoor.pop(0)
#         board.place_tile(foyer, Direction.NORTH, None, Direction.SOUTH)

#         return (
#             board,
#             self._dev.copy(),
#             self._indoor.copy(),
#             self._outdoor.copy(),
#         )
