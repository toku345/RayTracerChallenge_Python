from math import sqrt


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

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        return Tuple(self.x / magnitude,
                     self.y / magnitude,
                     self.z / magnitude,
                     self.w / magnitude)

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

    def __add__(self, other):
        return Tuple(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z,
                     self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z,
                     self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar):
        return Tuple(self.x * scalar,
                     self.y * scalar,
                     self.z * scalar,
                     self.w * scalar)

    def __truediv__(self, scalar):
        return Tuple(self.x / scalar,
                     self.y / scalar,
                     self.z / scalar,
                     self.w / scalar)


class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1.0)


class Vector(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0.0)

    def dot(self, other):
        return sum([self.x * other.x,
                    self.y * other.y,
                    self.z * other.z,
                    self.w * other.w])

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)


class Color(Tuple):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        super().__init__(red, green, blue, None)
