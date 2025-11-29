from src.model_after_pattern import (
    CombatStrategy,
)

class MockEngageStrategy(CombatStrategy):
    def execute(self, player, num_zombies):
        """"""
        pass
        
    def calculate_damage(self, zombie_count: int, player_attack: int):
        """Returns damage to be taken after combat action."""
        if zombie_count < 0:
            raise ValueError("Number of zombies must be > 0")
        if player_attack < 0:
            raise ValueError("Player attack must be >= 0")
        
        return max(0, zombie_count - player_attack)
        