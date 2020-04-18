from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.transformations import translation, scaling
from raytracerchallenge_python.tuple import Point, Vector


def test_creating_and_querying_a_ray():
    # Given
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)
    # When
    r = Ray(origin, direction)
    # Then
    assert r.origin == origin
    assert r.direction == direction


def test_computing_a_point_from_a_distance():
    # Given
    r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
    # Then
    assert r.position(0) == Point(2, 3, 4)
    assert r.position(1) == Point(3, 3, 4)
    assert r.position(-1) == Point(1, 3, 4)
    assert r.position(2.5) == Point(4.5, 3, 4)


def test_translating_a_ray():
    # Given
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    m = translation(3, 4, 5)
    # When
    r2 = r.transform(m)
    # Then
    assert r2.origin == Point(4, 6, 8)
    assert r2.direction == Vector(0, 1, 0)


def test_scaling_a_ray():
    # Given
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    m = scaling(2, 3, 4)
    # When
    r2 = r.transform(m)
    # Then
    assert r2.origin == Point(2, 6, 12)
    assert r2.direction == Vector(0, 3, 0)
