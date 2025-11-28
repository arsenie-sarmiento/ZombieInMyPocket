from abc import ABC, abstractmethod

# --- Strategy Interface ---
class CombatStrategy(ABC):

    @abstractmethod
    def execute(self, player, zombie_count):
        pass

    def get_current_health(self, player) -> int:
        """Returns the player's current health."""
        return player.health
 