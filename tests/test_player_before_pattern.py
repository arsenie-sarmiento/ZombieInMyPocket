import pytest
from unittest.mock import MagicMock

from src.model import Player
from src.model import IItem


class DummyItem(IItem):
    """Simple mockable item used for testing."""
    def __init__(self, name):
        self.name = name
        self.attack_bonus = 0  # for other player methods
    
    def use(self):
        return False

    def __repr__(self):
        return f"DummyItem({self.name})"


def test_combine_items_success():
    player = Player()

    item1 = DummyItem("itemA")
    item2 = DummyItem("itemB")

    # Mock combination engine so combine(item1,item2) returns a result
    mock_result = MagicMock(items_consumed=[item1, item2])
    player._combination_engine.combine = MagicMock(return_value=mock_result)

    player.add_item_to_inventory(item1)
    player.add_item_to_inventory(item2)

    result = player.combine_items_from_inventory()

    assert result is True
    assert item1 not in player.get_inventory()
    assert item2 not in player.get_inventory()


def test_combine_items_no_combinations_found():
    player = Player()

    item1 = DummyItem("itemA")
    item2 = DummyItem("itemB")

    # Always raise ValueError meaning "no combination rule"
    player._combination_engine.combine = MagicMock(side_effect=ValueError)

    player.add_item_to_inventory(item1)
    player.add_item_to_inventory(item2)

    result = player.combine_items_from_inventory()

    assert result is False
    assert item1 in player.get_inventory()
    assert item2 in player.get_inventory()


def test_combine_items_requires_two_items():
    player = Player()
    player.add_item_to_inventory(DummyItem("only_one"))

    result = player.combine_items_from_inventory()

    assert result is False
