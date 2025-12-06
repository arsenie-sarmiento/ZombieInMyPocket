"""Interface definitions for the Zombie in My Pocket game.

This module contains all the abstract base classes (interfaces) that define
the contracts for various game components including items, tiles, encounters,
players, and game management objects.
"""

from .combat_strategy import CombatStrategy
# from .game_time_component import GameTimeComponent
from .i_player import IPlayer
from .i_encounter import IEncounter
from .i_dev_card import IDevCard
from .i_tile import ITile
from .i_board import IBoard
from .i_game_pieces_factory import IGamePiecesFactory

__all__ = [
    'CombatStrategy',
    'IDevCard',
    'IPlayer',
    'IEncounter',
    'IBoard',
    'ITile',
    'IGamePiecesFactory',
]
