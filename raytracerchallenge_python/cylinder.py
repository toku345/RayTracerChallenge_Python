from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.intersection import Intersection, Intersections
from raytracerchallenge_python.tuple import Vector

from raytracerchallenge_python.helpers import EPSILON

from math import sqrt


class Cylinder(Shape):
    def local_intersect(self, ray):
        a = ray.direction.x ** 2 + ray.direction.z ** 2

        # ray is parallel to the y axis
        if abs(a) < EPSILON:
            return ()

        b = 2 * ray.origin.x * ray.direction.x + \
            2 * ray.origin.z * ray.direction.z
        c = ray.origin.x ** 2 + ray.origin.z ** 2 - 1
        disc = b ** 2 - 4 * a * c

        # ray does not intersect the cylinder
        if disc < 0:
            return ()

        t0 = (-b - sqrt(disc)) / (2 * a)
        t1 = (-b + sqrt(disc)) / (2 * a)

        return Intersections(Intersection(t0, self), Intersection(t1, self))

    def local_normal_at(self, point):
        return Vector(point.x, 0, point.z)
