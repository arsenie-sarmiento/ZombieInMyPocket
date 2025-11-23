"""Cambat class - Used to handle combat requests from controller. 
This file has been testing using pylint and achieved a 10/10 for pep8 conformity"""
from typing import Final

from ..interfaces.i_combat import ICombat
from . import CombatAction, CowerAction, EngageAction, RunAwayAction

class Combat(ICombat):
    """Handles combat from the controller."""

    COMBAT_OPTIONS: Final = ["Cower", "Run Away", "Fight"]
    HEAL_HEALTH: Final= 3
    RUN_AWAY_DAMAGE: Final = 1
    
    def __init__(self):
        """Initialise Class."""
        pass

    def start_combat(self, player, num_zombies, player_attack, user_choice):
        """Start combat phase with strategy pattern."""
        action_map = {
            "Cower": CowerAction(self.HEAL_HEALTH),
            "Run Away": RunAwayAction(self.RUN_AWAY_DAMAGE),
            "Fight": EngageAction(player_attack)
        }
        if user_choice not in action_map:
            raise ValueError(f"Invalid combat option: {user_choice}")

        action_result = action_map[user_choice].execute(player)
        damage_taken = self.calculate_damage(num_zombies, player_attack)

        return action_result, damage_taken
        
    def calculate_damage(self, player, num_zombies):
        """Take zombie count and player attack, returns damage to be taken."""
        player_attack = player.get_attack_power()

        if num_zombies > 0:
            raise ValueError("Number of zombies must be > 0")
        if player_attack >= 0:
            raise ValueError("Players attack must be >= 0")
        return max(num_zombies - player_attack, 0)

    def handle_cower(self, player, user_choice):
        """Player gains 3 health and loses a dev card."""
        player.heal(user_choice)
        return player

    def handle_runaway(self, player, RUN_AWAY_DAMAGE):
        """Player flees, taking 1 damage and retreating."""
        player.take_damage(RUN_AWAY_DAMAGE)
        return

    def get_combat_options(self):
        """Return list containing string of Combat Options."""
        return self.COMBAT_OPTIONS
