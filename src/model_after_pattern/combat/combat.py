from typing import Final

from src.model.player.player import Player
from ..enums.combat_option import CombatOption
from .cower_strategy import CowerStrategy
from .runaway_strategy import RunAwayStrategy
from .engage_strategy import EngageStrategy

class Combat(object):
    """REFACTORED Combat (context)"""

    def __init__(self, combat_mode:  CombatOption =  CombatOption.COWER) -> None:
        self.__combat_mode = combat_mode

        self.strategy_map: Final = {
            CombatOption.COWER: CowerStrategy(),
            CombatOption.RUN_AWAY: RunAwayStrategy(),
            CombatOption.ENGAGE: EngageStrategy()
        }

    def set_combat_strategy(self, combat_mode: CombatOption) -> None:
        if combat_mode not in self.strategy_map:
            raise ValueError(f"Invalid combat option: {combat_mode}")
        else:
            self.__combat_mode = combat_mode

    def start_combat(self, player: Player, zombie_count: int) -> None:
        """Start combat phase using Strategy pattern."""

        strategy = self.strategy_map[self.__combat_mode]
        strategy.execute(player, zombie_count)