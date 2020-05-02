from raytracerchallenge_python.camera import Camera
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.tuple import Point, Vector, Color
from raytracerchallenge_python.transformations import (
    rotation_y, translation, view_transform)
from raytracerchallenge_python.world import default_world

from raytracerchallenge_python.helpers import equal

from math import pi, sqrt


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


def test_constructing_a_ray_through_the_center_of_the_canvas():
    # Given
    c = Camera(201, 101, pi / 2)
    # When
    r = c.ray_for_pixel(100, 50)
    # Then
    assert r.origin == Point(0, 0, 0)
    assert r.direction == Vector(0, 0, -1)


def test_constructing_a_ray_through_a_corner_of_the_canvas():
    # Given
    c = Camera(201, 101, pi / 2)
    # When
    r = c.ray_for_pixel(0, 0)
    # Then
    assert r.origin == Point(0, 0, 0)
    assert r.direction == Vector(0.66519, 0.33259, -0.66851)


def test_constructing_a_ray_when_the_camera_is_transformed():
    # Given
    c = Camera(201, 101, pi / 2)
    # When
    c.transform = rotation_y(pi / 4) * translation(0, -2, 5)
    r = c.ray_for_pixel(100, 50)
    # Then
    assert r.origin == Point(0, 2, -5)
    assert r.direction == Vector(sqrt(2) / 2, 0, -sqrt(2) / 2)


def test_rendering_a_world_with_a_camera():
    # Given
    w = default_world()
    c = Camera(11, 11, pi / 2)
    f = Point(0, 0, -5)
    to = Point(0, 0, 0)
    up = Vector(0, 1, 0)
    c.transform = view_transform(f, to, up)
    # When
    image = c.render(w)
    # Then
    assert image.pixel_at(5, 5) == Color(0.38066, 0.47583, 0.2855)
