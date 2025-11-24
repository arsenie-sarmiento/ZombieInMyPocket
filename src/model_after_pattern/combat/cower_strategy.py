# from typing import Final
from ..interfaces import CombatStrategy

class CowerStrategy(CombatStrategy):
    """"""
    def __init__(self, heal_amount):
        self.heal_amount = heal_amount

    def execute(self, player, zombie_count):
        print(f'hello from cower: {self.heal_amount}')
        player.heal(self.heal_amount)
        return player
