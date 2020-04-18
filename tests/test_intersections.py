from raytracerchallenge_python.intersection import Intersection, Intersections
from raytracerchallenge_python.sphere import Sphere


def test_an_intersection_encapsulates_t_and_object():
    # Given
    s = Sphere()
    # When
    i = Intersection(3.5, s)
    # Then
    assert i.t == 3.5
    assert i.object == s


def test_aggregating_intersections():
    # Given
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    # When
    xs = Intersections(i1, i2)
    # Then
    assert len(xs) == 2
    assert xs[0].t == 1
    assert xs[1].t == 2
