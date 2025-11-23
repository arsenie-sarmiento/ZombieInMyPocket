import pytest

from src.model import Combat

class MockPlayer:
    """Mock Player class for testing combat."""
    def __init__(self, health: int = 6, attack_power=1):
        self.health = health
        self.attack_power = attack_power
        self.damage_taken = 0

    def heal(self, amount):
        self.health += amount

    def take_damage(self, amount):
        self.damage_taken += amount
        self.health -= amount

    # def get_attack_power(self) -> int:
        # bonus = sum(item.attack_bonus for item in self._inventory if hasattr(item, 'attack_bonus'))
        # return self.attack_power + bonus

# def test_get_combat_options():
#     """

#     """

def test_start_combat_cower():
    """
    Since start_combat hard-codes user_choice='Cower',
    only the cower branch is reachable.
    """
    combat = Combat()
    player = MockPlayer(health=6, attack_power=1)
    
    num_zombies = 1
    player_attack = player.attack_power

    user_choice = 'Cower'
    combat.start_combat(player, num_zombies, player_attack, user_choice)

    expected_health_after_cower = 9

    assert player.health == expected_health_after_cower 
    assert isinstance(player, MockPlayer)

def test_start_combat_runaway():
    """
    Since start_combat hard-codes user_choice='Cower',
    only the cower branch is reachable.
    """
    combat = Combat()
    player = MockPlayer(health=6, attack_power=1)
    
    num_zombies = 1
    player_attack = player.attack_power
    user_choice = 'Run Away'

    combat.start_combat(player, num_zombies, player_attack, user_choice)
    expected_health_after_cower = 5
    expected_damage_taken = 1
    
    assert player.damage_taken == expected_damage_taken
    assert player.health == expected_health_after_cower

def test_start_combat_invalid_choice():
    """Test that start_combat selects an invalid combat option."""
    combat = Combat()
    player = MockPlayer(health=6, attack_power=1)
    
    num_zombies = 1
    player_attack = player.attack_power
    user_choice = 'Fly Away'

    expected_message = 'Please choose a combat option'
    with pytest.raises(ValueError, match=expected_message):
        combat.start_combat(player, num_zombies, player_attack, user_choice)

def test_start_combat_calculate_damage():
    """Test that start_combat selects the Calculate Damage option."""

    combat = Combat()
    player = MockPlayer(health=6, attack_power=1)

    num_zombies = 2
    player_attack = player.attack_power
    user_choice = 'Calculate Damage'
    expected_damage_taken = 1

    actual_damage_taken = combat.start_combat(player, num_zombies, player_attack, user_choice)
    
    assert actual_damage_taken == expected_damage_taken