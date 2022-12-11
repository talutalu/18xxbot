from __future__ import annotations
from __future__ import annotations

from domain.state.map.future_tile import FutureTile
from domain.state.map.route import Route

from typing import TYPE_CHECKING, Dict, Tuple, List

if TYPE_CHECKING:  # Only imports the below statements during type checking
   from domain.state.map.tile import Tile
   from domain.state.map_state import MapState


class City:

    def __init__(self, tile: Tile, connection: int):
        self.tile = tile
        self.connection = connection
        self.routes: list[Route] = [Route(tile.x, tile.y, face) for face in set(tile.connections[connection])]

        self.route_extensions: dict[tuple[int, int], list[Route]] = {}

    def refresh_route_extensions(self, ms: MapState):
        self.legal_new_tiles(ms)

    def legal_new_tiles(self, ms: MapState) -> list[FutureTile]:
        self.route_extensions = {}
        future_tiles: dict[tuple[int, int], FutureTile] = {}
        for route in self.routes:
            lastc = route.clist[-1]
            n = ms.neighbor(lastc[0], lastc[1], route.ending_face)
            if not n or not n.is_empty():
                continue
            ft = future_tiles.get(lastc, None)
            if not ft:
                ft = FutureTile(n, set())
                future_tiles[lastc] = ft
            ft.at_least_one_face.add((route.ending_face + 3) % 6)

            if lastc not in self.route_extensions:
                self.route_extensions[lastc] = []
            self.route_extensions[lastc].append(route)

        return list(future_tiles.values())

    def update_routes(self, tile: Tile):
        """
        :param tile: a new tile that the user upgraded/put
        :return: all the roads that where updated
        """
        pass


