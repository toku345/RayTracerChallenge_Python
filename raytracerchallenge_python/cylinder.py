from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.intersection import Intersection, Intersections
from raytracerchallenge_python.tuple import Vector

from raytracerchallenge_python.helpers import EPSILON

from math import sqrt


class Cylinder(Shape):
    def __init__(self):
        super().__init__()
        self.minimum = -float('inf')
        self.maximum = float('inf')
        self.closed = False

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
            return Intersections()

        t0 = (-b - sqrt(disc)) / (2 * a)
        t1 = (-b + sqrt(disc)) / (2 * a)

        # if t0 > t1:
        #     t0, t1 = t1, t0

        xs = []

        y0 = ray.origin.y + t0 * ray.direction.y
        if self.minimum < y0 and y0 < self.maximum:
            xs.append(Intersection(t0, self))

        y1 = ray.origin.y + t1 * ray.direction.y
        if self.minimum < y1 and y1 < self.maximum:
            xs.append(Intersection(t1, self))

        return Intersections(*xs)

    def local_normal_at(self, point):
        return Vector(point.x, 0, point.z)
