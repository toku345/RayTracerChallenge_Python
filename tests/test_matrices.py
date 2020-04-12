from raytracerchallenge_python.matrix import Matrix


def test_constructing_and_inspecting_a_4x4_matrix():
    # Given
    M = Matrix(1, 2, 3, 4,
               5.5, 6.5, 7.5, 8.5,
               9, 10, 11, 12,
               13.5, 14.5, 15.5, 16.5)
    # Then
    assert M.at(0, 0) == 1
    assert M.at(0, 3) == 4
    assert M.at(1, 0) == 5.5
    assert M.at(1, 2) == 7.5
    assert M.at(2, 2) == 11
    assert M.at(3, 0) == 13.5
    assert M.at(3, 2) == 15.5


def test_a_2x2_matrix_ought_to_be_representable():
    # Given
    M = Matrix(-3, 5,
               1, -2)
    # Then
    assert M.at(0, 0) == -3
    assert M.at(0, 1) == 5
    assert M.at(1, 0) == 1
    assert M.at(1, 1) == -2


def test_a_3x3_matrix_ought_to_be_representable():
    # Given
    M = Matrix(-3, 5, 0,
               1, -2, -7,
               0, 1, 1)
    # Then
    assert M.at(0, 0) == -3
    assert M.at(1, 1) == -2
    assert M.at(2, 2) == 1
