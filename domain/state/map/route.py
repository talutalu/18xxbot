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

    def is_extended_by(self, tile: Tile):
        last = self.list[-1]
        if Coordinate.neighbor(last.c, last.b_face) != tile.c:
            return False
        return any((last.b_face + 3) % 6 in e for e in tile.connections) and len(tile.get_connected_edges()) <= 2

    def contains(self, c: Coordinate):
        return any(c == e.c for e in self.list)

    def merge(self, other: Route):
        pass

    def extend(self, tile: Tile):
        assert self.is_extended_by(tile)
        last = self.list[-1]
        connections = tile.get_connected_edges()
        a_face = (last.b_face + 3) % 6
        connections.remove(a_face)
        b_face = -1 if len(connections) == 0 else next(iter(connections))
        self.list.append(RouteAtom(tile.c, a_face, b_face))

    def fork(self, x: int, y: int, tile: Tile):
        pass

    def __repr__(self):
        return f"Route({self.list})"