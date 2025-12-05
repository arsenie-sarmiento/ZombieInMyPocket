import unittest
from src.model.game_pieces.game_pieces import GamePieces

class TestGamePieces(unittest.TestCase):
    """Unit tests for GamePieces class."""

    def test_initial_dev_card_count(self):
        gp = GamePieces()
        expected_count = 25  # Assuming there are 25 dev cards initially
        self.assertEqual(gp.dev_cards_remaining(), expected_count)

    def test_initial_indoor_tile_count(self):
        gp = GamePieces()
        expected_count = 30  # Assuming there are 30 indoor tiles initially
        self.assertEqual(gp.indoor_tiles_remaining(), expected_count)

    def test_initial_outdoor_tile_count(self):
        gp = GamePieces()
        expected_count = 20  # Assuming there are 20 outdoor tiles initially
        self.assertEqual(gp.outdoor_tiles_remaining(), expected_count)
        
    def test_draw_dev_card_reduces_deck(self):
        gp = GamePieces()
        initial = gp.dev_cards_remaining()
        gp.draw_dev_card()
        self.assertEqual(gp.dev_cards_remaining(), initial - 1)

    def test_indoor_tile_draw(self):
        gp = GamePieces()
        initial = gp.indoor_tiles_remaining()
        gp.draw_indoor_tile()
        self.assertEqual(gp.indoor_tiles_remaining(), initial - 1)
        
    def test_outdoor_tile_draw(self):
        gp = GamePieces()
        initial = gp.outdoor_tiles_remaining()
        gp.draw_outdoor_tile()
        self.assertEqual(gp.outdoor_tiles_remaining(), initial - 1)

    def test_tiles_remaining(self):
        gp = GamePieces()
        expected = gp.indoor_tiles_remaining() + gp.outdoor_tiles_remaining()
        self.assertEqual(gp.tiles_remaining(), expected) 


if __name__ == "__main__":
    unittest.main()
