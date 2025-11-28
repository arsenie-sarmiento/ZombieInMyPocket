import unittest
from tests.mocks.player import MockPlayer
# from tests.mocks.strategy import MockEngageStrategy
from src.model.combat import Combat


class TestCombatStart(unittest.TestCase):
    """Unit tests for Combat.start_combat behavior without exposing strategy pattern."""

    def setUp(self):
        self.player = MockPlayer(health=6, attack_power=2)
        self.combat = Combat()
        self.num_zombies = 4
        self.player_attack = self.player.attack_power

    def test_start_combat_cower_increases_health(self):
        """Cower choice should heal the player correctly."""
        user_choice = "Cower"
        self.combat.start_combat(
            self.player, self.num_zombies, self.player_attack, user_choice
        )
        expected_health = 9  # +3 from cower
        self.assertEqual(self.player.health, expected_health)
        self.assertIsInstance(self.player, MockPlayer)

    def test_start_combat_run_away_decreases_health(self):
        """Run Away choice should reduce player health appropriately."""
        user_choice = "Run Away"
        self.combat.start_combat(
            self.player, self.num_zombies, self.player_attack, user_choice
        )
        expected_health = 5
        expected_damage_taken = 1
        self.assertEqual(self.player.health, expected_health)
        self.assertEqual(self.player.damage_taken, expected_damage_taken)

    def test_start_combat_engage_calculates_damage(self):
        """Engage choice should correctly apply damage to the player."""
        user_choice = "Fight"
        actual_damage = self.combat.start_combat(
            self.player, self.num_zombies, self.player_attack, user_choice
        )
        expected_damage = 2  # calculated from num_zombies - player_attack
        expected_health = self.player.health  # health updated inside start_combat
        self.assertEqual(actual_damage, expected_damage)
        self.assertEqual(self.player.health, expected_health)

    def test_start_combat_invalid_choice_raises_error(self):
        """Invalid combat choice should raise a ValueError."""
        user_choice = "Fly Away"
        with self.assertRaises(ValueError) as cm:
            self.combat.start_combat(
                self.player, self.num_zombies, self.player_attack, user_choice
            )
        self.assertIn("Please choose a combat option", str(cm.exception))


class TestCalculateDamage(unittest.TestCase):
    """Unit tests for Combat.calculate_damage method."""

    def setUp(self):
        self.combat = Combat()

    def test_calculate_damage_normal_cases(self):
        """Test normal damage calculation."""
        test_cases = [
            (5, 3, 2),
            (2, 5, 0),
            (10, 10, 0),
            (0, 0, 0),
        ]
        for num_zombies, player_attack, expected in test_cases:
            with self.subTest(num_zombies=num_zombies, player_attack=player_attack):
                result = self.combat.calculate_damage(num_zombies, player_attack)
                self.assertEqual(result, expected)

    def test_calculate_damage_invalid_num_zombies(self):
        """Negative num_zombies should raise ValueError."""
        for num_zombies in [-1, -5, -10]:
            with self.subTest(num_zombies=num_zombies):
                with self.assertRaises(ValueError):
                    self.combat.calculate_damage(num_zombies, player_attack=5)

    def test_calculate_damage_invalid_player_attack(self):
        """Negative player_attack should raise ValueError."""
        for attack in [-1, -10]:
            with self.subTest(player_attack=attack):
                with self.assertRaises(ValueError):
                    self.combat.calculate_damage(num_zombies=5, player_attack=attack)


if __name__ == "__main__":
    unittest.main()

# ===============================
#   Combat Start Tests
# ===============================
# class TestCombatStart(unittest.TestCase):
#     """Tests Combat.start_combat() across all strategies."""

#     def setUp(self):
#         self.player = MockPlayer(health=6, attack_power=2)
#         self.combat = Combat(CombatOption.COWER)

#     # -----------------------------------------------------
#     # Cower Strategy
#     # ---------------------------------------------------------
#     def test_cower_heals_player(self):
#         """ """
#         zombie_count = 4
#         self.combat.set_combat_strategy(CombatOption.COWER)
#         self.combat.start_combat(self.player, zombie_count)

#         expected = 9  # +3 HP from cower strategy
#         self.assertEqual(self.player.health, expected)
#         self.assertIsInstance(self.player, MockPlayer)

#     # -----------------------------------------------------
#     # Run Away Strategy
#     # -----------------------------------------------------
#     def test_runaway_takes_damage(self):
#         self.combat.set_combat_strategy(CombatOption.RUN_AWAY)

#         print(f'Health:{self.player.health}')

#         zombie_count = 4
#         expected_health = 5

#         self.combat.start_combat(self.player, zombie_count)
#         self.assertEqual(self.player.health, expected_health)

#     # -----------------------------------------------------
#     # Engage Strategy
#     # -----------------------------------------------------
#     def test_engage_and_takes_damage(self):
#         self.combat.set_combat_strategy(CombatOption.ENGAGE)

#         print(f'Health:{self.player.health}')

#         zombie_count = 4
#         expected_damage = 2
#         expected_health = 4

#         self.combat.start_combat(self.player, zombie_count)

#         self.assertEqual(self.player.damage_taken, expected_damage)
#         self.assertEqual(self.player.health, expected_health)

# ===============================
#   Take Damage Tests
# ===============================
# class TestDamageCalculation(unittest.TestCase):
#     """Tests for the calculate_damage method."""
#     def setUp(self):
#         self.player = MockPlayer(health=6, attack_power=1)
#         self.strategy = MockEngageStrategy()

#     def test_calculate_fight_damage_valid(self):
#         cases = [
#             (5, 3, 2),
#             (2, 5, 0),
#             (10, 10, 0),
#             (0, 0, 0),
#         ]

#         for num_zombies, attack, expected in cases:
#             with self.subTest(
#                 zombies=num_zombies, attack=attack, expected=expected
#             ):
#                 self.assertEqual(
#                     self.strategy.calculate_damage(num_zombies, attack),
#                     expected,
#                 )

# =====================================================
#   Run All Tests
# =====================================================
if __name__ == "__main__":
    unittest.main()