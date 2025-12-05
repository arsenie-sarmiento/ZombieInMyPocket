
import unittest
from unittest.mock import MagicMock, patch
from src.model.game_pieces import GamePieces
from src.enums_and_types import Direction, Position

class TestGamePieces(unittest.TestCase):

    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    
    def test_game_piece_setup_on_start(self, mock_tile, mock_dev, mock_board):

        # --- Arrange ----------------------------------------------------------------
        # Create predictable mock lists
        indoor_tiles = [MagicMock(), MagicMock(), MagicMock()]
        outdoor_tiles = [MagicMock(), MagicMock()]
        dev_cards = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]

        mock_tile.get_indoor_tiles.return_value = indoor_tiles.copy()
        mock_tile.get_outdoor_tiles.return_value = outdoor_tiles.copy()
        mock_dev.get_dev_cards.return_value = dev_cards.copy()

        # Mock Board instance
        board_instance = MagicMock()
        mock_board.return_value = board_instance

        # --- Act --------------------------------------------------------------------
        gp = GamePieces()

        # --- Assert -----------------------------------------------------------------
        # 1. The foyer tile is placed on init (top indoor tile popped before shuffle)
        board_instance.place_tile.assert_called_once()
        called_tile = board_instance.place_tile.call_args[0][0]
        self.assertIn(called_tile, indoor_tiles)

        # 2. Drawing removes from the list
        before = gp.dev_cards_remaining()
        gp.draw_dev_card()
        self.assertEqual(gp.dev_cards_remaining(), before - 1)

        before_indoor = gp.indoor_tiles_remaining()
        gp.draw_indoor_tile()
        self.assertEqual(gp.indoor_tiles_remaining(), before_indoor - 1)

        before_outdoor = gp.outdoor_tiles_remaining()
        gp.draw_outdoor_tile()
        self.assertEqual(gp.outdoor_tiles_remaining(), before_outdoor - 1)

        # 3. Delegation: place_tile forwards call to board
        tileA = MagicMock()
        tileB = MagicMock()
        gp.place_tile(tileA, Direction.NORTH, tileB, Direction.SOUTH)
        board_instance.place_tile.assert_called()

        # 4. The stuck logic is delegated and combined with tile counts
        board_instance.is_stuck.return_value = True
        self.assertTrue(gp.is_stuck())

import unittest
from unittest.mock import MagicMock, patch
from src.model.game_pieces import GamePieces
from src.enums_and_types import Direction, Position

class TestGamePieces(unittest.TestCase):

    @patch("src.model.game_pieces.game_pieces.Board")
    @patch("src.model.game_pieces.game_pieces.DevCard")
    @patch("src.model.game_pieces.game_pieces.Tile")
    def test_core_behaviour_retained(self, mock_tile, mock_dev, mock_board):

        # --- Arrange ----------------------------------------------------------------
        # Create predictable mock lists
        indoor_tiles = [MagicMock(), MagicMock(), MagicMock()]
        outdoor_tiles = [MagicMock(), MagicMock()]
        dev_cards = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]

        mock_tile.get_indoor_tiles.return_value = indoor_tiles.copy()
        mock_tile.get_outdoor_tiles.return_value = outdoor_tiles.copy()
        mock_dev.get_dev_cards.return_value = dev_cards.copy()

        # Mock Board instance
        board_instance = MagicMock()
        mock_board.return_value = board_instance

        # --- Act --------------------------------------------------------------------
        gp = GamePieces()

        # --- Assert -----------------------------------------------------------------
        # 1. The foyer tile is placed on init (top indoor tile popped before shuffle)
        board_instance.place_tile.assert_called_once()
        called_tile = board_instance.place_tile.call_args[0][0]
        self.assertIn(called_tile, indoor_tiles)

        # 2. Drawing removes from the list
        before = gp.dev_cards_remaining()
        gp.draw_dev_card()
        self.assertEqual(gp.dev_cards_remaining(), before - 1)

        before_indoor = gp.indoor_tiles_remaining()
        gp.draw_indoor_tile()
        self.assertEqual(gp.indoor_tiles_remaining(), before_indoor - 1)

        before_outdoor = gp.outdoor_tiles_remaining()
        gp.draw_outdoor_tile()
        self.assertEqual(gp.outdoor_tiles_remaining(), before_outdoor - 1)

        # 3. Delegation: place_tile forwards call to board
        tileA = MagicMock()
        tileB = MagicMock()
        gp.place_tile(tileA, Direction.NORTH, tileB, Direction.SOUTH)
        board_instance.place_tile.assert_called()

        # 4. The stuck logic is delegated and combined with tile counts
        board_instance.is_stuck.return_value = True
        self.assertTrue(gp.is_stuck())




# import unittest
# from unittest.mock import patch, MagicMock
# from src.model.game_pieces.game_pieces import GamePieces
# from src.enums_and_types import Direction

# class TestGamePiecesSetup(unittest.TestCase):
#     """Unit test for the setup method of GamePieces (before refactor)."""

#     @patch("src.model.game_pieces.game_pieces.Board")
#     @patch("src.model.game_pieces.game_pieces.DevCard")
#     @patch("src.model.game_pieces.game_pieces.Tile")
#     @patch("src.model.game_pieces.game_pieces.shuffle")
#     def test_setup_initial_state(self, mock_shuffle, mock_tile, mock_dev, mock_board):
#         # Arrange: mock return values
#         indoor_tiles = [MagicMock(name=f"Indoor{i}") for i in range(3)]
#         outdoor_tiles = [MagicMock(name=f"Outdoor{i}") for i in range(2)]
#         dev_cards = [MagicMock(name=f"Dev{i}") for i in range(4)]

#         mock_tile.get_indoor_tiles.return_value = indoor_tiles.copy()
#         mock_tile.get_outdoor_tiles.return_value = outdoor_tiles.copy()
#         mock_dev.get_dev_cards.return_value = dev_cards.copy()

#         board_instance = MagicMock()
#         mock_board.return_value = board_instance

#         # Act: create GamePieces (calls setup internally)
#         gp = GamePieces()

#         # Assert 1: dev cards, indoor tiles, outdoor tiles initialized
#         self.assertEqual(gp.dev_cards_remaining(), len(dev_cards))
#         self.assertEqual(gp.indoor_tiles_remaining(), len(indoor_tiles) - 1)  # one indoor tile popped for foyer
#         self.assertEqual(gp.outdoor_tiles_remaining(), len(outdoor_tiles))

#         # Assert 2: board.place_tile called for foyer tile
#         foyer_tile = indoor_tiles[0]  # first tile in the list
#         board_instance.place_tile.assert_called_once_with(
#             foyer_tile, Direction.NORTH, None, Direction.SOUTH
#         )

#         # Assert 3: shuffle called on indoor and outdoor tiles
#         self.assertEqual(mock_shuffle.call_count, 2)
#         mock_shuffle.assert_any_call(indoor_tiles[1:])  # remaining indoor tiles after foyer pop
#         mock_shuffle.assert_any_call(outdoor_tiles)

# if __name__ == "__main__":
#     unittest.main()
