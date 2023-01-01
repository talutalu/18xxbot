

class Coordinate:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def neighbor(c, face: int):
        x = c.x
        y = c.y
        # TODO
        h = 1000
        if face == 0:
            return None if y == 0 or (y == 1 and x % 2 == 0) else Coordinate(x, y - 1)
        elif face == 1:
            return None if y == 0 or (y == 1 and (x + 1) % 2 == 0) else Coordinate(x + 1, y - 1)
        elif face == 2:
            return None if y == h or (y == h - 1 and (x + 1) % 2 == 0) else Coordinate(x + 1, y + 1)
        elif face == 3:
            return None if y == h or (y == h - 1 and x % 2 == 0) else Coordinate(x, y + 1)
        elif face == 4:
            return None if y == h or (y == h - 1 and (x - 1) % 2 == 0) else Coordinate(x - 1, y + 1)
        elif face == 5:
            return None if y == 0 or (y == 1 and (x - 1) % 2 == 0) else Coordinate(x - 1, y - 1)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
