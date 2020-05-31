from raytracerchallenge_python.group import Group
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector


def test_creating_a_new_group():
    # Given
    g = Group()
    # Then
    assert g.transform == identity_matrix()
    assert len(g) == 0


class MockShape(Shape):
    def local_intersect(self, ray):
        pass

    def local_normal_at(self, p):
        pass


def test_adding_a_child_to_a_group():
    # Given
    g = Group()
    s = MockShape()
    # When
    g.add_child(s)
    # Then
    assert len(g) > 0
    assert s in g
    assert s.parent == g


def test_intersectinga_ray_with_an_empty_group():
    # Given
    g = Group()
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    # When
    xs = g.local_intersect(r)
    # Then
    assert len(xs) == 0
