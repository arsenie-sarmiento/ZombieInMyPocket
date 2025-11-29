from ..interfaces.combat_strategy import CombatStrategy

class EngageStrategy(CombatStrategy):
    def __init__(self):
        pass

    def execute(self, player, zombie_count):
        attack_power = player.attack_power
        damage = self.calculate_damage(zombie_count, attack_power)
        player.take_damage(damage)

        # return self.get_current_health(player)
    
    def calculate_damage(self, zombie_count: int, player_attack: int):
        """Returns damage to be taken after combat action."""
        if zombie_count < 0:
            raise ValueError("Number of zombies must be > 0")
        if player_attack < 0:
            raise ValueError("Player attack must be >= 0")
        
        return max(0, zombie_count - player_attack)
        