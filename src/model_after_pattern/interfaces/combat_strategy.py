from abc import ABC, abstractmethod

# --- Strategy Interface ---
class CombatStrategy(ABC):

    @abstractmethod
    def execute(self, player, zombie_count: int):
        pass

    def get_current_health(self, player) -> int:
        """Returns the player's current health."""
        return player.health
 
    def calculate_damage(self, zombie_count: int, player_attack: int):
        """Returns damage to be taken after combat action."""
        if zombie_count < 0:
            raise ValueError("Number of zombies must be > 0")
        if player_attack < 0:
            raise ValueError("Player attack must be >= 0")
        
        return max(0, zombie_count - player_attack)
        