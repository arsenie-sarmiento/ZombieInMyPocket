from typing import Final
from ..interfaces.combat_strategy import CombatStrategy

class RunAwayStrategy(CombatStrategy):
    """"""

    def __init__(self, damage):
        self._damage = damage

    def execute(self, player, zombie_count):
        print('Running away')
        player.take_damage(self._damage)
        return player