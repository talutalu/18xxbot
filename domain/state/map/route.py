from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
   from domain.state.map.tile import Tile


class Route:

    def __init__(self, x: int, y: int, ending_face: int):
        """
        A route can be:
         . merged
         . extended
         . forked
        :param x: starting tile x coordinate
        :param y: starting tile y coordinate
        """
        self.clist: list[tuple[int, int]] = [(x, y)]
        self.ending_face = ending_face

    def contains(self, x: int, y: int):
        return (x, y) in self.clist

    def merge(self, other: Route):
        pass

    def extend(self, x: int, y: int, tile: Tile):
        pass

    def fork(self, x: int, y: int, tile: Tile):
        pass