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
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0


def test_a_ray_intersects_a_sphere_at_a_tangent():
    # Then
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == 5.0
    assert xs[1].t == 5.0


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
    assert xs[0].t == -1.0
    assert xs[1].t == 1.0


def test_a_sphere_is_behind_a_ray():
    # Given
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == -6.0
    assert xs[1].t == -4.0


def test_intersect_sets_the_object_on_the_intersection():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].object == s
    assert xs[1].object == s
