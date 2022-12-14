from __future__ import annotations

from domain.state.company_state import CompanyState
from typing import TYPE_CHECKING

from domain.state.map.city import City
from domain.state.map.coordinate import Coordinate
from domain.state.map.future_tile import FutureTile
from domain.state.map.tile import Tile


class MapState:

    def __init__(self, width: int, height: int, for_clone=False):
        """
        The map always starts with a 'higher' hex tile on the first column.

        :param width:
        :param height:
        """
        self.width = width
        self.height = height
        if for_clone:
            self.tiles = None
            self.cities = None
        else:
            # TODO don't instantiate too many tiles, the x component only has a tile every other index
            self.tiles = [[Tile(None, [], 0, [], Coordinate(x, y), None) for x in range(width)]
                          for y in range(height)]
            self.cities: list[City] = []

    def clone(self):
        copy = MapState(self.width, self.height, for_clone=True)
        copy.tiles = [a[:] for a in self.tiles]
        copy.cities = [c.clone() for c in self.cities]
        return copy

    def get_tile(self, c: Coordinate):
        return self.tiles[c.y][c.x]

    def legal_new_tiles(self, company_state: CompanyState):
        (x, y, c) = company_state.token_location
        city = self.tiles[y][x].cities[c]
        return city.legal_new_tiles(self)

    def put_tile(self, tile: Tile):
        old_tile = self.tiles[tile.c.y][tile.c.x]
        assert (not old_tile.contains_city() and tile.contains_city()) or old_tile.level + 1 == tile.level
        self.tiles[tile.c.y][tile.c.x] = tile

        # add city if we just added one
        if not old_tile.contains_city() and tile.contains_city():
            for city in tile.cities:
                self.cities.append(city)

        # check touched roads
        affected_roads = []
        for city in self.cities:
            for route in city.update_routes(tile):
                affected_roads.append(route)

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
                 c=Coordinate(xo, yo),
                 revenue=40,
                 id=-1)
        a.cities = [City(a, 0), City(a, 1)]
        ms.put_tile(a)

        b = Tile(connections=[(0, 0)],
                 level=2,
                 cities=[],
                 c=Coordinate(xd, yd),
                 revenue=30,
                 id=-2)
        b.cities = [City(b, 0)]
        ms.put_tile(b)

        return ms
