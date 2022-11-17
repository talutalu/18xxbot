from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
   from domain.state.map.tile import Tile


class FutureTile:

    def __init__(self, tile: Tile, at_least_one_face: set[int]):
        self.tile = tile
        self.at_least_one_face = at_least_one_face

    def __str__(self):
        return f"FutureTile({self.tile.x}, {self.tile.y}, faces={self.at_least_one_face})"