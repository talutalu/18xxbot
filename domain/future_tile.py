

class FutureTile:

    def __init__(self, x: int, y: int, constraints, level, city_level):
        self.x = x
        self.y = y
        self.constraints = constraints
        # empty is 0, yellow is 1, green is 2, brown is 3 and grey is 4
        self.level = level
        # 0: no city, 1: town, 2: simple city, 3: y city, 4: special city M, etc.
        self.city_level = city_level
