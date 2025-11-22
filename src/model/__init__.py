"""Package definitions for the Zombie in My Pocket game MODEL BEFORE PATTERN.

This module contains [].
"""

from .interfaces import IItem, IPlayer
from .game_time import GameTime
from .player import Player

__all__ = [
    'IItem',
    'IPlayer',
    'GameTime',
    'Player'
]
