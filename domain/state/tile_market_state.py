from domain.state.map.future_tile import FutureTile
from domain.state.map.tile import Tile


class TileMarketState:

    def __init__(self, tiles: list[Tile], quantities: list[int], tile_rotations=None):
        self.tiles = tiles
        if tile_rotations:
            self.tile_rotations = tile_rotations
        else:
            self.tile_rotations = [tile.get_unique_rotations() for tile in self.tiles]
        self.quantities = quantities

    def clone(self):
        return TileMarketState(tiles=self.tiles, quantities=self.quantities[:], tile_rotations=self.tile_rotations)

    def available_tiles(self, ft: FutureTile) -> list[Tile]:
        """
        :param ft:
        :return: the available tiles matching the provided ft constraint
        """
        result = []
        for i in range(len(self.tiles)):
            for tile in self.tile_rotations[i]:
                if ft.matches(tile):
                    t = tile.clone()
                    t.c = ft.tile.c
                    result.append(t)
        return result
