# ---------------------------
#   Mock Player Class
# ---------------------------
class MockPlayer(object):
    """Mock Player class for testing combat behavior."""

    def __init__(self, health: int = 6, attack_power: int = 1):
        self.health: int = health
        self.attack_power: int = attack_power
        self.damage_taken: int = 0

    def heal(self, amount: int):
        """Increase health by a positive amount."""
        print(f'Healing amount: {amount}')
        if amount > 0:
            self.health += amount

    def take_damage(self, amount: int):
        """Reduce health by a positive amount."""
        print(f'Taking damage amount: {amount}')
        if amount > 0:
            self.health -= amount
            self.damage_taken = amount

        if self.health < 0:
            self.health = 0
