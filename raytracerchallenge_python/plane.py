from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.tuple import Vector
from raytracerchallenge_python.intersection import Intersection

from raytracerchallenge_python.helpers import EPSILON


class Plane(Shape):
    def local_intersect(self, ray):
        if abs(ray.direction.y) < EPSILON:
            return []

        t = -ray.origin.y / ray.direction.y
        return [Intersection(t, self)]

    def local_normal_at(self, point):
        return Vector(0, 1, 0)
