from raytracerchallenge_python.intersection import Intersection, Intersections
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.plane import Plane
from raytracerchallenge_python.sphere import glass_sphere
from raytracerchallenge_python.transformations import scaling, translation

from raytracerchallenge_python.helpers import EPSILON

from math import sqrt


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


def test_precomputing_the_state_of_an_intersection():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    # When
    comps = i.prepare_computations(r)
    # Then
    assert comps.t == i.t
    assert comps.object == i.object
    assert comps.point == Point(0, 0, -1)
    assert comps.eyev == Vector(0, 0, -1)
    assert comps.normalv == Vector(0, 0, -1)


def test_the_hit__when_an_intersection_occurs_on_the_outside():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    # When
    comps = i.prepare_computations(r)
    # Then
    assert comps.inside is False


def test_the_hit__when_an_intersection_occurs_on_the_inside():
    # Given
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    # When
    comps = i.prepare_computations(r)
    # Then
    assert comps.point == Point(0, 0, 1)
    assert comps.eyev == Vector(0, 0, -1)
    assert comps.inside is True
    assert comps.normalv == Vector(0, 0, -1)


def test_the_hit_should_offset_the_point():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    shape.transform = translation(0, 0, 1)
    i = Intersection(5, shape)
    # When
    comps = i.prepare_computations(r)
    # Then
    assert comps.over_point.z < -EPSILON / 2
    assert comps.point.z > comps.over_point.z


def precomputing_the_reflection_vector():
    # Given
    shape = Plane()
    r = Ray(Point(0, 1, -1), Vector(0, -sqrt(2) / 2, sqrt(2) / 2))
    i = Intersection(sqrt(2), shape)
    # When
    comps = i.prepare_computations(r)
    # Then
    assert comps.reflectv == Vector(0, sqrt(2) / 2, sqrt(2) / 2)


def test_finding_n1_and_n2_at_various_intersections():
    # Given
    A = glass_sphere()
    A.transform = scaling(2, 2, 2)
    A.material.refractive_index = 1.5

    B = glass_sphere()
    B.transform = translation(0, 0, -0.25)
    B.material.refractive_index = 2.0

    C = glass_sphere()
    C.transform = translation(0, 0, 0.25)
    C.material.refractive_index = 2.5

    r = Ray(Point(0, 0, -4), Vector(0, 0, 1))
    xs = Intersections(Intersection(2, A),
                       Intersection(2.75, B),
                       Intersection(3.25, C),
                       Intersection(4.75, B),
                       Intersection(5.25, C),
                       Intersection(6, A))
    EXAMPLES = [
        {'n1': 1.0, 'n2': 1.5},  # index: 0
        {'n1': 1.5, 'n2': 2.0},  # index: 1
        {'n1': 2.0, 'n2': 2.5},  # index: 2
        {'n1': 2.5, 'n2': 2.5},  # index: 3
        {'n1': 2.5, 'n2': 1.5},  # index: 4
        {'n1': 1.5, 'n2': 1.0},  # index: 5
    ]
    for index in range(len(EXAMPLES)):
        # When
        comps = xs[index].prepare_computations(r, xs=xs)
        # Then
        assert comps.n1 == EXAMPLES[index]['n1']
        assert comps.n2 == EXAMPLES[index]['n2']


def test_the_under_point_is_offset_below_the_surface():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = glass_sphere()
    shape.transform = translation(0, 0, 1)
    i = Intersection(5, shape)
    xs = Intersections(i)
    # When
    comps = i.prepare_computations(r, xs)
    # Then
    assert comps.under_point.z > EPSILON / 2
    assert comps.point.z < comps.under_point.z
