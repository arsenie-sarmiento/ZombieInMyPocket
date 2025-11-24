import unittest
from unittest.mock import patch

from model_after_pattern import (
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
