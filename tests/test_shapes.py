from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import translation
from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.material import Material


class MockShape(Shape):
    pass


def test_the_default_transformation():
    # Given
    s = MockShape()
    # Then
    assert s.transform == identity_matrix()


def test_assigning_a_transformation():
    # Given
    s = MockShape()
    # When
    s.transform = translation(2, 3, 4)
    # Then
    assert s.transform == translation(2, 3, 4)


def test_the_default_material():
    # Given
    s = MockShape()
    # When
    m = s.material
    # Then
    assert m == Material()


def test_assigning_a_material():
    # Given
    s = MockShape()
    m = Material()
    m.ambient = 1
    # When
    s.material = m
    # Then
    assert s.material == m
