import unittest
from unittest.mock import MagicMock, patch
from src.model.game_pieces.game_pieces import GamePieces
from src.enums_and_types import Direction


class TestGamePieces(unittest.TestCase):

    @patch("src.model.game_pieces.game_pieces.shuffle")
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_setup_places_foyer_tile_before_shuffle(
        self, mock_tile, mock_dev, mock_board, mock_shuffle
    ):
        indoor = [MagicMock(name="T1"), MagicMock(name="T2")]
        outdoor = [MagicMock(name="O1")]
        dev = [MagicMock(name="D1")]

        mock_tile.get_indoor_tiles.return_value = indoor.copy()
        mock_tile.get_outdoor_tiles.return_value = outdoor.copy()
        mock_dev.get_dev_cards.return_value = dev.copy()

        board_instance = MagicMock()
        mock_board.return_value = board_instance

        GamePieces()

        foyer_tile = indoor[-1]
        board_instance.place_tile.assert_called_once_with(
            foyer_tile, Direction.NORTH, None, Direction.SOUTH
        )

        self.assertEqual(mock_shuffle.call_count, 2)

    # -------------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_dev_card_draw_reduces_count(self, mock_tile, mock_dev, mock_board):
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock(), MagicMock()]
        mock_board.return_value = MagicMock()

        gp = GamePieces()
        before = gp.dev_cards_remaining()

        gp.draw_dev_card()

        self.assertEqual(gp.dev_cards_remaining(), before - 1)

    # -------------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_indoor_tile_draw_reduces_count(self, mock_tile, mock_dev, mock_board):
        tiles = [MagicMock(), MagicMock(), MagicMock()]
        mock_tile.get_indoor_tiles.return_value = tiles.copy()
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        mock_board.return_value = MagicMock()

        gp = GamePieces()
        before = gp.indoor_tiles_remaining()

        gp.draw_indoor_tile()

        self.assertEqual(gp.indoor_tiles_remaining(), before - 1)

    # -------------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_outdoor_tile_draw_reduces_count(self, mock_tile, mock_dev, mock_board):
        mock_tile.get_outdoor_tiles.return_value = [MagicMock(), MagicMock()]
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        mock_board.return_value = MagicMock()

        gp = GamePieces()
        before = gp.outdoor_tiles_remaining()

        gp.draw_outdoor_tile()

        self.assertEqual(gp.outdoor_tiles_remaining(), before - 1)

    # -------------------------------------------------------------------------
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

    # -------------------------------------------------------------------------
    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_is_stuck_returns_true_only_if_board_reports_stuck_and_tiles_remaining(
        self, mock_tile, mock_dev, mock_board
    ):
        mock_tile.get_indoor_tiles.return_value = [MagicMock()]
        mock_tile.get_outdoor_tiles.return_value = [MagicMock()]
        mock_dev.get_dev_cards.return_value = [MagicMock()]
        board_instance = MagicMock()
        mock_board.return_value = board_instance

        gp = GamePieces()
        board_instance.is_stuck.return_value = True

        self.assertTrue(gp.is_stuck())

        gp._indoor_tiles.clear()
        gp._outdoor_tiles.clear()

        self.assertFalse(gp.is_stuck())

if __name__ == "__main__":
    unittest.main()
