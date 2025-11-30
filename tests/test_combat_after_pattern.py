import unittest
from unittest.mock import patch
from tests.mocks.player import MockPlayer
from tests.mocks.strategy import MockEngageStrategy
from src.model_after_pattern.interfaces.combat_strategy import CombatStrategy
from src.model_after_pattern import (
    Combat,
    CombatOption,
    CowerStrategy,
    RunAwayStrategy,
    EngageStrategy
)

# ===============================
#   Combat Start Tests
# ===============================
class TestCombatStart(unittest.TestCase):
    """Tests Combat.start_combat() across all strategies."""

    def setUp(self):
        self.player = MockPlayer(health=6, attack_power=2)
        self.zombie_count = 3
        self.combat = Combat(CombatOption.COWER)

    # -----------------------------------------------------
    # Cower Strategy
    # ---------------------------------------------------------
    def test_start_combat_cower_heals_player(self):
        """Test that the Cower strategy increases health."""

        self.combat.set_combat_strategy(CombatOption.COWER)
        self.combat.start_combat(self.player, self.zombie_count)

        expected = 9  # +3 HP from cower strategy
        self.assertEqual(self.player.health, expected)
        self.assertIsInstance(self.player, MockPlayer)

    # -----------------------------------------------------
    # Run Away Strategy
    # -----------------------------------------------------
    def test_start_combat_run_away_takes_damage(self):
        """Test that the Run Away strategy decreases health appropriately."""

        self.combat.set_combat_strategy(CombatOption.RUN_AWAY)
        self.combat.start_combat(self.player, self.zombie_count)

        expected_health = 5
        actual_health = self.player.health

        self.assertEqual(actual_health, expected_health)

    # -----------------------------------------------------
    # Engage Strategy
    # -----------------------------------------------------
    def test_start_combat_engage_and_takes_damage(self):
        """Test that the Engage strategy adjusts health."""

        self.combat = Combat(CombatOption.ENGAGE)
        self.combat.set_combat_strategy(CombatOption.ENGAGE)

        expected_damage = 1 # 3 zombies - 2 AP
        expected_health = 5 # 6HP - 1 (damage)

        self.combat.start_combat(self.player, self.zombie_count)
        actual_damage = self.player.damage_taken   

        self.assertEqual(actual_damage, expected_damage)
        self.assertEqual(self.player.health, expected_health)

# ===============================
#   Take Damage Tests
# ===============================
class TestDamageCalculation(unittest.TestCase):
    """Tests for the calculate_damage method."""
    def setUp(self):
        self.player = MockPlayer(health=6, attack_power=1)
        self.strategy = MockEngageStrategy()
        # self.combat = Combat(CombatOption.IDLE)
        # self.combat.set_combat_strategy(CombatOption.ENGAGE)
        # self.strategy = self.combat.get_current_mode()

    def test_calculate_fight_damage_valid(self):
        """Test normal damage calculation scenarios."""

        cases = [
            (5, 3, 2),
            (2, 5, 0),
            (10, 10, 0),
            (0, 0, 0),
        ]

        for zombie_count, attack, expected in cases:
            with self.subTest(
                zombies=zombie_count, attack=attack
            ):
                result = self.strategy.calculate_damage(zombie_count, attack)
                self.assertEqual(result, expected)

    def test_calculate_damage_zombie_count_error(self):
        """Test that negative zombie_count raises ValueError."""
        zombie_count = -1
        with self.assertRaises(ValueError) as cm:
            self.strategy.calculate_damage(zombie_count, player_attack=5)
        self.assertIn("Number of zombies must be > 0", str(cm.exception))

    def test_calculate_damage_player_attack_error(self):
        """Test that negative or zero player_attack raises ValueError."""

        player_attack = -1
        with self.assertRaises(ValueError) as cm:
            self.strategy.calculate_damage(zombie_count=5, player_attack=player_attack)
        self.assertIn("Player attack must be >= 0", str(cm.exception))

    def test_calculate_damage_num_zombies_error(self):
        """Test that negative num_zombies raises ValueError."""
        num_zombies = -1
        with self.assertRaises(ValueError) as cm:
            self.strategy.calculate_damage(num_zombies, player_attack=5)
        self.assertIn("Number of zombies must be > 0", str(cm.exception))

        
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

    def test_set_combat_strategy_invalid_option(self):
        combat = Combat(CombatOption.IDLE)

        invalid_option = "NOT_A_REAL_OPTION"

        with self.assertRaises(TypeError) as ctx:
            combat.set_combat_strategy(invalid_option)

        self.assertIn(
            "combat_mode must be a CombatOption enum", 
            str(ctx.exception)
        )

# ===============================
#   Combat Strategy Get Options Tests
# ===============================
class TestCombatOptions(unittest.TestCase):
    """Unit tests for Combat.get_combat_options method."""

    def setUp(self):
        self.combat = Combat()
        self.player = MockPlayer(health=6, attack_power=1)

    def test_get_combat_options_returns_list(self):
        """Test that get_combat_options returns a list with all options."""
        options = self.combat.get_combat_options()
        self.assertIsInstance(options, list)
        # expected_options = ["Cower", "Run Away", "Fight"]
        expected_options = [CombatOption.COWER, CombatOption.RUN_AWAY, CombatOption.ENGAGE]
        self.assertEqual(options, expected_options)

    def test_get_combat_options_contains_specific_option(self):
        """Test that 'Cower' is present in combat options."""
        options = self.combat.get_combat_options()
        self.assertIn(CombatOption.COWER, options)

    def test_start_combat_invalid_choice(self):
        """Test that an invalid combat choice raises ValueError."""
        from src.model_after_pattern.combat.combat import CombatOption

        # Pick a valid enum member that has no strategy defined
        self.combat.set_combat_strategy(CombatOption.IDLE)
        num_zombies = 2

        with self.assertRaises(ValueError) as cm:
            self.combat.start_combat(self.player, num_zombies)

        self.assertIn("No strategy defined for combat option:", str(cm.exception))


    # def test_start_combat_invalid_choice(self):
    #     """Test that an invalid combat choice raises ValueError."""
    #     # Patch the Enum in the module where it's used
    #     with patch('tests.mocks.enums.CombatOption') as MockEnum:
    #         # MockEnum.NOT_A_REAL_OPTION = "NOT_A_REAL_OPTION"
    #         self.combat.set_combat_strategy(MockEnum.NOT_A_REAL_OPTION)
    #         num_zombies = 2
    #         with self.assertRaises(ValueError) as cm:
    #             self.combat.start_combat(self.player, num_zombies)
    #         self.assertIn("Please choose a combat option", str(cm.exception))

    # =====================================================
#   Run All Tests
# =====================================================
if __name__ == "__main__":
    unittest.main()