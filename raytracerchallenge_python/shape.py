from abc import ABCMeta, abstractmethod

from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.material import Material


class Shape(metaclass=ABCMeta):
    def __init__(self):
        self.transform = identity_matrix()
        self.material = Material()
        self.parent = None

    def intersect(self, ray):
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    @abstractmethod
    def local_intersect(self, ray):
        """ abstruct method !!! """

    def normal_at(self, world_point):
        local_point = self.world_to_object(world_point)
        local_normal = self.local_normal_at(local_point)
        return self.normal_to_world(local_normal)

    @abstractmethod
    def local_normal_at(self, point):
        """ abstruct method !!! """

    def world_to_object(self, point):
        if self.parent:
            point = self.parent.world_to_object(point)
        return self.transform.inverse() * point

    def normal_to_world(self, normal):
        normal = self.transform.inverse().transpose() * normal
        normal.w = 0
        normal = normal.normalize()

        if self.parent:
            normal = self.parent.normal_to_world(normal)

        return normal
