from domain.future_tile import FutureTile
from domain.tile import Tile


class MapState:

    def __init__(self, width: int, height: int):
        """
        The map always starts with a 'higher' hex tile on the first column.

        :param width:
        :param height:
        """
        self.width = width
        self.height = height
        # TODO don't instantiate too many tiles, the x component only has a tile every other index
        self.tiles = [[Tile([], 0, 0, [], None) for x in range(width)]
                      for y in range(height)]

        self.cities = []
        self.future_tiles_from_city: list[FutureTile] = []

    def neighbors(self, x: int, y: int):
        h = self.height - 1
        tile_0 = None if y == 0 or (y == 1 and x % 2 == 0) else self.tiles[y - 1][x]
        tile_1 = None if y == 0 or (y == 1 and (x + 1) % 2 == 0) else self.tiles[y - 1][x + 1]
        tile_2 = None if y == h or (y == h - 1 and (x + 1) % 2 == 0) else self.tiles[y + 1][x + 1]
        tile_3 = None if y == h or (y == h - 1 and x % 2 == 0) else self.tiles[y + 1][x]
        tile_4 = None if y == h or (y == h - 1 and (x - 1) % 2 == 0) else self.tiles[y + 1][x - 1]
        tile_5 = None if y == 0 or (y == 1 and (x - 1) % 2 == 0) else self.tiles[y - 1][x - 1]
        return [tile_0, tile_1, tile_2, tile_3, tile_4, tile_5]

    def put_tile(self, x: int, y: int, tile: Tile):
        self.tiles[y][x] = tile

        if tile.contains_city():
            # TODO this implementation is not enough
            # update future tiles

            self.cities.extend([(x, y, c) for c in tile.num_cities()])
        pass

    def upgrade_tile(self, x: int, y: int, tile: Tile):
        pass

    @staticmethod
    def generate_test_for_2p(x: int, y: int):
        ms = MapState(x, y)
        xo = x // 2
        yo = 0 if xo % 2 == 0 else 1
        xd = xo
        yd = y - 1 if xo % 2 == 1 else y - 2

        to = ms.tiles[yo][xo]
        td = ms.tiles[yd][xd]

        to.connections = [(2, 2), (4, 4)]
        to.level = 2
        to.city_level = 3
        to.city_connections = [0, 1]
        to.revenue = 40

        td.connections = [(0, 0)]
        td.level = 2
        to.city_level = 2
        to.city_connections = [0]
        to.revenue = 30

        return ms
