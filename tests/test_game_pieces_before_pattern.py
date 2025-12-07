import unittest
from unittest.mock import MagicMock, patch
from src.model.game_pieces.game_pieces import GamePieces
from src.enums_and_types import Direction


class TestGamePieces(unittest.TestCase):

    # ----------------------------------------------------------------------
    # SETUP TEST
    # ----------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.shuffle")
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_setup_initialises_board_and_places_foyer_tile(
        self, mock_tile, mock_dev, mock_board, mock_shuffle
    ):
        """Setup() should create lists, place foyer tile, and shuffle tiles."""

        # Controlled lists returned by mocks
        indoor_tiles = [MagicMock(), MagicMock()]
        outdoor_tiles = [MagicMock()]
        dev_cards = [MagicMock(), MagicMock()]

        mock_tile.get_indoor_tiles.return_value = indoor_tiles.copy()
        mock_tile.get_outdoor_tiles.return_value = outdoor_tiles.copy()
        mock_dev.get_dev_cards.return_value = dev_cards.copy()

        board_instance = MagicMock()
        mock_board.return_value = board_instance

        # Act
        GamePieces()

        # Expect foyer tile (last indoor tile) placed before shuffle
        foyer = indoor_tiles[-1]
        board_instance.place_tile.assert_called_once_with(
            foyer, Direction.NORTH, None, Direction.SOUTH
        )

        # Shuffle must be called twice
        self.assertEqual(mock_shuffle.call_count, 2)

    # ----------------------------------------------------------------------
    # DEV CARD DRAW
    # ----------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_draw_dev_card_reduces_count(self, mock_tile, mock_dev, mock_board):
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock(), MagicMock()]
        mock_board.return_value = MagicMock()

        gp = GamePieces()
        before = gp.dev_cards_remaining()

        gp.draw_dev_card()

        self.assertEqual(gp.dev_cards_remaining(), before - 1)

    # ----------------------------------------------------------------------
    # INDOOR TILE DRAW
    # ----------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_draw_indoor_tile_reduces_count(self, mock_tile, mock_dev, mock_board):
        mock_tile.get_indoor_tiles.return_value = [MagicMock(), MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        mock_board.return_value = MagicMock()

        gp = GamePieces()
        before = gp.indoor_tiles_remaining()

        gp.draw_indoor_tile()

        self.assertEqual(gp.indoor_tiles_remaining(), before - 1)

    # ----------------------------------------------------------------------
    # OUTDOOR TILE DRAW
    # ----------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_draw_outdoor_tile_reduces_count(self, mock_tile, mock_dev, mock_board):
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock(), MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        mock_board.return_value = MagicMock()

        gp = GamePieces()
        before = gp.outdoor_tiles_remaining()

        gp.draw_outdoor_tile()

        self.assertEqual(gp.outdoor_tiles_remaining(), before - 1)

    # ----------------------------------------------------------------------
    # PLACE TILE DELEGATION
    # ----------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_place_tile_delegates_to_board(self, mock_tile, mock_dev, mock_board):
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        board_instance = MagicMock()
        mock_board.return_value = board_instance

        gp = GamePieces()

        tileA = MagicMock()
        tileB = MagicMock()

        gp.place_tile(tileA, Direction.NORTH, tileB, Direction.SOUTH)

        board_instance.place_tile.assert_called_with(
            tileA, Direction.NORTH, tileB, Direction.SOUTH
        )

    # ----------------------------------------------------------------------
    # IS STUCK LOGIC
    # ----------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_is_stuck_requires_board_stuck_and_tiles_remaining(
        self, mock_tile, mock_dev, mock_board
    ):
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        board_instance = MagicMock()

        mock_board.return_value = board_instance
        board_instance.is_stuck.return_value = True

        gp = GamePieces()

        # First: stuck because board says stuck and tiles exist
        self.assertTrue(gp.is_stuck())

        # Remove all tiles; should no longer be “stuck”
        gp._indoor_tiles.clear()
        gp._outdoor_tiles.clear()

        self.assertFalse(gp.is_stuck())


if __name__ == "__main__":
    unittest.main()
