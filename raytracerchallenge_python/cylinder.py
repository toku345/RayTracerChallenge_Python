from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.intersection import Intersection

from raytracerchallenge_python.helpers import EPSILON


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

        return (Intersection(1, self),)

    def local_normal_at(self, point):
        """ not implemented """
