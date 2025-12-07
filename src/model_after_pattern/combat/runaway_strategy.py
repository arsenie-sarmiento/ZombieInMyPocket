from typing import Final
from ..interfaces.combat_strategy import CombatStrategy

class RunAwayStrategy(CombatStrategy):
    """Handles combat strategy by running away."""

    RUN_AWAY_DAMAGE: Final = 1

    def __init__(self):
        pass

    def execute(self, player, zombie_count):
        print('Running away')
        player.take_damage(self.RUN_AWAY_DAMAGE)