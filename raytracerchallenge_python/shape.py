from abc import ABCMeta, abstractmethod

from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.material import Material


class Shape(metaclass=ABCMeta):
    def __init__(self):
        self.transform = identity_matrix()
        self.material = Material()

    def intersect(self, ray):
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    @abstractmethod
    def local_intersect(self, ray):
        """ abstruct method !!! """
