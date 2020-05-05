from abc import ABCMeta

from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.material import Material


class Shape(metaclass=ABCMeta):
    def __init__(self):
        self.transform = identity_matrix()
        self.material = Material()
