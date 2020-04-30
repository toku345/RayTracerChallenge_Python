from raytracerchallenge_python.transformations import (
    translation, scaling, rotation_x, rotation_y, rotation_z, shearing,
    view_transform)
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.matrix import identity_matrix, Matrix

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


def test_individual_transformations_are_applied_in_sequence():
    # Given
    p = Point(1, 0, 1)
    A = rotation_x(pi / 2)
    B = scaling(5, 5, 5)
    C = translation(10, 5, 7)

    # apply rotation first
    # When
    p2 = A * p
    # Then
    assert p2 == Point(1, -1, 0)

    # then apply scaling
    # When
    p3 = B * p2
    # Then
    assert p3 == Point(5, -5, 0)

    # then apply translation
    # When
    p4 = C * p3
    # Then
    assert p4 == Point(15, 0, 7)


def test_chained_transformations_must_be_applied_in_reverse_order():
    # Given
    p = Point(1, 0, 1)
    A = rotation_x(pi / 2)
    B = scaling(5, 5, 5)
    C = translation(10, 5, 7)
    # When
    T = C * B * A
    # Then
    assert T * p == Point(15, 0, 7)


def test_the_transformation_matrix_for_the_default_orientation():
    # Given
    f = Point(0, 0, 0)  # from
    to = Point(0, 0, -1)
    up = Vector(0, 1, 0)
    # When
    t = view_transform(f, to, up)
    # Then
    assert t == identity_matrix()


def test_a_view_transformation_matrix_looking_in_positive_z_direction():
    # Given
    f = Point(0, 0, 0)
    to = Point(0, 0, 1)
    up = Vector(0, 1, 0)
    # When
    t = view_transform(f, to, up)
    # Then
    assert t == scaling(-1, 1, -1)


def test_the_view_transformation_moves_the_world():
    # Given
    f = Point(0, 0, 8)
    to = Point(0, 0, 0)
    up = Vector(0, 1, 0)
    # When
    t = view_transform(f, to, up)
    # Then
    assert t == translation(0, 0, -8)


def test_an_arbitray_view_transformation():
    # Given
    f = Point(1, 3, 2)
    to = Point(4, -2, 8)
    up = Vector(1, 1, 0)
    # When
    t = view_transform(f, to, up)
    # Then
    assert t == Matrix(-0.50709, 0.50709, 0.67612, -2.36643,
                       0.76772, 0.60609, 0.12122, -2.82843,
                       -0.35857, 0.59761, -0.71714, 0.00000,
                       0.00000, 0.00000,  0.00000,  1.00000)
