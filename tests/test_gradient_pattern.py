from raytracerchallenge_python.gradient_pattern import GradientPattern
from raytracerchallenge_python.tuple import Color, Point

BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)


def test_a_gradient_linearly_interpolates_between_colors():
    # Given
    pattern = GradientPattern(WHITE, BLACK)
    # Then
    assert pattern.pattern_at(Point(0.25, 0, 0)) == Color(0.75, 0.75, 0.75)
    assert pattern.pattern_at(Point(0.5, 0, 0)) == Color(0.5, 0.5, 0.5)
    assert pattern.pattern_at(Point(0.75, 0, 0)) == Color(0.25, 0.25, 0.25)
