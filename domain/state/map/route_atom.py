from __future__ import annotations

from domain.state.map.coordinate import Coordinate


class RouteAtom:

    def __init__(self, c: Coordinate, a_face: int | None, b_face: int | None):
        self.c = c
        self.a_face = a_face
        self.b_face = b_face

    def __repr__(self):
        return f"RouteAtom(c={self.c}, a={self.a_face}, b={self.b_face})"
