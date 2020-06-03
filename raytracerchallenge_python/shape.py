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

    def normal_at(self, point):
        local_point = self.transform.inverse() * point
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return world_normal.normalize()

    @abstractmethod
    def local_normal_at(self, point):
        """ abstruct method !!! """

    def world_to_object(self, point):
        if self.parent:
            point = self.parent.world_to_object(point)
        return self.transform.inverse() * point
