from typing import Final

from ..enums.combat_option import CombatOption
from .cower_strategy import CowerStrategy
from .runaway_strategy import RunAwayStrategy
from .engage_strategy import EngageStrategy

class Combat(object):
    """REFACTORED Combat (context)"""

    def __init__(self, combat_mode) -> None:
        self.__combat_mode = combat_mode

        self.strategy_map: Final = {
            CombatOption.COWER: CowerStrategy(),
            CombatOption.RUN_AWAY: RunAwayStrategy(),
            CombatOption.ENGAGE: EngageStrategy()
        }

    def set_combat_strategy(self, combat_mode: CombatOption) -> None:
        # --- Validate type explicitly ---
        if not isinstance(combat_mode, CombatOption):
            raise TypeError(
                f"combat_mode must be a CombatOption enum, got {type(combat_mode).__name__}"
            )

        # --- Validate that this enum value has a mapped strategy ---
        try:
            strategy = self.strategy_map[combat_mode]
        except KeyError:
            raise ValueError(
                f"No strategy defined for combat option: {combat_mode}"
            ) from None
        
        self.__combat_mode = strategy
            

    def start_combat(self, player, zombie_count) -> None:
        """Start combat phase using Strategy pattern."""

        self.__combat_mode.execute(player, zombie_count)