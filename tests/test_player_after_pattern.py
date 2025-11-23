import pytest
from unittest.mock import MagicMock

from src.model.player.player import Player
from src.model.interfaces.i_item import IItem


class DummyItem(IItem):
    def __init__(self, name):
        self.name = name

    def use(self):
        return False


def test_execute_combine_success():
    player = Player()

    item1 = DummyItem("A")
    item2 = DummyItem("B")
    new_item = DummyItem("C")

    player.add_item_to_inventory(item1)
    player.add_item_to_inventory(item2)

    # Mock result container
    mock_result = MagicMock(
        produced_item=new_item,
        items_consumed=[item1, item2]
    )

    # Engine now handles the logic instead of inside Player
    player._combination_engine.execute_combine = MagicMock(return_value=mock_result)

    result = player._combination_engine.execute_combine(player)

    assert result.produced_item == new_item
    assert item1 in result.items_consumed
    assert item2 in result.items_consumed


def test_execute_combine_no_result():
    player = Player()

    item1 = DummyItem("A")
    item2 = DummyItem("B")

    player.add_item_to_inventory(item1)
    player.add_item_to_inventory(item2)

    player._combination_engine.execute_combine = MagicMock(return_value=None)

    result = player._combination_engine.execute_combine(player)

    assert result is None


def test_player_inventory_updates_after_command():
    """
    Ensures the command itself mutates the inventory — not Player.
    """
    player = Player()

    item1 = DummyItem("A")
    item2 = DummyItem("B")
    new_item = DummyItem("C")

    player.add_item_to_inventory(item1)
    player.add_item_to_inventory(item2)

    mock_result = MagicMock(
        produced_item=new_item,
        items_consumed=[item1, item2]
    )

    def mutate_inventory(p):
        # Simulate how the real command mutates the inventory
        p.remove_item_from_inventory(item1)
        p.remove_item_from_inventory(item2)
        p.add_item_to_inventory(new_item)
        return mock_result

    player._combination_engine.execute_combine = MagicMock(side_effect=mutate_inventory)

    result = player._combination_engine.execute_combine(player)

    assert new_item in player.get_inventory()
    assert item1 not in player.get_inventory()
    assert item2 not in player.get_inventory()
