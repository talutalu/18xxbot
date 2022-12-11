from __future__ import annotations

from domain.state.company_state import CompanyState
from typing import TYPE_CHECKING

from domain.state.map.city import City
from domain.state.map.future_tile import FutureTile
from domain.state.map.tile import Tile


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
        self.tiles = [[Tile(None, [], 0, [], x, y, None) for x in range(width)]
                      for y in range(height)]
        self.future_tiles_from_city: list[FutureTile] = []

        self.cities = []

    def neighbor(self, x: int, y: int, face: int):
        h = self.height - 1
        if face == 0:
            return None if y == 0 or (y == 1 and x % 2 == 0) else self.tiles[y - 1][x]
        elif face == 1:
            return None if y == 0 or (y == 1 and (x + 1) % 2 == 0) else self.tiles[y - 1][x + 1]
        elif face == 2:
            return None if y == h or (y == h - 1 and (x + 1) % 2 == 0) else self.tiles[y + 1][x + 1]
        elif face == 3:
            return None if y == h or (y == h - 1 and x % 2 == 0) else self.tiles[y + 1][x]
        elif face == 4:
            return None if y == h or (y == h - 1 and (x - 1) % 2 == 0) else self.tiles[y + 1][x - 1]
        elif face == 5:
            return None if y == 0 or (y == 1 and (x - 1) % 2 == 0) else self.tiles[y - 1][x - 1]

    def neighbors(self, x: int, y: int):
        return [self.neighbor(x, y, face) for face in range(6)]

    def legal_new_tiles(self, company_state: CompanyState):
        (x, y, c) = company_state.token_location
        city = self.tiles[y][x].cities[c]
        return city.legal_new_tiles(self)

    def put_tile(self, tile: Tile):
        old_tile = self.tiles[tile.y][tile.x]
        self.tiles[tile.y][tile.x] = tile

        # add city and upgrade route extensions
        if not old_tile.contains_city() and tile.contains_city():
            for city in tile.cities:
                city.refresh_route_extensions(self)
                self.cities.append(city)

        # check touched roads
        faces = [[] for _ in range(6)]
        for city in self.cities:
            coord = (tile.x, tile.y)
            if coord not in city.route_extensions:
                continue
            routes = city.route_extensions[coord]
            for route in routes:
                faces[route.ending_face].append(route)



        # remove tile from market

    def upgrade_tile(self, x: int, y: int, tile: Tile):
        pass

    @staticmethod
    def generate_test_for_2p(x: int, y: int):
        ms = MapState(x, y)
        xo = x // 2
        yo = 0 if xo % 2 == 0 else 1
        xd = xo
        yd = y - 1 if xo % 2 == 1 else y - 2

        a = Tile(connections=[(2, 2), (4, 4)],
                 level=2,
                 cities=[],
                 x=xo,
                 y=yo,
                 revenue=40,
                 id=-1)
        a.cities = [City(a, 0), City(a, 1)]
        ms.put_tile(a)

        b = Tile(connections=[(0, 0)],
                 level=2,
                 cities=[],
                 x=xd,
                 y=yd,
                 revenue=30,
                 id=-2)
        b.cities = [City(b, 0)]
        ms.put_tile(b)

        return ms
