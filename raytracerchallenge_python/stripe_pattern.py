from math import floor


class StripePattern:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def stripe_at(self, point):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b
