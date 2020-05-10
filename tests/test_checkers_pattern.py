from raytracerchallenge_python.checkers_pattern import CheckersPattern
from raytracerchallenge_python.tuple import Color, Point

BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)


def test_checkers_should_repeat_in_x():
    # Given
    pattern = CheckersPattern(WHITE, BLACK)
    # Then
    assert pattern.pattern_at(Point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(Point(0.99, 0, 0)) == WHITE
    assert pattern.pattern_at(Point(1.01, 0, 0)) == BLACK


def test_checkers_should_repeat_in_y():
    # Given
    pattern = CheckersPattern(WHITE, BLACK)
    # Then
    assert pattern.pattern_at(Point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(Point(0, 0.99, 0)) == WHITE
    assert pattern.pattern_at(Point(0, 1.01, 0)) == BLACK


def test_checkers_should_repeat_in_z():
    # Given
    pattern = CheckersPattern(WHITE, BLACK)
    # Then
    assert pattern.pattern_at(Point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(Point(0, 0, 0.99)) == WHITE
    assert pattern.pattern_at(Point(0, 0, 1.01)) == BLACK
