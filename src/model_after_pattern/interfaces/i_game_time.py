# gametime_interface.py
from typing import Protocol

class IGameTime(Protocol):
    """Abstraction for any GameTime implementation"""
    def get_hour(self) -> int:
        ...
    def increase_hour(self) -> None:
        ...
