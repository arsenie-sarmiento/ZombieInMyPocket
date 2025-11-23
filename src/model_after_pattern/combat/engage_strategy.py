from ..interfaces.combat_strategy import CombatStrategy

# class EngageStrategy(CombatAction):
#     def __init__(self, damage_to_zombies):
#         self.damage_to_zombies = damage_to_zombies

#     def execute(self, player):
#         # Example: you could add fight-specific logic here
#         return f"{player.name} fights for {self.damage_to_zombies} damage!"

class EngageStrategy(CombatStrategy):
    def execute(self, player, **kwargs):
        # Placeholder: define fight logic here
        print('Engagigng...FIGHTTTTT')
        # Example: player.attack() or custom logic
        return player