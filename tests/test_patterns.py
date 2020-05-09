from raytracerchallenge_python.pattern import Pattern
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import translation, scaling
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.tuple import Point, Color


class MockPattern(Pattern):
    def pattern_at(self, point):
        return Color(point.x, point.y, point.z)


def test_the_default_pattern_transformation():
    # Given
    pattern = MockPattern()
    # Then
    assert pattern.transform == identity_matrix()


def test_assigning_a_transformation():
    # Given
    pattern = MockPattern()
    # When
    pattern.transform = translation(1, 2, 3)
    # Then
    assert pattern.transform == translation(1, 2, 3)


def test_a_pattern_with_an_object_transformation():
    # Given
    shape = Sphere()
    shape.transform = scaling(2, 2, 2)
    pattern = MockPattern()
    # When
    c = pattern.pattern_at_shape(shape, Point(2, 3, 4))
    # Then
    assert c == Color(1, 1.5, 2)


def test_a_pattern_with_a_pattern_transformation():
    # Given
    shape = Sphere()
    pattern = MockPattern()
    pattern.transform = scaling(2, 2, 2)
    # When
    c = pattern.pattern_at_shape(shape, Point(2, 3, 4))
    # Then
    assert c == Color(1, 1.5, 2)


def test_a_pattern_with_both_an_object_and_a_pattern_transformation():
    # Given
    shape = Sphere()
    shape.transform = scaling(2, 2, 2)
    pattern = MockPattern()
    pattern.transform = translation(0.5, 1, 1.5)
    # When
    c = pattern.pattern_at_shape(shape, Point(2.5, 3, 3.5))
    # Then
    assert c == Color(0.75, 0.5, 0.25)
