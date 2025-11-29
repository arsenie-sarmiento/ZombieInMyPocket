import unittest
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
    def test_cower_heals_player(self):
        """Test that the Cower strategy increases health."""

        self.combat.set_combat_strategy(CombatOption.COWER)
        self.combat.start_combat(self.player, self.zombie_count)

        expected = 9  # +3 HP from cower strategy
        self.assertEqual(self.player.health, expected)
        self.assertIsInstance(self.player, MockPlayer)

    # -----------------------------------------------------
    # Run Away Strategy
    # -----------------------------------------------------
    def test_runaway_takes_damage(self):
        """Test that the Run Away strategy decreases health appropriately."""

        self.combat.set_combat_strategy(CombatOption.RUN_AWAY)

        print(f'Health:{self.player.health}')

        expected_health = 5

        self.combat.start_combat(self.player, self.zombie_count)
        self.assertEqual(self.player.health, expected_health)

    # -----------------------------------------------------
    # Engage Strategy
    # -----------------------------------------------------
    def test_engage_and_takes_damage(self):
        """Test that the Engage strategy adjusts health."""

        self.combat = Combat(CombatOption.ENGAGE)
        self.combat.set_combat_strategy(CombatOption.ENGAGE)

        print(f'Health:{self.player.health}')

        expected_damage = 1 # 3 zombies - 2 AP
        expected_health = 5 # 6HP - 1 (damage)

        self.combat.start_combat(self.player, self.zombie_count)

        self.assertEqual(self.player.damage_taken, expected_damage)
        self.assertEqual(self.player.health, expected_health)

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
        combat = Combat()

        invalid_option = "NOT_A_REAL_OPTION"

        with self.assertRaises(ValueError) as ctx:
            combat.set_combat_strategy(invalid_option)

        self.assertIn(f"Invalid combat option: {invalid_option}", str(ctx.exception))


# =====================================================
#   Run All Tests
# =====================================================
if __name__ == "__main__":
    unittest.main()