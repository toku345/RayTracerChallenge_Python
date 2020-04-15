from math import sqrt
from decimal import Decimal

from raytracerchallenge_python.helpers import equal


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

    def to_list(self):
        return [self.x, self.y, self.z, self.w]

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, Tuple):
            return False

        return all([equal(self.x, other.x),
                    equal(self.y, other.y),
                    equal(self.z, other.z),
                    equal(self.w, other.w)])

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
        super().__init__(red, green, blue, 0)

    def ppm_pixel_str(self, maximum_color_value):
        def convert(value):
            if value < 0:
                value = 0
            elif value > 1:
                value = 1
            ppm_value = value * maximum_color_value
            return Decimal(ppm_value).quantize(Decimal('1.'))

        r = convert(self.red)
        g = convert(self.green)
        b = convert(self.blue)
        return f"{r} {g} {b}"

    def __mul__(self, scalar_or_color):
        if type(scalar_or_color) == Color:
            return self._hadamard_product(scalar_or_color)
        else:
            return super().__mul__(scalar_or_color)

    def _hadamard_product(self, other):
        r = self.red * other.red
        g = self.green * other.green
        b = self.blue * other.blue
        return Color(r, g, b)
