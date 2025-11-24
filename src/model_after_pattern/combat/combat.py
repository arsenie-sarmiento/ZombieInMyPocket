from typing import Final
from ..enums.combat_option import CombatOption
from .cower_strategy import CowerStrategy
from .runaway_strategy import RunAwayStrategy
from .engage_strategy import EngageStrategy

class Combat(object):
    """REFACTORED Combat (context)"""

    # COMBAT_OPTIONS: Final = ["Cower", "Run Away", "Fight"]
    HEAL_HEALTH: Final = 3
    RUN_AWAY_DAMAGE: Final = 1
    
    def __init__(self, combat_choice):
        self.__combat_choice = combat_choice

        # Map enum to strategy instances
        self.strategy_map = {
            CombatOption.COWER: CowerStrategy(self.HEAL_HEALTH),
            CombatOption.RUN_AWAY: RunAwayStrategy(self.RUN_AWAY_DAMAGE),
            CombatOption.ENGAGE: EngageStrategy()
        }

    def set_combat_strategy(self, combat_choice):
        if combat_choice not in self.strategy_map:
            raise ValueError(f"Invalid combat option: {combat_choice}")
        else:
            self.__combat_choice = combat_choice

    def start_combat(self, player, zombie_count):
        """Start combat phase using Strategy pattern."""

        print(f"Combat choice: {self.__combat_choice.name}")
        strategy = self.strategy_map[self.__combat_choice]
        strategy.execute(player, zombie_count)
        return player
    
    def handle_damage(self, player, damage):
        # zombies vs attack score
        # damage vs health

        # if num_zombies < 0:
        #     raise ValueError("Number of zombies must be > 0")
        # if player_attack < 0:
        #     raise ValueError("Player attack must be >= 0")
        
        player.take_damage(damage)
    
    # def calculate_damage(self, num_zombies, player_attack):
    #     """Returns damage to be taken after combat action."""
    #     if num_zombies < 0:
    #         raise ValueError("Number of zombies must be > 0")
    #     if player_attack < 0:
    #         raise ValueError("Player attack must be >= 0")
        
    
    # def start_combat(self, player, zombie_count, player_attack, user_choice: CombatStrategy):
    #     """Start combat phase using Strategy pattern."""

    #     self.__combat_choice.execute(player)
    #     print("execute combat")
        # if user_choice not in self.strategy_map:
        #     raise ValueError(f"Invalid combat option: {user_choice}")

        # # Execute chosen combat action
        # strategy = self.strategy_map[user_choice]
        # strategy.execute(player)

        # # Always calculate damage after action
        # damage = self.calculate_damage(zombie_count, player_attack)
        # player.take_damage(damage)
        # return player



    # def get_combat_options(self):
    #     """Return list of combat options as strings."""
    #     return [option.name for option in CombatOption]

# if __name__ == '__main__':
#     """
#     The expected output:

#     Drive dangerously fast
#     crash and never arrive at all
#     Drive sensibly at a normal speed
#     arrive safely on time
#     Drive reeeallly slowly
#     arrive late and annoy your fellow motorists
#     """
#     print('hi')

#     cower = CowerStrategy(1)
#     cower.execute()
#     # fight = EngageStrategy()
#     # run = RunAwayStrategy()

#     # combat = Combat(cower)
#     # combat.start_combat()

#     # combat.set_combat_strategy(fight)
#     # combat.start_combat()

#     # combat.set_combat_strategy(run)
#     # combat.start_combat()
