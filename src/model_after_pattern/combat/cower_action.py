from .combat_action import CombatAction

class CowerAction(CombatAction):
    def __init__(self, heal_amount):
        self.heal_amount = heal_amount

    def execute(self, player):
        player.heal(self.heal_amount)
        return player