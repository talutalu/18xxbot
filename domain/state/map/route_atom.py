from domain.state.map.coordinate import Coordinate


class RouteAtom:

    def __init__(self, c: Coordinate, a_face: int, b_face: int):
        self.c = c
        self.a_face = a_face
        self.b_face = b_face
