"""Interface definitions for the Zombie in My Pocket game.

This module contains [].
"""

from .game_time import GameTime
from .format_decorator import FormatDecorator
from .custom_message_decorator import MessageDecorator
from .base_decorator import GameTimeDecorator

__all__ = [
    'GameTime',
    'GameTimeDecorator',
    'FormatDecorator',
    'MessageDecorator'
]
