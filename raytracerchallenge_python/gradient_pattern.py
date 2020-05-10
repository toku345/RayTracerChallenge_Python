from raytracerchallenge_python.pattern import Pattern

from math import floor


class GradientPattern(Pattern):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point):
        distance = self.b - self.a
        fraction = point.x - floor(point.x)
        return self.a + distance * fraction
