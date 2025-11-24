from typing import Final
from ..interfaces.combat_strategy import CombatStrategy

class RunAwayStrategy(CombatStrategy):
    """"""
    # RUN_AWAY_DAMAGE: Final = 1

    def __init__(self, damage):
        self.damage = damage

    def execute(self, player, zombie_count):
        print('Running away')
        player.take_damage(self.damage)
        return player