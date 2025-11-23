import pytest

from src.model import Combat

class MockPlayer:
    """Mock Player class for testing combat."""
    def __init__(self, health: int = 6):
        self.health = health
        self.damage_taken = 0

    def heal(self, amount):
        self.health += amount

    def take_damage(self, amount):
        self.damage_taken += amount
        self.health -= amount

def test_get_combat_options():
    """
    
    """

def test_start_combat_cower():
    """
    Since start_combat hard-codes user_choice='Cower',
    only the cower branch is reachable.
    """
    combat = Combat()
    player = MockPlayer(health=6)
    
    # Mock user choice to "Cower" by default
    user_choice = 'Cower'
    combat.start_combat(player, user_choice)

    expected_health_after_cower = 9  # healed by 3

    assert player.health == expected_health_after_cower 
    assert isinstance(player, MockPlayer)

def test_start_combat_runaway():
    """
    Since start_combat hard-codes user_choice='Cower',
    only the cower branch is reachable.
    """
    combat = Combat()
    player = MockPlayer(health=6)
    
    user_choice = 'Run Away'
    combat.start_combat(player, user_choice)
    expected_health_after_cower = 5
    
    assert player.damage_taken == 1
    assert player.health == expected_health_after_cower

# def test_start_combat_invalid_choice(monkeypatch):
#     combat = Combat()
#     player = MockPlayer()
    
#     def fake_start(self, p):
#         user_choice = "Fly Away"
#         if user_choice not in self.COMBAT_OPTIONS:
#             raise ValueError("Please choose a combat option")
    
#     monkeypatch.setattr("src.model.combat.Combat.start_combat", fake_start)
    
#     with pytest.raises(ValueError, match="Please choose a combat option"):
#         combat.start_combat(player)
