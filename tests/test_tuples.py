from raytracerchallenge_python.tuple import Tuple


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
