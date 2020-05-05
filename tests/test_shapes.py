from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import translation
from raytracerchallenge_python.shape import Shape


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
