import unittest
from src.model_after_pattern import (
    Combat,
    CombatOption,
    CombatStrategy,
    CowerStrategy,
    RunAwayStrategy,
    EngageStrategy,
)


# ---------------------------
#   Mock Player Class
# ---------------------------
class MockPlayer:
    """Mock Player class for testing combat behavior."""

    def __init__(self, health: int = 6, attack_power: int = 1):
        self.health: int = health
        self.attack_power: int = attack_power
        self.damage_taken: int = 0

    def heal(self, amount: int):
        """Increase health by a positive amount."""
        if amount > 0:
            self.health += amount

    def take_damage(self, amount: int):
        """Reduce health by a positive amount."""
        if amount > 0:
            self.health -= amount
            self.damage_taken = amount

        if self.health < 0:
            self.health = 0

# ===============================
#   Combat Strategy Mapping Tests
# ===============================
class TestCombatStrategies(unittest.TestCase):
    """Tests strategy mapping and strategy-setting behavior."""

    def test_strategy_mapping(self):
        combat = Combat(CombatOption.COWER)

        self.assertIsInstance(
            combat.strategy_map[CombatOption.COWER], CowerStrategy
        )
        self.assertIsInstance(
            combat.strategy_map[CombatOption.RUN_AWAY], RunAwayStrategy
        )
        self.assertIsInstance(
            combat.strategy_map[CombatOption.ENGAGE], EngageStrategy
        )

    def test_set_invalid_strategy(self):
        combat = Combat(CombatOption.COWER)

        with self.assertRaises(ValueError):
            combat.set_combat_strategy("WRONG_OPTION")

# ===============================
#   Combat Start Tests
# ===============================
class TestCombatStart(unittest.TestCase):
    """Tests Combat.start_combat() across all strategies."""

    def setUp(self):
        self.player = MockPlayer(health=6, attack_power=2)
        self.combat = Combat(CombatOption.COWER)

    # -----------------------------------------------------
    # Cower Strategy
    # -----------------------------------------------------
    def test_cower_heals_player(self):
        """ """
        zombie_count = 4
        self.combat.set_combat_strategy(CombatOption.COWER)
        self.combat.start_combat(self.player, zombie_count)

        expected = 9  # +3 HP from cower strategy
        self.assertEqual(self.player.health, expected)
        self.assertIsInstance(self.player, MockPlayer)

    # -----------------------------------------------------
    # Run Away Strategy
    # -----------------------------------------------------
    def test_runaway_takes_damage(self):
        self.combat.set_combat_strategy(CombatOption.RUN_AWAY)

        print(f'Health:{self.player.health}')

        zombie_count = 4
        expected_health = 5

        self.combat.start_combat(self.player, zombie_count)
        self.assertEqual(self.player.health, expected_health)

    # -----------------------------------------------------
    # Engage Strategy
    # -----------------------------------------------------
    def test_engage_and_takes_damage(self):
        self.combat.set_combat_strategy(CombatOption.ENGAGE)

        print(f'Health:{self.player.health}')

        zombie_count = 4
        expected_damage = 2
        expected_health = 4

        self.combat.start_combat(self.player, zombie_count)

        self.assertEqual(self.player.damage_taken, expected_damage)
        self.assertEqual(self.player.health, expected_health)

# ---------------------------
#   Mock EngageStrategy Class
# ---------------------------

class MockEngageStrategy(CombatStrategy):
    def execute(self, player, num_zombies):
        pass

# ===============================
#   Take Damage Tests
# ===============================
class TestDamageCalculation(unittest.TestCase):
    """Tests for the calculate_damage method."""
    def setUp(self):
        self.player = MockPlayer(health=6, attack_power=1)
        self.strategy = MockEngageStrategy()

    def test_calculate_fight_damage_valid(self):
        cases = [
            (5, 3, 2),
            (2, 5, 0),
            (10, 10, 0),
            (0, 0, 0),
        ]

        for num_zombies, attack, expected in cases:
            with self.subTest(
                zombies=num_zombies, attack=attack, expected=expected
            ):
                self.assertEqual(
                    self.strategy.calculate_damage(num_zombies, attack),
                    expected,
                )

    # def test_take_damage_overkill(self):
    #     self.player.health = 1
    #     self.player.take_damage(15)
    #     self.assertEqual(self.player.health, 0)
    #     self.assertEqual(self.player.damage_taken, 15)

# =====================================================
#   Run All Tests
# =====================================================
if __name__ == "__main__":
    unittest.main()




# def test_start_combat_invalid_choice():
#     """Test that start_combat selects an invalid combat option."""
#     combat = Combat(CombatOption.COWER)
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

# -------------------------------
# Tests for MockPlayer itself
# -------------------------------
# class TestMockPlayer(unittest.TestCase):
#     """Test basic player methods: take_damage and heal."""

#     def setUp(self):
#         self.player = MockPlayer(health=6, attack_power=1)


    # def test_calculate_fight_damage_invalid(self):
    #     with self.assertRaises(ValueError):
    #         self.strategy.calculate_damage(-1, 2)

    #     with self.assertRaises(ValueError):
    #         self.strategy.calculate_damage(3, -1)

    # def test_take_damage_positive(self):
    #     self.player.take_damage(3)
    #     self.assertEqual(self.player.health, 7)
    #     self.assertEqual(self.player.damage_taken, 3)

    # def test_take_damage_overkill(self):
    #     self.player.take_damage(15)
    #     self.assertEqual(self.player.health, 0)
    #     self.assertEqual(self.player.damage_taken, 15)

    # def test_take_damage_negative(self):
    #     self.player.take_damage(-5)
    #     self.assertEqual(self.player.health, 10)
    #     self.assertEqual(self.player.damage_taken, 0)

    # def test_heal_positive(self):
    #     self.player.take_damage(5)
    #     self.player.heal(3)
    #     self.assertEqual(self.player.health, 8)

    # def test_heal_negative(self):
    #     self.player.heal(-3)
    #     self.assertEqual(self.player.health, 10)

    # def test_take_damage_negative(self):
    #     self.player.take_damage(-5)
    #     self.assertEqual(self.player.health, 10)
    #     self.assertEqual(self.player.damage_taken, 0)

    # def test_calculate_fight_damage_invalid(self):
    #     with self.assertRaises(ValueError):
    #         self.strategy.calculate_damage(-1, 2)

    #     with self.assertRaises(ValueError):
    #         self.strategy.calculate_damage(3, -1)