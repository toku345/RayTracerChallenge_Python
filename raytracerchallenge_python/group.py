from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.intersection import Intersections


class Group(Shape):
    def __init__(self):
        self.transform = identity_matrix()
        self.children = []

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def add_child(self, shape):
        self.children.append(shape)
        shape.parent = self

    def local_intersect(self, ray):
        # if len(self.children) == 0:
        return Intersections()

    def local_normal_at(self, point):
        """ not implemented """
