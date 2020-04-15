from raytracerchallenge_python.transformations import translation, scaling
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


def test_scaling_matrix_applied_to_a_point():
    # Given
    trasform = scaling(2, 3, 4)
    p = Point(-4, 6, 8)
    # Then
    assert trasform * p == Point(-8, 18, 32)


def test_a_scaling_matrix_applied_to_a_vector():
    # Given
    tranform = scaling(2, 3, 4)
    v = Vector(-4, 6, 8)
    # Then
    assert tranform * v == Vector(-8, 18, 32)


def test_multiplying_by_the_inverse_of_a_scaling_matrix():
    # Given
    transform = scaling(2, 3, 4)
    inv = transform.inverse()
    v = Vector(-4, 6, 8)
    # Then
    assert inv * v == Vector(-2, 2, 2)


def test_reflection_is_scaling_by_a_negative_value():
    # Given
    transform = scaling(-1, 1, 1)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(-2, 3, 4)
