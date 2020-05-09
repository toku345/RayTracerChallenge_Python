from raytracerchallenge_python.stripe_pattern import StripePattern
from raytracerchallenge_python.tuple import Color, Point
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.transformations import scaling, translation


BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)


def test_creating_a_stripe_pattern():
    # Given
    pattern = StripePattern(WHITE, BLACK)
    # Then
    assert pattern.a == WHITE
    assert pattern.b == BLACK


def test_a_stripe_pattern_is_constant_in_y():
    # Given
    pattern = StripePattern(WHITE, BLACK)
    # Then
    assert pattern.stripe_at(Point(0, 0, 0)) == WHITE
    assert pattern.stripe_at(Point(0, 1, 0)) == WHITE
    assert pattern.stripe_at(Point(0, 2, 0)) == WHITE


def test_a_stripe_pattern_is_constant_in_z():
    # Given
    pattern = StripePattern(WHITE, BLACK)
    # Then
    assert pattern.stripe_at(Point(0, 0, 0)) == WHITE
    assert pattern.stripe_at(Point(0, 0, 1)) == WHITE
    assert pattern.stripe_at(Point(0, 0, 2)) == WHITE


def test_a_stripe_pattern_alternates_in_x():
    # Given
    pattern = StripePattern(WHITE, BLACK)
    # Then
    assert pattern.stripe_at(Point(0, 0, 0)) == WHITE
    assert pattern.stripe_at(Point(0.9, 0, 0)) == WHITE
    assert pattern.stripe_at(Point(1, 0, 0)) == BLACK
    assert pattern.stripe_at(Point(-0.1, 0, 0)) == BLACK
    assert pattern.stripe_at(Point(-1, 0, 0)) == BLACK
    assert pattern.stripe_at(Point(-1.1, 0, 0)) == WHITE


def test_stripes_with_an_object_transformation():
    # Given
    object = Sphere()
    object.transform = scaling(2, 2, 2)
    pattern = StripePattern(WHITE, BLACK)
    # When
    c = pattern.stripe_at_object(object, Point(1.5, 0, 0))
    # Then
    assert c == WHITE


def test_stripes_with_a_pattern_transformation():
    # Given
    object = Sphere()
    pattern = StripePattern(WHITE, BLACK)
    pattern.transform = scaling(2, 2, 2)
    # When
    c = pattern.stripe_at_object(object, Point(1.5, 0, 0))
    # Then
    assert c == WHITE


def test_stripes_with_both_an_object_and_a_pattern_transformation():
    # Given
    object = Sphere()
    object.transform = scaling(2, 2, 2)
    pattern = StripePattern(WHITE, BLACK)
    pattern.transform = translation(0.5, 0, 0)
    # When
    c = pattern.stripe_at_object(object, Point(2.5, 0, 0))
    # Then
    assert c == WHITE
