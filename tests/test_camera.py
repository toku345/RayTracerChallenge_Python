from raytracerchallenge_python.camera import Camera
from raytracerchallenge_python.matrix import identity_matrix

from raytracerchallenge_python.helpers import equal

from math import pi


def test_constructing_a_camera():
    # Given
    hsize = 160
    vsize = 120
    field_of_view = pi / 2
    # When
    c = Camera(hsize, vsize, field_of_view)
    # Then
    assert c.hsize == 160
    assert c.vsize == 120
    assert c.field_of_view == pi / 2
    assert c.transform == identity_matrix()


def test_the_pixel_size_for_a_horizontal_canvas():
    # Given
    c = Camera(200, 125, pi / 2)
    # Then
    assert equal(c.pixel_size, 0.01)


def test_the_pixel_size_for_a_vertical_canvas():
    # Given
    c = Camera(125, 200, pi / 2)
    # Then
    assert equal(c.pixel_size, 0.01)
