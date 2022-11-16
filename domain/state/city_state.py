from domain.future_tile import FutureTile
from domain.state.map_state import MapState
from domain.tile import Tile


class CityState:

    def __init__(self, ms: MapState, tile: Tile, x: int, y: int, city: int):
        self.ms = ms
        self.tile = tile
        self.x = x
        self.y = y
        self.city = city
        self.future_tiles: list[FutureTile] = []
        self.init_future_tiles()

    def init_future_tiles(self):
        for n in self.ms.neighbors(self.x, self.y):
            if not n.is_empty():
                continue


