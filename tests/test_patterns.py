from raytracerchallenge_python.pattern import Pattern
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import translation


class TestPattern(Pattern):
    pass


def test_the_default_pattern_transformation():
    # Given
    pattern = TestPattern()
    # Then
    assert pattern.transform == identity_matrix()


def test_assigning_a_transformation():
    # Given
    pattern = TestPattern()
    # When
    pattern.transform = translation(1, 2, 3)
    # Then
    assert pattern.transform == translation(1, 2, 3)
