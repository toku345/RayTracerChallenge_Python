from raytracerchallenge_python.group import Group
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.transformations import translation


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


def test_intersecting_a_ray_with_a_nonempty_group():
    # Given
    g = Group()
    s1 = Sphere()
    s2 = Sphere()
    s2.transform = translation(0, 0, -3)
    s3 = Sphere()
    s3.transform = translation(5, 0, 0)
    g.add_child(s1)
    g.add_child(s2)
    g.add_child(s3)
    # When
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = g.local_intersect(r)
    # Then
    assert len(xs) == 4
    assert xs[0].object == s2
    assert xs[1].object == s2
    assert xs[2].object == s1
    assert xs[3].object == s1
