from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
   from domain.state.map.tile import Tile


class FutureTile:

    def __init__(self, tile: Tile, at_least_one_face: set[int]):
        # this is the underlying current tile of the map
        self.tile = tile
        # this is a constraint (usually coming from a neighboring tile that will be extended)
        self.at_least_one_face = at_least_one_face

    def __str__(self):
        return f"FutureTile({self.tile.c}, faces={self.at_least_one_face})"

    def matches(self, tile: Tile):
        # TODO we should also take into account the current underlying tile
        a = tile.get_connected_edges()
        b = self.at_least_one_face
        return len(a.intersection(b)) > 0
