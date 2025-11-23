"""Interface definitions for the Zombie in My Pocket game.

This module contains all the abstract base classes (interfaces) that define
the contracts for various game components including items, tiles, encounters,
players, and game management objects.
"""

from .i_game_time import IGameTime
from .i_item import IItem
from .i_player import IPlayer
from .i_combat import ICombat


__all__ = [
    'IGameTime',
    'IItem',
    'IPlayer',
    'ICombat'
]
