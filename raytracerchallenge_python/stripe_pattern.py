from raytracerchallenge_python.pattern import Pattern

from math import floor


class StripePattern(Pattern):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b
