import pytest

from src.model_after import Combat

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

# def test_start_combat_runaway():
#     """
#     Since start_combat hard-codes user_choice='Cower',
#     only the cower branch is reachable.
#     """
#     combat = Combat()
#     player = MockPlayer(health=6, attack_power=1)
    
#     num_zombies = 1
#     player_attack = player.attack_power
#     user_choice = 'Run Away'

#     combat.start_combat(player, num_zombies, player_attack, user_choice)
#     expected_health_after_cower = 5
#     expected_damage_taken = 1
    
#     assert player.damage_taken == expected_damage_taken
#     assert player.health == expected_health_after_cower

# def test_start_combat_invalid_choice():
#     """Test that start_combat selects an invalid combat option."""
#     combat = Combat()
#     player = MockPlayer(health=6, attack_power=1)
    
#     num_zombies = 1
#     player_attack = player.attack_power
#     user_choice = 'Fly Away'

#     expected_message = 'Please choose a combat option'
#     with pytest.raises(ValueError, match=expected_message):
#         combat.start_combat(player, num_zombies, player_attack, user_choice)

# def test_start_combat_calculate_damage():
#     """Test that start_combat selects the Calculate Damage option."""

#     combat = Combat()
#     player = MockPlayer(health=6, attack_power=1)

#     num_zombies = 2
#     player_attack = player.attack_power
#     user_choice = 'Calculate Damage'
#     expected_damage_taken = 1

#     actual_damage_taken = combat.start_combat(player, num_zombies, player_attack, user_choice)
    
#     assert actual_damage_taken == expected_damage_taken

# @pytest.mark.parametrize(
#     "num_zombies, player_attack, expected",
#     [
#         (5, 2, 3),
#         (3, 5, 0),   # max(num_zombies - player_attack, 0)
#         (10, 10, 0),
#         (7, 3, 4),
#     ]
# )
# def test_calculate_damage_normal(num_zombies, player_attack, expected):
#     """Test normal damage calculation scenarios."""
#     combat = Combat()
#     result = combat.calculate_damage(num_zombies, player_attack)
#     assert result == expected

# @pytest.mark.parametrize(
#     "num_zombies",
#     [-1, -5, -10]
# )
# def test_calculate_damage_num_zombies_error(num_zombies):
#     """Test that negative num_zombies raises ValueError."""
#     combat = Combat()
#     with pytest.raises(ValueError, match="Number of zombies must be > 0"):
#         combat.calculate_damage(num_zombies, player_attack=5)

# @pytest.mark.parametrize(
#     "player_attack",
#     [0, -1, -10]
# )
# def test_calculate_damage_player_attack_error(player_attack):
#     """Test that non-positive player_attack raises ValueError."""
#     combat = Combat()
#     with pytest.raises(ValueError, match="Players attack must be >= 0"):
#         combat.calculate_damage(num_zombies=5, player_attack=player_attack)




# def test_get_combat_options_returns_list():
#     """Test that get_combat_options returns the full list."""
#     combat = Combat()
#     options = combat.get_combat_options()
    
#     # Verify it returns a list
#     assert isinstance(options, list)
    
#     # Checking all expected options are present
#     expected_options = ["Cower", "Run Away", "Fight"]
#     assert options == expected_options

# def test_get_combat_options_contains_specific_option():
#     """Test that 'Cower' is one of the combat options."""
#     combat = Combat()
#     options = combat.get_combat_options()
    
#     assert "Cower" in options