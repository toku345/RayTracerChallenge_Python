from raytracerchallenge_python.tuple import Tuple, point, vector
from math import sqrt


def test_a_tuple_with_w_equal_1_is_a_point():
    # Given
    a = Tuple(4.3, -4.2, 3.1, 1.0)
    # Then
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 1.0
    assert a.is_point()
    assert not a.is_vector()


def test_a_tuple_with_w_equal_0_is_a_vector():
    # Given
    a = Tuple(4.3, -4.2, 3.1, 0.0)
    # Then
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 0.0
    assert not a.is_point()
    assert a.is_vector()


def test_equivalence_tuple_objects():
    a = Tuple(4.3, -4.2, 3.1, 1.0)
    assert a == Tuple(4.3, -4.2, 3.1, 1.0)
    assert a != Tuple(9.9, -4.2, 3.1, 1.0)
    assert a != Tuple(4.3,  9.9, 3.1, 1.0)
    assert a != Tuple(4.3, -4.2, 9.9, 1.0)
    assert a != Tuple(4.3, -4.2, 3.1, 0.0)
    assert a != (4.3, -4.2, 3.1, 1.0)


def test_func_point_creates_tuples_with_w_equal_1():
    # Given
    p = point(4, -4, 3)
    # Then
    assert p == Tuple(4, -4, 3, 1)


def test_func_vector_creates_tuples_with_w_equal_0():
    # Given
    p = vector(4, -4, 3)
    # Then
    assert p == Tuple(4, -4, 3, 0)


def test_adding_two_tuples():
    # Given
    a1 = Tuple(3, -2, 5, 1)
    a2 = Tuple(-2, 3, 1, 0)
    # Then
    assert a1 + a2 == Tuple(1, 1, 6, 1)


def test_subtracting_two_points():
    # Given
    p1 = point(3, 2, 1)
    p2 = point(5, 6, 7)
    # Then
    assert p1 - p2 == vector(-2, -4, -6)


def test_subtracting_a_vector_from_a_point():
    # Given
    p = point(3, 2, 1)
    v = vector(5, 6, 7)
    # Then
    assert p - v == point(-2, -4, -6)


def test_subtracting_two_vectors():
    # Given
    v1 = vector(3, 2, 1)
    v2 = vector(5, 6, 7)
    # Then
    assert v1 - v2 == vector(-2, -4, -6)


def test_subtracing_a_vector_from_the_zero_vector():
    # Given
    zero = vector(0, 0, 0)
    v = vector(1, -2, 3)
    # Then
    assert zero - v == vector(-1, 2, -3)


def test_negating_a_tuple():
    # Given
    a = Tuple(1, -2, 3, -4)
    # Then
    assert -a == Tuple(-1, 2, -3, 4)


def test_multiplying_a_tuple_by_a_scalar():
    # Given
    a = Tuple(1, -2, 3, -4)
    # Then
    assert a * 3.5 == Tuple(3.5, -7.0, 10.5, -14)


def test_multiplying_a_tuple_by_a_fraction():
    # Given
    a = Tuple(1, -2, 3, -4)
    # Then
    assert a * 0.5 == Tuple(0.5, -1, 1.5, -2)


def test_dividing_a_tuple_by_a_scalar():
    # Given
    a = Tuple(1, -2, 3, -4)
    # Then
    assert a / 2 == Tuple(0.5, -1, 1.5, -2)


def test_computing_the_magnitude_of_vector_1_0_0():
    # Given
    v = vector(1, 0, 0)
    # Then
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_0_1_0():
    # Given
    v = vector(0, 1, 0)
    # Then
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_0_0_1():
    # Given
    v = vector(0, 0, 1)
    # Then
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_1_2_3():
    # Given
    v = vector(1, 2, 3)
    # Then
    assert v.magnitude() == sqrt(14)


def test_computing_the_magnitude_of_vector_negative1_negative2_negative3():
    # Given
    v = vector(-1, -2, -3)
    # Then
    assert v.magnitude() == sqrt(14)
