# from typing import Final
from ..interfaces import CombatStrategy

class CowerStrategy(CombatStrategy):
    """"""
    def __init__(self, heal_amount):
        self._heal_amount = heal_amount

    def execute(self, player, zombie_count):
        print(f'hello from cower: {self._heal_amount}')
        player.heal(self._heal_amount)
        return player
