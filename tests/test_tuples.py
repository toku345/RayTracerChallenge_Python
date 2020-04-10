from raytracerchallenge_python.tuple import Tuple, Point, Vector, Color
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
    p = Point(4, -4, 3)
    # Then
    assert p == Tuple(4, -4, 3, 1)


def test_func_vector_creates_tuples_with_w_equal_0():
    # Given
    p = Vector(4, -4, 3)
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
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    # Then
    assert p1 - p2 == Vector(-2, -4, -6)


def test_subtracting_a_vector_from_a_point():
    # Given
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)
    # Then
    assert p - v == Point(-2, -4, -6)


def test_subtracting_two_vectors():
    # Given
    v1 = Vector(3, 2, 1)
    v2 = Vector(5, 6, 7)
    # Then
    assert v1 - v2 == Vector(-2, -4, -6)


def test_subtracing_a_vector_from_the_zero_vector():
    # Given
    zero = Vector(0, 0, 0)
    v = Vector(1, -2, 3)
    # Then
    assert zero - v == Vector(-1, 2, -3)


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
    v = Vector(1, 0, 0)
    # Then
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_0_1_0():
    # Given
    v = Vector(0, 1, 0)
    # Then
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_0_0_1():
    # Given
    v = Vector(0, 0, 1)
    # Then
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_1_2_3():
    # Given
    v = Vector(1, 2, 3)
    # Then
    assert v.magnitude() == sqrt(14)


def test_computing_the_magnitude_of_vector_negative1_negative2_negative3():
    # Given
    v = Vector(-1, -2, -3)
    # Then
    assert v.magnitude() == sqrt(14)


def test_normalizing_vector_4_0_0_gives_1_0_0():
    # Given
    v = Vector(4, 0, 0)
    # Then
    assert v.normalize() == Vector(1, 0, 0)


def test_normalizing_vector_1_2_3():
    # Given
    v = Vector(1, 2, 3)
    # Then
    assert v.normalize() == Vector(1/sqrt(14), 2 / sqrt(14), 3 / sqrt(14))


def test_magnitude_of_a_normalized_vector():
    # Given
    v = Vector(1, 2, 3)
    # When
    norm = v.normalize()
    # Then
    assert norm.magnitude() == 1


def test_the_dot_product_of_two_tuples():
    # Given
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    # Then
    assert a.dot(b) == 20


def test_the_cross_product_of_two_vectors():
    # Given
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    # Then
    assert a.cross(b) == Vector(-1, 2, -1)
    assert b.cross(a) == Vector(1, -2, 1)


def test_colors_are_red_green_blue_tuples():
    # Given
    c = Color(-0.5, 0.4, 1.7)
    # Then
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7
