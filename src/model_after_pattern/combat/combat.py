from typing import Final
from ..enums.combat_option import CombatOption
from .cower_strategy import CowerStrategy
from .runaway_strategy import RunAwayStrategy
from .engage_strategy import EngageStrategy

class Combat(object):
    """REFACTORED Combat (context)"""

    HEAL_HEALTH: Final = 3
    RUN_AWAY_DAMAGE: Final = 1
    
    def __init__(self, combat_choice):
        self.__combat_choice = combat_choice

        self.strategy_map = {
            CombatOption.COWER: CowerStrategy(self.HEAL_HEALTH),
            CombatOption.RUN_AWAY: RunAwayStrategy(self.RUN_AWAY_DAMAGE),
            CombatOption.ENGAGE: EngageStrategy()
        }

    def set_combat_strategy(self, combat_choice):
        if combat_choice not in self.strategy_map:
            raise ValueError(f"Invalid combat option: {combat_choice}")
        else:
            self.__combat_choice = combat_choice

    def start_combat(self, player, zombie_count):
        """Start combat phase using Strategy pattern."""

        print(f"Combat choice: {self.__combat_choice.name}")
        strategy = self.strategy_map[self.__combat_choice]
        strategy.execute(player, zombie_count)
        return player