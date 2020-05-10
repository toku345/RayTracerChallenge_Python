from raytracerchallenge_python.ring_pattern import RingPattern
from raytracerchallenge_python.tuple import Color, Point

BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)


def test_a_ring_should_extend_in_both_x_and_z():
    # Given
    pattern = RingPattern(WHITE, BLACK)
    # Then
    assert pattern.pattern_at(Point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(Point(1, 0, 0)) == BLACK
    assert pattern.pattern_at(Point(0, 0, 1)) == BLACK
    # 0.708 = just slightly more than sqrt(2) / 2
    assert pattern.pattern_at(Point(0.708, 0, 0.708)) == BLACK
