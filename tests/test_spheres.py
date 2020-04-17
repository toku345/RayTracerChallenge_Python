from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector


def test_a_ray_intersects_a_sphere_at_two_points():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0] == 4.0
    assert xs[1] == 6.0


def test_a_ray_intersects_a_sphere_at_a_tangent():
    # Then
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0] == 5.0
    assert xs[1] == 5.0


def test_a_ray_misses_s_sphere():
    # Given
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 0


def test_a_ray_originates_inside_a_sphere():
    # Given
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0] == -1.0
    assert xs[1] == 1.0


def test_a_sphere_is_behind_a_ray():
    # Given
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0] == -6.0
    assert xs[1] == -4.0
