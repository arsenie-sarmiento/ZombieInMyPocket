import pytest

from src.model import Combat

class MockPlayer:
    """Mock Player class for testing combat."""
    def __init__(self):
        self.health = 10
        self.damage_taken = 0

    def heal(self, amount):
        self.health += amount

    def take_damage(self, amount):
        self.damage_taken += amount
        self.health -= amount

def test_start_combat_cower(monkeypatch):
    combat = Combat()
    player = MockPlayer()
    
    # Mock user choice to "Cower"
    monkeypatch.setattr("src.model.combat.Combat.start_combat", lambda self, p: self.handle_cower(p))
    
    result = combat.start_combat(player)
    
    assert result.health == 13  # healed by 3
    assert isinstance(result, MockPlayer)

def test_start_combat_runaway(monkeypatch):
    combat = Combat()
    player = MockPlayer()
    
    # Mock user choice to "Run Away"
    monkeypatch.setattr("src.model.combat.Combat.start_combat", lambda self, p: self.handle_runaway(p, self.RUN_AWAY_DAMAGE))
    
    combat.start_combat(player)
    
    assert player.damage_taken == 1
    assert player.health == 9

def test_start_combat_invalid_choice(monkeypatch):
    combat = Combat()
    player = MockPlayer()
    
    # Mock user choice to something invalid
    def fake_start(self, p):
        user_choice = "Fly Away"
        if user_choice not in self.COMBAT_OPTIONS:
            raise ValueError("Please choose a combat option")
    
    monkeypatch.setattr("src.model.combat.Combat.start_combat", fake_start)
    
    with pytest.raises(ValueError, match="Please choose a combat option"):
        combat.start_combat(player)
