class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return self.w == 1.0

    def is_vector(self):
        return not self.is_point()

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, Tuple):
            return False

        return (
            self.x == other.x
            and self.y == other.y
            and self.z == other.z
            and self.w == other.w
        )


def point(x, y, z):
    return Tuple(x, y, z, 1.0)


def vector(x, y, z):
    return Tuple(x, y, z, 0.0)
