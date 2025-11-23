from abc import ABC, abstractmethod

# --- Strategy Interface ---
# class CombatStrategy(ABC):
#     @abstractmethod
#     def execute(self, player):
#         pass
# Strategy Interface
class CombatStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass
        # print("hello from interface")
    # def execute(self, player, **kwargs):
    #     raise NotImplementedError("Must implement execute method")