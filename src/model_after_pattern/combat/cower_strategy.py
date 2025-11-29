from typing import Final
from ..interfaces import CombatStrategy

class CowerStrategy(CombatStrategy):
    """"""

    HEAL_AMOUNT: Final = 3

    def __init__(self):
        pass
        
    def execute(self, player, zombie_count):
        print(f'hello from cower: {self.HEAL_AMOUNT}')
        player.heal(self.HEAL_AMOUNT)
        # return self.get_current_health(player)
