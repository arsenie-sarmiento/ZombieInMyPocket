from abc import ABC, abstractmethod

from src.enums_and_types.enums import Direction, Rotation
from src.enums_and_types.types import Position
from src.model.game_pieces.board import TileDict
from src.model_after_pattern.interfaces.i_tile import ITile

class IBoard(ABC):

    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def get_all_tiles(self) -> TileDict:
        pass

    @abstractmethod
    def get_tile(self, position: Position) -> ITile | None:
        pass

    @abstractmethod
    def place_tile(
        self, new_tile: ITile, 
        new_exit: Direction,
        placed_tile: ITile | None,
        placed_tile_exit: Direction
    ) -> None:
        pass

    @abstractmethod
    def can_move_to_new_tile(
         self, 
         placed_tile: ITile,
         placed_tile_exit: Direction
    ) -> bool:
            pass
    
    @abstractmethod
    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        pass

    @abstractmethod
    def __can_place_tile(self, new_tile: ITile,
                         placed_tile: ITile,
                         placed_tile_exit: Direction) -> bool:
        pass
    
    @abstractmethod
    def __get_rotation_to_align_door(self, new_exit: Direction,
                                     placed_tile_exit: Direction) -> Rotation:
        pass

    @abstractmethod
    def get_tile_position(self, tile: ITile) -> Position:
        pass

    @abstractmethod
    def is_stuck(self) -> bool:
        pass

    @abstractmethod
    def _direction_from_position(
        self,
        position_from: Position,
        position_to: Position
    ) -> Direction:
        pass

    @abstractmethod
    def __move_position(self, pos: Position, dir: Direction) -> Position:
        pass

    @abstractmethod
    def __reverse_direction(self, dir: Direction) -> Direction:
        pass