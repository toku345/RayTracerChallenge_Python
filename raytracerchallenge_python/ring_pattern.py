from raytracerchallenge_python.pattern import Pattern

from math import floor, sqrt


class RingPattern(Pattern):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point):
        if floor(sqrt(point.x ** 2 + point.z ** 2)) % 2 == 0:
            return self.a
        else:
            return self.b
