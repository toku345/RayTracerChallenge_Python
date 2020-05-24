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
