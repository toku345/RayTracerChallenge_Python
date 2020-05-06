from raytracerchallenge_python.plane import Plane
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.ray import Ray


def test_the_normal_of_a_plane_is_constant_everywhere():
    # Given
    p = Plane()
    # When
    n1 = p.local_normal_at(Point(0, 0, 0))
    n2 = p.local_normal_at(Point(10, 0, -10))
    n3 = p.local_normal_at(Point(-5, 0, 150))
    # Then
    assert n1 == Vector(0, 1, 0)
    assert n2 == Vector(0, 1, 0)
    assert n3 == Vector(0, 1, 0)


def test_intersect_with_a_ray_parallel_to_the_plane():
    # Given
    p = Plane()
    r = Ray(Point(0, 10, 0), Vector(0, 0, 1))
    # When
    xs = p.local_intersect(r)
    # Then
    assert len(xs) == 0


def test_intersect_with_a_coplanar_ray():
    # Given
    p = Plane()
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    # When
    xs = p.local_intersect(r)
    # Then
    assert len(xs) == 0


def test_a_ray_intersecting_a_plane_from_above():
    # Given
    p = Plane()
    r = Ray(Point(0, 1, 0), Vector(0, -1, 0))
    # When
    xs = p.local_intersect(r)
    # Then
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].object == p


def test_a_ray_intersecting_a_plane_from_below():
    # Given
    p = Plane()
    r = Ray(Point(0, -1, 0), Vector(0, 1, 0))
    # When
    xs = p.local_intersect(r)
    # Then
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].object == p
