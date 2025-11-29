from abc import ABC, abstractmethod

# --- Strategy Interface ---
class CombatStrategy(ABC):

    @abstractmethod
    def execute(self, player, zombie_count):
        pass
