from ..interfaces.combat_strategy import CombatStrategy

class EngageStrategy(CombatStrategy):
    def __init__(self):
        pass

    def execute(self, player, zombie_count):
        attack_power = player.attack_power
        damage = self.calculate_damage(zombie_count, attack_power)
        player.take_damage(damage)

        return player