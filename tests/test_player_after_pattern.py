import unittest
from unittest.mock import MagicMock

from src.model.player.player import Player
from src.model.interfaces.i_item import IItem

# ===============================
#   Player Item Combination Tests
# ===============================
class TestPlayerItemCombination(unittest.TestCase):

    def test_combine_items_from_inventory(self):
        item1 = MagicMock(spec=IItem)
        item2 = MagicMock(spec=IItem)

        combination_result = MagicMock()
        combination_result.items_consumed = [item1, item2]

        player = Player()
        player._combination_engine.combine = MagicMock(side_effect=lambda a, b:
            combination_result if {a, b} == {item1, item2} else None
        )

        # Put items in inventory
        player.add_item_to_inventory(item1)
        player.add_item_to_inventory(item2)

        # Attempt combination
        success = player.combine_items_from_inventory()

        self.assertTrue(success)
        self.assertNotIn(item1, player.get_inventory())
        self.assertNotIn(item2, player.get_inventory())


if __name__ == "__main__":
    unittest.main()
