from __future__ import annotations
from typing import TYPE_CHECKING

from domain.state.map.coordinate import Coordinate
from domain.state.map.route_atom import RouteAtom

if TYPE_CHECKING:  # Only imports the below statements during type checking
   from domain.state.map.tile import Tile
   from domain.state.map.city import City


class Route:

    def __init__(self, atom: RouteAtom):
        """
        A route can be:
         . merged
         . extended
         . forked
        """
        self.list: list[RouteAtom] = [atom]

    def contains(self, c: Coordinate):
        return any(c == e.c for e in self.list)

    def merge(self, other: Route):
        pass

    def extend(self, x: int, y: int, tile: Tile):
        pass

    def fork(self, x: int, y: int, tile: Tile):
        pass