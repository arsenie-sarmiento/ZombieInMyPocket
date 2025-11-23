from typing import Final
from ..interfaces import CombatStrategy

class CowerStrategy(CombatStrategy):
    """"""

    HEAL_HEALTH: Final= 3

    def __init__(self, heal_amount):
        self.heal_amount = heal_amount

    def execute(self):
        print(f'hello from cower: {self.heal_amount}')
    # def execute(self, player, **kwargs):
        # print('Cowering, healing')
        # player.heal(self.heal_amount)
        # return player
