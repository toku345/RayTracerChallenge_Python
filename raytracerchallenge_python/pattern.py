from abc import ABCMeta, abstractmethod

from raytracerchallenge_python.matrix import identity_matrix


class Pattern(metaclass=ABCMeta):
    def __init__(self):
        self.transform = identity_matrix()

    def pattern_at_shape(self, shape, world_point):
        shape_point = shape.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * shape_point

        return self.pattern_at(pattern_point)

    @abstractmethod
    def pattern_at(self, point):
        """ abstrac tmethod !!! """
