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


def test_writing_pixels_to_a_canvas():
    # Given
    c = Canvas(10, 20)
    red = Color(1, 0, 0)
    # When
    c.write_pixel(2, 3, red)
    # Then
    assert c.pixel_at(2, 3) == red
    assert c.pixels[3][2] == red
