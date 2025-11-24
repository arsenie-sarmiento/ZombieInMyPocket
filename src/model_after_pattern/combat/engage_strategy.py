from ..interfaces.combat_strategy import CombatStrategy

# class EngageStrategy(CombatAction):
#     def __init__(self, damage_to_zombies):
#         self.damage_to_zombies = damage_to_zombies

#     def execute(self, player):
#         # Example: you could add fight-specific logic here
#         return f"{player.name} fights for {self.damage_to_zombies} damage!"

class EngageStrategy(CombatStrategy):
    def __init__(self):
        pass

    def execute(self, player, zombie_count):
        # Placeholder: define fight logic here
        print('Engagigng...FIGHTTTTT')
        # Example: player.attack() or custom logic
        attack_power = player.attack_power
        # Number of zombies - Attack power -> calculate damage received
        current_health = player.health
        damage = self.calculate_damage(zombie_count, attack_power)

        # Health - damage received = new health
        player.take_damage(damage)
        # player.damage_taken = damage

        return player
    
    # def calculate_fight_damage(self, num_zombies, player_attack):
    #     """Returns damage to be taken after combat action."""
    #     if num_zombies < 0:
    #         raise ValueError("Number of zombies must be > 0")
    #     if player_attack < 0:
    #         raise ValueError("Player attack must be >= 0")
    #     return max(num_zombies - player_attack, 0)