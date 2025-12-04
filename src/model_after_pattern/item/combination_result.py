from ..interfaces.i_item import IItem
from typing import List

# @dataclass
# class CombinationResult:
#   def __init__(self, items_consumed: List[IItem]):
#     """Result of combining two items.
#     Attributes:
#          kills_all_zombies: Whether this combination kills all zombies on the tile
#          items_consumed: List of items that are consumed in the combination
#      """
#     self.items_consumed = items_consumed

@dataclass
class CombinationResult:
    """Result of combining two items.
    
    Attributes:
        kills_all_zombies: Whether this combination kills all zombies on the tile
        items_consumed: List of items that are consumed in the combination
    """
    kills_all_zombies: bool = False
    items_consumed: List[IItem] = None

    def __post_init__(self):
        """Initialize items_consumed to empty list if None."""
        if self.items_consumed is None:
            self.items_consumed = []
