import unittest
from unittest.mock import MagicMock
from src.model.game_pieces.game_pieces import GamePieces
from src.enums_and_types import Direction


class TestGamePiecesSetup(unittest.TestCase):

    # ----------------------------------------------------------------------
    # SCENARIO 1 — Setup pulls objects from factory
    # ----------------------------------------------------------------------
    def test_setup_uses_factory_to_create_objects(self):
        factory = MagicMock()

        # Mock returns
        factory.create_board.return_value = MagicMock()
        factory.create_dev_cards.return_value = [MagicMock(), MagicMock()]
        factory.create_indoor_tiles.return_value = [MagicMock(), MagicMock()]
        factory.create_outdoor_tiles.return_value = [MagicMock()]

        gp = GamePieces(factory)

        # Assertions: factory methods were used
        factory.create_board.assert_called_once()
        factory.create_dev_cards.assert_called_once()
        factory.create_indoor_tiles.assert_called_once()
        factory.create_outdoor_tiles.assert_called_once()

    # ----------------------------------------------------------------------
    # SCENARIO 2 — Foyer tile is placed correctly
    # ----------------------------------------------------------------------
    def test_foyer_tile_is_popped_and_placed(self):
        factory = MagicMock()

        # Create a controlled indoor tile list
        foyer_tile = MagicMock(name="foyer_tile")
        tile2 = MagicMock(name="tile2")
        indoor_tiles = [foyer_tile, tile2]

        board = MagicMock()

        factory.create_board.return_value = board
        factory.create_dev_cards.return_value = []
        factory.create_indoor_tiles.return_value = indoor_tiles.copy()
        factory.create_outdoor_tiles.return_value = []

        GamePieces(factory)

        # foyer_tile should be placed (it was the last element popped)
        board.place_tile.assert_called_once_with(
            tile2,                # because .pop() removes the LAST element
            Direction.NORTH,
            None,
            Direction.SOUTH
        )

    # ----------------------------------------------------------------------
    # SCENARIO 3 — Remaining tiles are shuffled
    # ----------------------------------------------------------------------
    def test_tiles_are_shuffled(self):
        factory = MagicMock()

        indoor_tiles = [MagicMock(), MagicMock(), MagicMock()]
        outdoor_tiles = [MagicMock(), MagicMock()]

        factory.create_board.return_value = MagicMock()
        factory.create_dev_cards.return_value = []
        factory.create_indoor_tiles.return_value = indoor_tiles.copy()
        factory.create_outdoor_tiles.return_value = outdoor_tiles.copy()

        GamePieces(factory)

        # Shuffle must be invoked twice
        self.assertEqual(factory.shuffle_tiles.call_count, 2)

        # Shuffle applied to correct lists *after foyer pop*
        shuffled_indoor = factory.shuffle_tiles.call_args_list[0][0][0]
        shuffled_outdoor = factory.shuffle_tiles.call_args_list[1][0][0]

        # Indoor tiles should have 2 left after pop
        self.assertEqual(len(shuffled_indoor), 2)
        self.assertEqual(len(shuffled_outdoor), 2)

    # ----------------------------------------------------------------------
    # SCENARIO 4 — Indoor/outdoor/dev card lists are stored correctly
    # ----------------------------------------------------------------------
    def test_lists_are_saved_to_gamepieces(self):
        factory = MagicMock()

        dev_cards = [MagicMock(), MagicMock()]
        indoor = [MagicMock(), MagicMock()]      # foyer is last item
        outdoor = [MagicMock()]

        factory.create_board.return_value = MagicMock()
        factory.create_dev_cards.return_value = dev_cards.copy()
        factory.create_indoor_tiles.return_value = indoor.copy()
        factory.create_outdoor_tiles.return_value = outdoor.copy()

        gp = GamePieces(factory)

        # After popping foyer tile, 1 tile remains
        self.assertEqual(gp.dev_cards_remaining(), 2)
        self.assertEqual(gp.indoor_tiles_remaining(), 1)
        self.assertEqual(gp.outdoor_tiles_remaining(), 1)

    # ----------------------------------------------------------------------
    # SCENARIO 5 — Setup still works with zero tiles (edge case)
    # ----------------------------------------------------------------------
    def test_setup_handles_empty_tile_lists(self):
        factory = MagicMock()

        factory.create_board.return_value = MagicMock()
        factory.create_dev_cards.return_value = []
        factory.create_indoor_tiles.return_value = []   # No foyer tile
        factory.create_outdoor_tiles.return_value = []

        # No crash expected
        gp = GamePieces(factory)

        # Board.place_tile should NEVER be called since no foyer tile exists
        factory.create_board.return_value.place_tile.assert_not_called()

        self.assertEqual(gp.indoor_tiles_remaining(), 0)
        self.assertEqual(gp.outdoor_tiles_remaining(), 0)
        self.assertEqual(gp.dev_cards_remaining(), 0)


if __name__ == "__main__":
    unittest.main()
