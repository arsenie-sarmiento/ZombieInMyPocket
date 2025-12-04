
# src/model/item/combination_visitor.py
from ..interfaces.i_item import IItem
from typing import List, Optional


class CombinationResult:
    def __init__(self, items_consumed: List[IItem]):
        self.items_consumed = items_consumed

class ItemCombinationVisitor:
    """Encapsulates the entire combination-searching algorithm."""

    def __init__(self, combination_engine):
        self._engine = combination_engine

    def visit(self, inventory: List[IItem]) -> Optional[CombinationResult]:
        if len(inventory) < 2:
            return None

        for i in range(len(inventory)):
            for j in range(i + 1, len(inventory)):
                item1, item2 = inventory[i], inventory[j]

                try:
                    result = self._engine.combine(item1, item2)
                    if result:
                        return CombinationResult(result.items_consumed)
                except ValueError:
                    continue
        return None


