from raytracerchallenge_python.tuple import Color
from raytracerchallenge_python.canvas import Canvas


def test_creating_a_canvas():
    # Given
    c = Canvas(10, 20)
    # Then
    assert c.width == 10
    assert c.height == 20

    for h in range(20):
        for w in range(10):
            assert c.pixels[h][w] == Color(0, 0, 0)

    b = Color(0, 0, 0)
    assert c.pixels == \
        [
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b],
        ]
