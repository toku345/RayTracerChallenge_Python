from raytracerchallenge_python.cylinder import Cylinder
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.ray import Ray

from raytracerchallenge_python.helpers import equal


def test_a_ray_misses_a_cylinder():
    EXAMPLES = [
        # origin          direction
        (Point(1, 0, 0),  Vector(0, 1, 0)),
        (Point(0, 0, 0),  Vector(0, 1, 0)),
        (Point(0, 0, -5), Vector(1, 1, 1)),
    ]
    for origin, direction in EXAMPLES:
        # Given
        cyl = Cylinder()
        dir = direction.normalize()
        r = Ray(origin, dir)
        # When
        xs = cyl.local_intersect(r)
        # Then
        assert len(xs) == 0


def test_a_ray_strikes_a_cylinder():
    EXAMPLES = [
        # origin            direction          t0       t1
        (Point(1, 0, -5),   Vector(0, 0, 1),   5,       5),
        (Point(0, 0, -5),   Vector(0, 0, 1),   4,       6),
        (Point(0.5, 0, -5), Vector(0.1, 1, 1), 6.80798, 7.08872),
    ]
    for origin, direction, t0, t1 in EXAMPLES:
        # Given
        cyl = Cylinder()
        dir = direction.normalize()
        r = Ray(origin, dir)
        # When
        xs = cyl.local_intersect(r)
        # Then
        assert len(xs) == 2
        assert equal(xs[0].t, t0)
        assert equal(xs[1].t, t1)


def test_normal_vector_on_a_cylinder():
    EXAMPLES = [
        # point           normal
        (Point(1, 0, 0),  Vector(1, 0, 0)),
        (Point(0, 5, -1), Vector(0, 0, -1)),
        (Point(0, -2, 1), Vector(0, 0, 1)),
        (Point(-1, 1, 0), Vector(-1, 0, 0)),
    ]
    for point, normal in EXAMPLES:
        # Given
        cyl = Cylinder()
        # When
        n = cyl.local_normal_at(point)
        # Then
        assert n == normal


def test_the_default_minimum_and_maximum_for_a_cylinder():
    # Given
    cyl = Cylinder()
    # Then
    assert cyl.minimum == -float('inf')
    assert cyl.maximum == float('inf')


def test_intersecting_a_constrained_cylinder():
    EXAMPLES = [
        # point             direction          count
        (Point(0, 1.5, 0),  Vector(0.1, 1, 0), 0),
        (Point(0, 3, -5),   Vector(0, 0, 1),   0),
        (Point(0, 0, -5),   Vector(0, 0, 1),   0),
        (Point(0, 2, -5),   Vector(0, 0, 1),   0),
        (Point(0, 1, -5),   Vector(0, 0, 1),   0),
        (Point(0, 1.5, -2), Vector(0, 0, 1),   2),
        (Point(0, 1.5, 2),  Vector(0, 0, -1),  2),
    ]
    for point, direction, count in EXAMPLES:
        # Given
        cyl = Cylinder()
        cyl.minimum = 1
        cyl.maximum = 2
        dir = direction.normalize()
        r = Ray(point, dir)
        # When
        xs = cyl.local_intersect(r)
        # Then
        assert len(xs) == count
