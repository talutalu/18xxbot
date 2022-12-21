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

    def __init__(self, tile: Tile, connection: int):
        self.tile = tile
        self.connection = connection
        self.routes: list[Route] = [Route(RouteAtom(self.tile.c, -1, face))
                                    for face in set(tile.connections[connection])]

    def legal_new_tiles(self, ms: MapState) -> list[FutureTile]:
        """
        Legal new tiles that can continue (and not upgrade) one of the existing routes
        that starts with this city.
        """
        future_tiles: dict[Coordinate, FutureTile] = {}
        for route in self.routes:
            tip = route.list[-1]
            n = ms.neighbor(tip.c, tip.b_face)
            if not n or not n.is_empty():
                continue
            ft = future_tiles.get(tip.c, None)
            if not ft:
                ft = FutureTile(n, set())
                future_tiles[tip.c] = ft
            ft.at_least_one_face.add((tip.b_face + 3) % 6)
        return list(future_tiles.values())

    def update_routes(self, tile: Tile):
        """
        :param tile: a new tile that the user upgraded/put
        :return: all the roads that where updated
        """
        pass


