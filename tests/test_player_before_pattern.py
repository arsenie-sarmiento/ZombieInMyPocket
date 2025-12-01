import unittest
from unittest.mock import MagicMock

from src.model.player.player import Player
from src.model.interfaces.i_item import IItem


class TestCombineItemsFromInventory(unittest.TestCase):

    # 1. Returns False if fewer than 2 items
    def test_returns_false_when_inventory_has_fewer_than_two_items(self):
        player = Player()
        player._combination_engine.combine = MagicMock()

        player.add_item_to_inventory(MagicMock(spec=IItem))
        self.assertFalse(player.combine_items_from_inventory())
        player._combination_engine.combine.assert_not_called()

    # 2. Returns True on first valid combination
    def test_returns_true_when_valid_combination_found(self):
        player = Player()

        a = MagicMock(spec=IItem)
        b = MagicMock(spec=IItem)
        result = MagicMock()
        result.items_consumed = [a, b]

        player._combination_engine.combine = MagicMock(
            side_effect=lambda x, y: result if {x, y} == {a, b} else None
        )

        player.add_item_to_inventory(a)
        player.add_item_to_inventory(b)

        self.assertTrue(player.combine_items_from_inventory())

    # 3. Only one combination is applied (short-circuit)
    def test_stops_after_first_successful_combination(self):
        player = Player()

        a = MagicMock(spec=IItem)
        b = MagicMock(spec=IItem)
        c = MagicMock(spec=IItem)

        result = MagicMock()
        result.items_consumed = [a]

        def fake_combine(x, y):
            if {x, y} == {a, b}:
                return result
            return None

        combine_mock = MagicMock(side_effect=fake_combine)
        player._combination_engine.combine = combine_mock

        player.add_item_to_inventory(a)
        player.add_item_to_inventory(b)
        player.add_item_to_inventory(c)

        player.combine_items_from_inventory()
        # Must stop after combining (a,b)
        # Thus (a,c) and (b,c) must not be attempted after success
        # (a,b) is the first attempted pair in nested order

        expected_calls = 1
        self.assertEqual(combine_mock.call_count, expected_calls)

    # 4. Items consumed are removed from inventory
    def test_consumed_items_are_removed(self):
        player = Player()

        a = MagicMock(spec=IItem)
        b = MagicMock(spec=IItem)
        c = MagicMock(spec=IItem)

        result = MagicMock()
        result.items_consumed = [a, b]

        player._combination_engine.combine = MagicMock(
            side_effect=lambda x, y: result if {x, y} == {a, b} else None
        )

        player.add_item_to_inventory(a)
        player.add_item_to_inventory(b)
        player.add_item_to_inventory(c)

        player.combine_items_from_inventory()
        inv = player.get_inventory()

        self.assertNotIn(a, inv)
        self.assertNotIn(b, inv)
        self.assertIn(c, inv)

    # 5. No items are removed if no valid combination exists
    def test_inventory_unchanged_on_no_combination(self):
        player = Player()

        a = MagicMock(spec=IItem)
        b = MagicMock(spec=IItem)

        player._combination_engine.combine = MagicMock(return_value=None)

        player.add_item_to_inventory(a)
        player.add_item_to_inventory(b)

        player.combine_items_from_inventory()

        self.assertEqual(player.get_inventory(), [a, b])

    # 6. ValueError from combination engine is swallowed
    def test_valueerror_is_swallowed(self):
        player = Player()

        a = MagicMock(spec=IItem)
        b = MagicMock(spec=IItem)

        def raise_value_error(x, y):
            raise ValueError("incompatible")

        player._combination_engine.combine = MagicMock(side_effect=raise_value_error)

        player.add_item_to_inventory(a)
        player.add_item_to_inventory(b)

        # Should not raise exception
        result = player.combine_items_from_inventory()
        self.assertFalse(result)

    # 7. Order of unconsumed items is preserved
    def test_order_of_unconsumed_items_preserved(self):
        player = Player()

        a = MagicMock(spec=IItem)
        b = MagicMock(spec=IItem)
        c = MagicMock(spec=IItem)

        # Ensure combination fails
        player._combination_engine.combine = MagicMock(return_value=None)

        # Add in a known order
        player.add_item_to_inventory(a)
        player.add_item_to_inventory(b)
        player.add_item_to_inventory(c)

        player.combine_items_from_inventory()

        self.assertEqual(player.get_inventory(), [a, b, c])


if __name__ == "__main__":
    unittest.main()
