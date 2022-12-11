from domain.state.map.future_tile import FutureTile
from domain.state.map.tile import Tile


class TileMarketState:

    def __init__(self, tiles: list[Tile], quantities: list[int]):
        self.tiles = tiles
        self.tile_rotations = [tile.get_unique_rotations() for tile in self.tiles]
        self.quantities = quantities

    def available_tiles(self, ft: FutureTile) -> list[Tile]:
        result = []
        for i in range(len(self.tiles)):
            for tile in self.tile_rotations[i]:
                if ft.matches(tile):
                    t = tile.clone()
                    t.x = ft.tile.x
                    t.y = ft.tile.y
                    result.append(t)
        return result
