from raytracerchallenge_python.transformations import (
    translation, scaling, rotation_x, rotation_y, rotation_z, shearing)
from raytracerchallenge_python.tuple import Point, Vector

from math import pi, sqrt


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


def test_rotating_a_point_around_the_x_axis():
    # Given
    p = Point(0, 1, 0)
    half_quarter = rotation_x(pi / 4)
    full_quarter = rotation_x(pi / 2)
    # Then
    assert half_quarter * p == Point(0, sqrt(2) / 2, sqrt(2) / 2)
    assert full_quarter * p == Point(0, 0, 1)


def test_the_inverse_of_an__x_rotation__rotates_in_the_opposite_direction():
    # Given
    p = Point(0, 1, 0)
    half_quarter = rotation_x(pi / 4)
    inv = half_quarter.inverse()
    # Then
    assert inv * p == Point(0, sqrt(2) / 2, -sqrt(2) / 2)


def test_rotating_a_point_around_the_y_axis():
    # Given
    p = Point(0, 0, 1)
    half_quarter = rotation_y(pi / 4)
    full_quarter = rotation_y(pi / 2)
    # Then
    assert half_quarter * p == Point(sqrt(2) / 2, 0, sqrt(2) / 2)
    assert full_quarter * p == Point(1, 0, 0)


def test_rotating_a_point_around_the_z_axis():
    # Given
    p = Point(0, 1, 0)
    half_quarter = rotation_z(pi / 4)
    full_quarter = rotation_z(pi / 2)
    # Then
    assert half_quarter * p == Point(-sqrt(2) / 2, sqrt(2) / 2, 0)
    assert full_quarter * p == Point(-1, 0, 0)


def test_a_shearing_transformation_moves_x_in_propotion_to_y():
    # Given
    transform = shearing(1, 0, 0, 0, 0, 0)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(5, 3, 4)


def test_a_shearing_transformation_moves_x_in_propotion_to_z():
    # Given
    transform = shearing(0, 1, 0, 0, 0, 0)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(6, 3, 4)


def test_a_shearing_transformation_moves_y_in_propotion_to_x():
    # Given
    transform = shearing(0, 0, 1, 0, 0, 0)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(2, 5, 4)


def test_a_shearing_transformation_moves_y_in_propotion_to_z():
    # Given
    transform = shearing(0, 0, 0, 1, 0, 0)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(2, 7, 4)


def test_a_shearing_transformation_moves_z_in_propotion_to_x():
    # Given
    transform = shearing(0, 0, 0, 0, 1, 0)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(2, 3, 6)


def test_a_shearing_transformation_moves_z_in_propotion_to_y():
    # Given
    transform = shearing(0, 0, 0, 0, 0, 1)
    p = Point(2, 3, 4)
    # Then
    assert transform * p == Point(2, 3, 7)
