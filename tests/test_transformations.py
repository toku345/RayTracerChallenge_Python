from raytracerchallenge_python.transformations import translation
from raytracerchallenge_python.tuple import Point, Vector


def test_multiplying_by_a_translation_matrix():
    # Given
    transform = translation(5, -3, 2)
    p = Point(-3, 4, 5)
    # Then
    assert transform * p == Point(2, 1, 7)


def test_multiplying_by_the_inverse_of_a_translation_matrix():
    # Given
    transform = translation(5, -3, 2)
    inv = transform.inverse()
    p = Point(-3, 4, 5)
    # Then
    assert inv * p == Point(-8, 7, 3)


def test_translation_does_not_affect_vectors():
    # Given
    transform = translation(5, -3, 2)
    v = Vector(-3, 4, 5)
    # Then
    assert transform * v == v
