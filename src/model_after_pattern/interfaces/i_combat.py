from abc import ABC, abstractmethod

# --- Context Interface ---
class ICombat(ABC):
    @abstractmethod
    def start_combat(self, player, zombie_count):
        """Start the combat phase for the given player."""
        pass

    @abstractmethod
    def set_combat_strategy(self, combat_choice):
        """Set the combat strategy based on the player's choice."""
        pass