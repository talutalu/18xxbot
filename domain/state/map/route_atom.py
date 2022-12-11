from domain.state.map.tile import Tile


class RouteAtom:

    def __init__(self, tile: Tile, a_face: int, b_face: int):
        self.tile = tile
        self.a_face = a_face
        self.b_face = b_face
