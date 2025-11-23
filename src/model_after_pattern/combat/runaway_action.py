from .combat_action import CombatAction

class RunAwayAction(CombatAction):
    def __init__(self, damage):
        self.damage = damage

    def execute(self, player):
        player.take_damage(self.damage)
        return player