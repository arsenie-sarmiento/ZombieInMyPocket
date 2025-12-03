from ..interfaces.i_player import IPlayer
from ..interfaces.i_item import IItem
# from src.enums_and_types.types import Position
class Player(IPlayer):
    """Player iteration-two implementation."""

    def __init__(self, initial_health: int = 6, attack_power: int = 1, inventory_limit: int = 2):
        pass
        # self._health = initial_health
        # self._max_health = initial_health
        # self._attack_power = attack_power
        # self._inventory: list[IItem] = []
        # self._position: Position = (0, 0)
        # self._has_totem = False
        # self._inventory_limit = inventory_limit
        # self._combination_engine = CombinationEngine()