from __future__ import annotations
from __future__ import annotations

from domain.state.map.coordinate import Coordinate
from domain.state.map.future_tile import FutureTile
from domain.state.map.route import Route

from typing import TYPE_CHECKING, Dict, Tuple, List

from domain.state.map.route_atom import RouteAtom

if TYPE_CHECKING:  # Only imports the below statements during type checking
   from domain.state.map.tile import Tile
   from domain.state.map_state import MapState


class City:

    def __init__(self, tile: Tile, connection: int, for_clone=False):
        self.tile = tile
        self.connection = connection
        if for_clone:
            self.routes = None
        else:
            self.routes: list[Route] = [Route(RouteAtom(self.tile.c, None, face))
                                        for face in set(tile.connections[connection])]

    def clone(self):
        copy = City(self.tile, self.connection, for_clone=True)
        copy.routes = [r.clone() for r in self.routes]
        return copy

    def legal_new_tiles(self, ms: MapState) -> list[FutureTile]:
        """
        Legal new tiles that can continue (and not upgrade) one of the existing routes
        that starts with this city.
        """
        future_tiles: dict[Coordinate, FutureTile] = {}

        for route in self.routes:
            tip = route.list[-1]
            if tip.b_face is None:
                continue
            n = Coordinate.neighbor(tip.c, tip.b_face)
            n = ms.get_tile(n)
            if not n or not n.is_empty():
                continue
            ft = future_tiles.get(tip.c, None)
            if not ft:
                ft = FutureTile(n, set())
                future_tiles[tip.c] = ft
            ft.at_least_one_face.add((tip.b_face + 3) % 6)

        return list(future_tiles.values())

    def update_routes(self, tile: Tile):
        affected_routes = []

        for route in self.routes:
            if route.is_extended_by(tile):
                route.extend(tile)
                affected_routes.append(route)

        return affected_routes


