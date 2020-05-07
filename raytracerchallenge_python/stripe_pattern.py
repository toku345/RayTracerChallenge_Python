from raytracerchallenge_python.matrix import identity_matrix

from math import floor


class StripePattern:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.transform = identity_matrix()

    def stripe_at(self, point):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b

    def stripe_at_object(self, object, world_point):
        object_point = object.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point

        return self.stripe_at(pattern_point)
