import unittest
from src.model.combat.combat import Combat
from mocks.player import MockPlayer


class TestCombatStart(unittest.TestCase):
    """Unit tests for Combat.start_combat method."""

    def setUp(self):
        self.player = MockPlayer(health=6, attack_power=1)
        self.combat = Combat()
        self.num_zombies = 1
        self.player_attack = self.player.attack_power

    def test_start_combat_cower(self):
        """Test that the Cower strategy increases health."""
        user_choice = "Cower"
        self.combat.start_combat(self.player, self.num_zombies, self.player_attack, user_choice)
        expected_health = 9
        self.assertEqual(self.player.health, expected_health)
        self.assertIsInstance(self.player, MockPlayer)

    def test_start_combat_runaway(self):
        """Test that the Run Away strategy decreases health appropriately."""
        user_choice = "Run Away"
        self.combat.start_combat(self.player, self.num_zombies, self.player_attack, user_choice)
        expected_health = 5
        expected_damage_taken = 1
        self.assertEqual(self.player.health, expected_health)
        self.assertEqual(self.player.damage_taken, expected_damage_taken)

    def test_start_combat_invalid_choice(self):
        """Test that an invalid combat choice raises ValueError."""
        user_choice = "Fly Away"
        with self.assertRaises(ValueError) as cm:
            self.combat.start_combat(self.player, self.num_zombies, self.player_attack, user_choice)
        self.assertIn("Please choose a combat option", str(cm.exception))

    def test_start_combat_calculate_damage(self):
        """Test that 'Calculate Damage' option returns correct damage."""
        self.num_zombies = 2
        user_choice = "Calculate Damage"
        actual_damage = self.combat.start_combat(self.player, self.num_zombies, self.player_attack, user_choice)
        expected_damage = 1
        self.assertEqual(actual_damage, expected_damage)


class TestCalculateDamage(unittest.TestCase):
    """Unit tests for Combat.calculate_damage method."""

    def setUp(self):
        self.combat = Combat()

    def test_calculate_damage_normal(self):
        """Test normal damage calculation scenarios."""
        cases = [
            (5, 2, 3),
            (3, 5, 0),
            (10, 10, 0),
            (7, 3, 4),
        ]
        for num_zombies, attack, expected in cases:
            with self.subTest(num_zombies=num_zombies, attack=attack):
                result = self.combat.calculate_damage(num_zombies, attack)
                self.assertEqual(result, expected)

    def test_calculate_damage_num_zombies_error(self):
        """Test that negative num_zombies raises ValueError."""
        for num_zombies in [-1, -5, -10]:
            with self.subTest(num_zombies=num_zombies):
                with self.assertRaises(ValueError) as cm:
                    self.combat.calculate_damage(num_zombies, player_attack=5)
                self.assertIn("Number of zombies must be > 0", str(cm.exception))

    def test_calculate_damage_player_attack_error(self):
        """Test that negative or zero player_attack raises ValueError."""
        for player_attack in [0, -1, -10]:
            with self.subTest(player_attack=player_attack):
                with self.assertRaises(ValueError) as cm:
                    self.combat.calculate_damage(num_zombies=5, player_attack=player_attack)
                self.assertIn("Players attack must be >=", str(cm.exception))


class TestCombatOptions(unittest.TestCase):
    """Unit tests for Combat.get_combat_options method."""

    def setUp(self):
        self.combat = Combat()

    def test_get_combat_options_returns_list(self):
        """Test that get_combat_options returns a list with all options."""
        options = self.combat.get_combat_options()
        self.assertIsInstance(options, list)
        expected_options = ["Cower", "Run Away", "Fight"]
        self.assertEqual(options, expected_options)

    def test_get_combat_options_contains_specific_option(self):
        """Test that 'Cower' is present in combat options."""
        options = self.combat.get_combat_options()
        self.assertIn("Cower", options)


if __name__ == "__main__":
    unittest.main()
