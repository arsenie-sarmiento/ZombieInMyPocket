from typing import Final
from ..enums.combat_option import CombatOption
from .cower_strategy import CowerStrategy
from .runaway_strategy import RunAwayStrategy
from .engage_strategy import EngageStrategy

class Combat(object):
    """REFACTORED Combat (context)"""

    
    def __init__(self, combat_mode):
        self.__combat_mode = combat_mode

        self.strategy_map = {
            CombatOption.COWER: CowerStrategy(),
            CombatOption.RUN_AWAY: RunAwayStrategy(),
            CombatOption.ENGAGE: EngageStrategy()
        }

    def set_combat_strategy(self, combat_mode):
        if combat_mode not in self.strategy_map:
            raise ValueError(f"Invalid combat option: {combat_mode}")
        else:
            self.__combat_mode = combat_mode

    def start_combat(self, player, zombie_count):
        """Start combat phase using Strategy pattern."""

        print(f"Combat mode: {self.__combat_mode.name}")
        strategy = self.strategy_map[self.__combat_mode]
        strategy.execute(player, zombie_count)
        return player