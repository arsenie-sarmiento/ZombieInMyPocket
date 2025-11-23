from .combat_action import CombatAction

class EngageAction(CombatAction):
    def __init__(self, damage_to_zombies):
        self.damage_to_zombies = damage_to_zombies

    def execute(self, player):
        # Example: you could add fight-specific logic here
        return f"{player.name} fights for {self.damage_to_zombies} damage!"
