import unittest
from unittest.mock import MagicMock
from src.model_after_pattern.game_pieces.game_pieces import GamePieces
from src.enums_and_types import Direction

# ===============================
#   Game Pieces Setup Tests
# ===============================
class TestGamePiecesSetup(unittest.TestCase):

    # ----------------------------------------------------------------------
    # Setup pulls objects from factory
    # ----------------------------------------------------------------------
    def test_setup_uses_factory_to_create_objects(self):
        """ Test that setup uses the factory to create game pieces """
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
    # Foyer tile is placed correctly
    # ----------------------------------------------------------------------
    def test_foyer_tile_is_popped_and_placed(self):
        """ Test that the foyer tile is popped and placed correctly """
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
    # Remaining tiles are shuffled
    # ----------------------------------------------------------------------
    def test_tiles_are_shuffled(self):
        """ Test that the indoor and outdoor tiles are shuffled """
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
    # Indoor/outdoor/dev card lists are stored correctly
    # ----------------------------------------------------------------------
    def test_lists_are_saved_to_gamepieces(self):
        """ Test that the lists are saved correctly in GamePieces """
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
    # Setup still works with zero tiles (edge case)
    # ----------------------------------------------------------------------
    def test_setup_handles_empty_tile_lists(self):
        """ Handles setup for empty indoor/outdoor tiles sets """
        factory = MagicMock()

        board_instance = MagicMock()
        factory.create_board.return_value = board_instance

        factory.create_dev_cards.return_value = []
        factory.create_indoor_tiles.return_value = []   # No foyer tile
        factory.create_outdoor_tiles.return_value = []

        # Should not crash
        gp = GamePieces(factory)

        # No foyer tile => place_tile must NOT be called
        board_instance.place_tile.assert_not_called()

        self.assertEqual(gp.indoor_tiles_remaining(), 0)
        self.assertEqual(gp.outdoor_tiles_remaining(), 0)
        self.assertEqual(gp.dev_cards_remaining(), 0)

    # ----------------------------------------------------------------------
    # Drawing dev cards reduces counts
    # ----------------------------------------------------------------------
    def test_dev_card_draw_reduces_count(self):
        """ Test that drawing a dev card reduces the count of remaining dev cards """
        factory = MagicMock()

        factory.create_board.return_value = MagicMock()
        factory.create_indoor_tiles.return_value = [MagicMock()]
        factory.create_outdoor_tiles.return_value = [MagicMock()]
        factory.create_dev_cards.return_value = [MagicMock(), MagicMock()]

        gp = GamePieces(factory)
        before = gp.dev_cards_remaining()

        gp.draw_dev_card()

        self.assertEqual(gp.dev_cards_remaining(), before - 1)

    # ----------------------------------------------------------------------
    # Drawing indoor tiles reduces counts
    # ----------------------------------------------------------------------
    def test_indoor_tile_draw_reduces_count(self):
        """ Test that drawing an indoor tile reduces the count of remaining indoor tiles """
        factory = MagicMock()

        tiles = [MagicMock(), MagicMock(), MagicMock()]

        factory.create_board.return_value = MagicMock()
        factory.create_outdoor_tiles.return_value = [MagicMock()]
        factory.create_dev_cards.return_value = [MagicMock()]
        factory.create_indoor_tiles.return_value = tiles.copy()

        gp = GamePieces(factory)
        before = gp.indoor_tiles_remaining()

        gp.draw_indoor_tile()

        self.assertEqual(gp.indoor_tiles_remaining(), before - 1)

    # ----------------------------------------------------------------------
    # Drawing outdoor tiles reduces counts
    # ----------------------------------------------------------------------
    def test_outdoor_tile_draw_reduces_count(self):
        """ Test that drawing an outdoor tile reduces the count of remaining outdoor tiles """
        factory = MagicMock()

        factory.create_board.return_value = MagicMock()
        factory.create_indoor_tiles.return_value = [MagicMock()]
        factory.create_dev_cards.return_value = [MagicMock()]
        factory.create_outdoor_tiles.return_value = [MagicMock(), MagicMock()]

        gp = GamePieces(factory)
        before = gp.outdoor_tiles_remaining()

        gp.draw_outdoor_tile()

        self.assertEqual(gp.outdoor_tiles_remaining(), before - 1)

if __name__ == "__main__":
    unittest.main()
