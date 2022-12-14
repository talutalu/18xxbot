from __future__ import annotations

from domain.state.map.coordinate import Coordinate

"""
This class represents a hex tile.

Here are the hex indices used to refer to one side of the hex:
              0
            _____
      5    /     \   1
          /       \
         (    6    )
      4   \       /  2
           \_____/
              3

The hex can be rotated on the map.
"""
from domain.state.map.city import City


class Tile:

    def __init__(self, id, connections, level, cities: list[City], c: Coordinate=None, revenue=None):
        self.id = id
        self.connections: list[tuple[int, ...]] = connections
        # empty is 0, yellow is 1, green is 2, brown is 3 and grey is 4
        self.level = level
        # 0: no city, 1: town, 2: simple city, 3: y city, etc.
        self.cities = cities

        self.c = c

        self.revenue = revenue

        self.rotation = 0

    def __str__(self):
        return f"Tile(c={self.c}, connections={str(self.connections)})"

    def clone(self):
        return Tile(id=self.id,
                    connections=[c for c in self.connections],
                    level=self.level,
                    # TODO deep clone this?
                    cities=self.cities,
                    c=self.c,
                    revenue=self.revenue)

    def get_unique_rotations(self):
        unique_rotations = [self.clone()]
        for inc in (1, 2, 3, 4, 5):
            candidate = sorted([tuple(sorted([(e + inc) % 6 for e in c])) for c in self.connections])
            if candidate not in [t.connections for t in unique_rotations]:
                tile = self.clone()
                tile.connections = candidate
                tile.rotation = inc
                unique_rotations.append(tile)
        return unique_rotations

    def get_connected_edges(self):
        return set([e for c in self.connections for e in c])

    def contains_city(self):
        return len(self.cities) > 0

    def is_empty(self):
        return self.level == 0

    def num_cities(self):
        return len(self.cities)