from typing import Final

from ..player.player import Player
from ..interfaces.combat_strategy import CombatStrategy
from ..enums.combat_option import CombatOption
from .cower_strategy import CowerStrategy
from .runaway_strategy import RunAwayStrategy
from .engage_strategy import EngageStrategy

class Combat(object):
    """REFACTORED Combat (context)"""

    def __init__(self, combat_mode = CombatOption.IDLE) -> None:
        self.__combat_mode = combat_mode

        self.strategy_map: Final = {
            CombatOption.COWER: CowerStrategy(),
            CombatOption.RUN_AWAY: RunAwayStrategy(),
            CombatOption.ENGAGE: EngageStrategy()
        }

    def set_combat_strategy(self, combat_mode: CombatOption) -> None:
        if not isinstance(combat_mode, CombatOption):
            raise TypeError(
                f"combat_mode must be a CombatOption enum, got {type(combat_mode).__name__}"
            )
        else:
            print(f"Setting combat strategy to {combat_mode}")
            pass
            try:
                strategy = self.strategy_map[combat_mode]
            except KeyError:
                raise ValueError(
                    f"No strategy defined for combat option: {combat_mode}"
                ) from None
            self.__combat_mode = strategy

    def start_combat(self, player: Player, zombie_count: int) -> None:
        """Start combat phase using Strategy pattern."""
        self.__combat_mode.execute(player, zombie_count)

    def get_current_mode(self) -> CombatStrategy:
        """Return current combat mode strategy."""
        return self.__combat_mode