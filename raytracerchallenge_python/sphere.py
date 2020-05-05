from raytracerchallenge_python.tuple import Point
from raytracerchallenge_python.intersection import (
    Intersection, Intersections)
from raytracerchallenge_python.shape import Shape

from math import sqrt


class Sphere(Shape):
    def __eq__(self, other):
        return all([self.transform == other.transform,
                    self.material == other.material])

    def local_intersect(self, ray):
        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is centered at the world origin
        sphere_to_ray = ray.origin - Point(0, 0, 0)

        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return ()

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)
        return Intersections(Intersection(t1, self), Intersection(t2, self))

    def normal_at(self, world_point):
        object_point = self.transform.inverse() * world_point
        object_normal = object_point - Point(0, 0, 0)
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return world_normal.normalize()
