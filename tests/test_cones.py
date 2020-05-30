from raytracerchallenge_python.cone import Cone
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.ray import Ray

from raytracerchallenge_python.helpers import equal

from math import sqrt


def test_intersecting_a_cone_with_a_ray():
    EXAMPLES = [
        # origin          direction            t0       t1
        (Point(0, 0, -5), Vector(0, 0, 1),     5,        5),
        (Point(0, 0, -5), Vector(1, 1, 1),     8.66025,  8.66025),
        (Point(1, 1, -5), Vector(-0.5, -1, 1), 4.55006, 49.44994),
    ]
    for origin, direction, t0, t1 in EXAMPLES:
        # Given
        shape = Cone()
        dir = direction.normalize()
        r = Ray(origin, dir)
        # When
        xs = shape.local_intersect(r)
        # Then
        assert len(xs) == 2
        assert equal(xs[0].t, t0)
        assert equal(xs[1].t, t1)


def test_intersecting_a_cone_with_a_ray_parallel_to_one_of_its_halves():
    # Given
    shape = Cone()
    direction = Vector(0, 1, 1).normalize()
    r = Ray(Point(0, 0, -1), direction)
    # When
    xs = shape.local_intersect(r)
    # Then
    assert len(xs) == 1
    assert equal(xs[0].t, 0.35355)


def test_a_ray_misses_a_cone():
    # Given
    shape = Cone()
    direction = Vector(1, 1, 0).normalize()
    r = Ray(Point(1, 1, 0), direction)
    # When
    xs = shape.local_intersect(r)
    # Then
    assert len(xs) == 0


def test_the_default_minimum_and_maximum_for_a_cone():
    # Given
    shape = Cone()
    # Then
    assert shape.minimum == -float('inf')
    assert shape.maximum == float('inf')


def test_the_default_closed_value_for_a_cone():
    # Given
    shape = Cone()
    # Then
    assert shape.closed is False


def test_intersecting_a_cone_end_caps():
    EXAMPLES = [
        # origin             direction        count
        (Point(0, 0, -5),    Vector(0, 1, 0), 0),
        (Point(0, 0, -0.25), Vector(0, 1, 1), 2),
        (Point(0, 0, -0.25), Vector(0, 1, 0), 4),
    ]
    for origin, direction, count in EXAMPLES:
        # Given
        shape = Cone()
        shape.minimum = -0.5
        shape.maximum = 0.5
        shape.closed = True
        dir = direction.normalize()
        r = Ray(origin, dir)
        # When
        xs = shape.local_intersect(r)
        # Then
        assert len(xs) == count


def test_computing_the_normal_vector_on_a_cone():
    EXAMPLES = [
        # point            normal
        (Point(0, 0, 0),   Vector(0, 0, 0)),
        (Point(1, 1, 1),   Vector(1, -sqrt(2), 1)),
        (Point(-1, -1, 0), Vector(-1, 1, 0)),
    ]
    for point, normal in EXAMPLES:
        # Given
        shape = Cone()
        # When
        n = shape.local_normal_at(point)
        # Then
        assert n == normal


def test_the_normal_vector_on_a_cones_end_caps():
    EXAMPLES = [
        # point              normal
        (Point(0, 1, 0),     Vector(0, 1, 0)),
        (Point(0.5, 1, 0),   Vector(0, 1, 0)),
        (Point(0, 1, 0.5),   Vector(0, 1, 0)),
        (Point(0, -1, 0),    Vector(0, -1, 0)),
        (Point(-0.5, -1, 0), Vector(0, -1, 0)),
        (Point(0, -1, 0.5),  Vector(0, -1, 0)),
    ]
    for point, normal in EXAMPLES:
        # Given
        shape = Cone()
        shape.minimum = -1
        shape.maximum = 1
        shape.closed = True
        # When
        n = shape.local_normal_at(point)
        # Then
        assert n == normal
