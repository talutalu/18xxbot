
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
class Tile:

    def __init__(self, connections, level, city_level, city_connections, revenue=None):
        self.connections = connections
        # empty is 0, yellow is 1, green is 2, brown is 3 and grey is 4
        self.level = level
        # 0: no city, 1: town, 2: simple city, 3: y city, etc.
        self.city_level = city_level
        # if there is more than one city, this is an array
        self.city_connections = city_connections
        self.revenue = revenue

    def __str__(self):
        return "Tile(" + str(self.connections) + ")"

    def clone(self):
        return Tile(connections=[c for c in self.connections],
                    level=self.level,
                    city_level=self.city_level,
                    city_connections=self.city_connections,
                    revenue=self.revenue)

    def get_unique_rotations(self):
        unique_rotations = [self.clone()]
        for inc in (1, 2, 3, 4, 5):
            candidate = sorted([tuple(sorted([(e + inc) % 6 for e in c])) for c in self.connections])
            if candidate not in [t.connections for t in unique_rotations]:
                tile = self.clone()
                tile.connections = candidate
                unique_rotations.append(tile)
        return unique_rotations

    def get_connected_edges(self):


    def contains_city(self):
        return self.city_level > 0

    def is_empty(self):
        return self.level == 0

    def num_cities(self):
        return len(self.city_connections)