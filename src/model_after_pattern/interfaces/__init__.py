"""Interface definitions for the Zombie in My Pocket game.

This module contains all the abstract base classes (interfaces) that define
the contracts for various game components including items, tiles, encounters,
players, and game management objects.
"""

from .combat_strategy import CombatStrategy
from .game_time_component import GameTimeComponent
from .i_item import IItem
from .i_player import IPlayer

__all__ = [
    'CombatStrategy',
    'GameTimeComponent',
    'IItem',
    'IPlayer',
]
