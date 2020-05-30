from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.intersection import Intersections, Intersection
from raytracerchallenge_python.tuple import Vector

from raytracerchallenge_python.helpers import EPSILON

from math import sqrt


class Cone(Shape):
    def __init__(self):
        super().__init__()
        self.minimum = -float('inf')
        self.maximum = float('inf')
        self.closed = False

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
                xs = [Intersection(-c / (2 * b), self)] + \
                    self._intersect_caps(ray)
                return Intersections(*xs)

        disc = b ** 2 - 4 * a * c
        t0 = (-b - sqrt(disc)) / (2 * a)
        t1 = (-b + sqrt(disc)) / (2 * a)

        xs = []

        y0 = ray.origin.y + t0 * ray.direction.y
        if self.minimum < y0 and y0 < self.maximum:
            xs.append(Intersection(t0, self))

        y1 = ray.origin.y + t1 * ray.direction.y
        if self.minimum < y1 and y1 < self.maximum:
            xs.append(Intersection(t1, self))

        xs = xs + self._intersect_caps(ray)

        return Intersections(*xs)

    def _intersect_caps(self, ray):
        def check_cap(ray, t):
            x = ray.origin.x + t * ray.direction.x
            y = ray.origin.y + t * ray.direction.y
            z = ray.origin.z + t * ray.direction.z
            return (x ** 2 + z ** 2) <= y ** 2

        xs = []
        if self.closed is False or abs(ray.direction.y) < EPSILON:
            return xs

        t = (self.minimum - ray.origin.y) / ray.direction.y
        if check_cap(ray, t):
            xs.append(Intersection(t, self))

        t = (self.maximum - ray.origin.y) / ray.direction.y
        if check_cap(ray, t):
            xs.append(Intersection(t, self))

        return xs

    def local_normal_at(self, point):
        dist = point.x ** 2 + point.z ** 2

        if dist < abs(point.y) and point.y >= self.maximum - EPSILON:
            return Vector(0, 1, 0)
        elif dist < abs(point.y) and point.y <= self.minimum + EPSILON:
            return Vector(0, -1, 0)

        y = sqrt(point.x ** 2 + point.z ** 2)
        if point.y > 0:
            y = -y
        return Vector(point.x, y, point.z)
