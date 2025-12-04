from ..item.item_combination_visitor import ItemCombinationVisitor
from ..item.combination_engine import CombinationEngine
from ..interfaces.i_player import IPlayer

class Player(IPlayer):
    def __init__(self, initial_health=6, attack_power=1, inventory_limit=2):
        self._health = initial_health
        self._max_health = initial_health
        self._attack_power = attack_power
        self._inventory = []
        self._position = (0, 0)
        self._has_totem = False
        self._inventory_limit = inventory_limit

        self._combination_engine = CombinationEngine()
        self._combination_visitor = ItemCombinationVisitor(self._combination_engine)

    def combine_items_from_inventory(self) -> bool:
        result = self._combination_visitor.visit(self._inventory)

        if not result:
            return False

        # Only Player applies the mutations to its own inventory
        for item in result.items_consumed:
            self.remove_item_from_inventory(item)

        return True


