from abc import ABC, abstractmethod

# --- Strategy Interface ---
class CombatAction(ABC):
    @abstractmethod
    def execute(self, player):
        pass
