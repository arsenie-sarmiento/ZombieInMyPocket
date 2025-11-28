from typing import Final
from ..interfaces.combat_strategy import CombatStrategy

class RunAwayStrategy(CombatStrategy):
    """"""

    RUN_AWAY_DAMAGE: Final = 1

    def __init__(self):
        pass

    def execute(self, player):
        print('Running away')
        player.take_damage(self.RUN_AWAY_DAMAGE)
        return self.get_current_health(player)