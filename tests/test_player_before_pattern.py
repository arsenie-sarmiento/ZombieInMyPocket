import unittest
from unittest.mock import MagicMock

from src.model.player.player import Player
from .mocks.interfaces.i_item import IItem
from .mocks.base_item import ConsumableItem
from .mocks.combination_engine import CombinationEngine
from .mocks.combination_rules import CombinationRule

# ===============================
#   Player Item Combination Tests
# ===============================
class TestCombineItemsFromInventory(unittest.TestCase):

    # Returns False if fewer than 2 items
    def test_inventory_with_fewer_than_two_items(self):
        initial_health = 6
        attack_power = 1
        inventory_limit = 2
        player = Player(initial_health, attack_power, inventory_limit)
        # player._combination_engine.combine = ConsumableItem()

        item_a = MagicMock(spec=IItem)
        player.add_item_to_inventory(item_a)
        # item_b = MagicMock(spec=IItem)
        # player.add_item_to_inventory(item_b)
        # self.assertFalse(player.combine_items_from_inventory())

        # player.add_item_to_inventory(MagicMock(spec=IItem))
        print(player.get_inventory())
        self.assertFalse(player.combine_items_from_inventory())
        # player._combination_engine.combine.assert_not_called()

    # # # Returns True on first valid combination
    def test_valid_item_combo_found(self):
        initial_health = 6
        attack_power = 1
        inventory_limit = 2
        player = Player(initial_health, attack_power, inventory_limit)

        item_a = MagicMock(spec=IItem)
        item_b = MagicMock(spec=IItem)
        result = MagicMock()
        result.items_consumed = [item_a, item_b]

        player._combination_engine.combine = MagicMock(
            side_effect=lambda x, y: result if {x, y} == {item_a, item_b} else None
        )

        player.add_item_to_inventory(item_a)
        player.add_item_to_inventory(item_b)

        self.assertTrue(player.combine_items_from_inventory())

    # Only one combination is applied (short-circuit)
    # def test_stops_after_first_successful_combination(self):
    #     initial_health = 6
    #     attack_power = 1
    #     inventory_limit = 2
    #     player = Player(initial_health, attack_power, inventory_limit)

    #     item_a = MagicMock(spec=IItem)
    #     item_b = MagicMock(spec=IItem)
    #     item_c = MagicMock(spec=IItem)

    #     result = MagicMock()
    #     result.items_consumed = [item_a]

    #     def fake_combine(x, y):
    #         if {x, y} == {item_a, item_b}:
    #             return result
    #         return None

    #     combine_mock = MagicMock(side_effect=fake_combine)
    #     player._combination_engine.combine = combine_mock

    #     player.add_item_to_inventory(item_a)
    #     player.add_item_to_inventory(item_b)
    #     player.add_item_to_inventory(item_c)

    #     player.combine_items_from_inventory()
    #     # Must stop after combining (a,b)
    #     # Thus (a,c) and (b,c) must not be attempted after success
    #     # (a,b) is the first attempted pair in nested order

    #     expected_calls = 1
    #     self.assertEqual(combine_mock.call_count, expected_calls)

    # # Items consumed are removed from inventory
    def test_consumed_items_are_removed(self):
        initial_health = 6
        attack_power = 1
        inventory_limit = 2
        player = Player(initial_health, attack_power, inventory_limit)

        item_a = MagicMock(spec=IItem)
        item_b = MagicMock(spec=IItem)

        result = MagicMock()
        result.items_consumed = [item_a, item_b]

        player._combination_engine.combine = MagicMock(
            side_effect=lambda x, y: result if {x, y} == {item_a, item_b} else None
        )

        player.add_item_to_inventory(item_a)
        player.add_item_to_inventory(item_b)

        player.combine_items_from_inventory()
        inv = player.get_inventory()

        self.assertNotIn(item_a, inv)
        self.assertNotIn(item_b, inv)

    # No items are removed if no valid combination exists
    def test_no_items_removed_on_invalid_combo(self):
        initial_health = 6
        attack_power = 1
        inventory_limit = 2
        player = Player(initial_health, attack_power, inventory_limit)

        item_a = MagicMock(spec=IItem)
        item_b = MagicMock(spec=IItem)

        player._combination_engine.combine = MagicMock(return_value=None)

        player.add_item_to_inventory(item_a)
        player.add_item_to_inventory(item_b)

        player.combine_items_from_inventory()

        self.assertEqual(player.get_inventory(), [item_a, item_b])

    # ValueError from combination engine is swallowed
    def test_no_valueerror_riased(self):
        initial_health = 6
        attack_power = 1
        inventory_limit = 2
        player = Player(initial_health, attack_power, inventory_limit)        

        item_a = MagicMock(spec=IItem)
        item_b = MagicMock(spec=IItem)

        def raise_value_error(x, y):
            raise ValueError("incompatible")

        player._combination_engine.combine = MagicMock(side_effect=raise_value_error)

        player.add_item_to_inventory(item_a)
        player.add_item_to_inventory(item_b)

        # Should not raise exception
        result = player.combine_items_from_inventory()
        self.assertFalse(result)

    # Order of unconsumed items is preserved
    def test_order_of_unconsumed_items_preserved(self):
        player = Player()

        item_a = MagicMock(spec=IItem)
        item_b = MagicMock(spec=IItem)

        # Ensure combination fails
        player._combination_engine.combine = MagicMock(return_value=None)

        # Add in a known order
        player.add_item_to_inventory(item_a)
        player.add_item_to_inventory(item_b)

        player.combine_items_from_inventory()

        self.assertEqual(player.get_inventory(), [item_a, item_b])

if __name__ == "__main__":
    unittest.main()
