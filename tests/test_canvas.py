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


def test_constructing_the_ppm_header():
    # Given
    c = Canvas(5, 3)
    # When
    ppm = c.to_ppm()
    # Then
    assert ppm.split("\n")[0:3] == ["P3",
                                    "5 3",
                                    "255"]


def test_constructing_the_ppm_pixel_data():
    # Given
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    # When
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = c.to_ppm()
    # Then
    assert ppm.split("\n")[3:6] == \
        ["255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"]


def test_splitting_long_lines_in_ppm_files():
    # Given
    c = Canvas(10, 2)
    # When
    color = Color(1, 0.8, 0.6)
    for y in range(2):
        for x in range(10):
            c.write_pixel(x, y, color)
    ppm = c.to_ppm()
    # Then
    assert ppm.split("\n")[3:7] == \
        ["255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
         "153 255 204 153 255 204 153 255 204 153 255 204 153",
         "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
         "153 255 204 153 255 204 153 255 204 153 255 204 153"]
