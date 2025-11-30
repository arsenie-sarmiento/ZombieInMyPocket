from enum import Enum, auto

class CombatOption(Enum):
    IDLE = auto()
    COWER = auto()
    RUN_AWAY = auto()
    ENGAGE = auto()