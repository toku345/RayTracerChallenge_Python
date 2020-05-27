from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.intersection import Intersections, Intersection

from raytracerchallenge_python.helpers import EPSILON

from math import sqrt


class Cone(Shape):
    def local_intersect(self, ray):
        a = ray.direction.x ** 2 - ray.direction.y ** 2 + ray.direction.z ** 2
        b = 2 * ray.origin.x * ray.direction.x \
            - 2 * ray.origin.y * ray.direction.y \
            + 2 * ray.origin.z * ray.direction.z
        c = ray.origin.x ** 2 - ray.origin.y ** 2 + ray.origin.z ** 2

        if abs(a) < EPSILON:
            if abs(b) < EPSILON:
                return Intersections()
            else:
                return Intersections(Intersection(-c / (2 * b), self))

        disc = b ** 2 - 4 * a * c
        t0 = (-b - sqrt(disc)) / (2 * a)
        t1 = (-b + sqrt(disc)) / (2 * a)

        return Intersections(Intersection(t0, self), Intersection(t1, self))

    def local_normal_at(self, point):
        """ not implemented """
