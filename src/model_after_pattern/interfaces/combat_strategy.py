from abc import ABC, abstractmethod

# --- Strategy Interface ---
# class CombatStrategy(ABC):
#     @abstractmethod
#     def execute(self, player):
#         pass
# Strategy Interface
class CombatStrategy(ABC):
    @abstractmethod
    def execute(self, player, num_zombies):
        pass
        # print("hello from interface")
    # def execute(self, player, **kwargs):
    #     raise NotImplementedError("Must implement execute method")

    def calculate_damage(self, num_zombies, player_attack):
        """Returns damage to be taken after combat action."""
        if num_zombies < 0:
            raise ValueError("Number of zombies must be > 0")
        if player_attack < 0:
            raise ValueError("Player attack must be >= 0")
        
        return max(0, num_zombies - player_attack)
        