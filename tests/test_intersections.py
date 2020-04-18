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


def test_the_hit__when_all_intersections_have_positive_t():
    # Given
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = Intersections(i2, i1)
    # When
    i = xs.hit()
    # Then
    assert i == i1


def test_the_hit__when_some_intersections_have_negative_t():
    # Given
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = Intersections(i2, i1)
    # When
    i = xs.hit()
    # Then
    assert i == i2


def test_the_hit__when_all_intersections_have_netative_t():
    # Given
    s = Sphere()
    i1 = Intersection(-2, s)
    i2 = Intersection(-1, s)
    xs = Intersections(i2, i1)
    # When
    i = xs.hit()
    # Then
    assert i is None


def test_the_hit_is_always_the_lowest_nonnegative_intersection():
    # Given
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = Intersections(i1, i2, i3, i4)
    # When
    i = xs.hit()
    # Then
    assert i == i4