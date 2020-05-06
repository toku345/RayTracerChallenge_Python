from raytracerchallenge_python.material import Material
from raytracerchallenge_python.tuple import Color, Point, Vector
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.stripe_pattern import StripePattern

from math import sqrt


def test_the_default_material():
    # Given
    m = Material()
    # Then
    assert m.color == Color(1, 1, 1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200.0


def test_material_equality_with_identical_materials():
    m1 = Material()
    m2 = Material()
    assert m1 == m2


def test_material_equality_with_different_materials():
    m1 = Material()
    m2 = Material()
    m2.ambient = 1
    assert m1 != m2


def test_lighting_with_the_eye_between_the_light_and_the_surface():
    # Given
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
    # When
    result = m.lighting(light, position, eyev, normalv)
    # Then
    assert result == Color(1.9, 1.9, 1.9)


def test_lighting_with_the_eye_between_light_and_surface_eye_offset_45degree():
    # Given
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, sqrt(2) / 2, sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
    # When
    result = m.lighting(light, position, eyev, normalv)
    # Then
    assert result == Color(1.0, 1.0, 1.0)


def test_lighting_with_the_eye_opposite_surface_light_offset_45degree():
    # Given
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
    # When
    result = m.lighting(light, position, eyev, normalv)
    # Then
    assert result == Color(0.7364, 0.7364, 0.7364)


def test_lighting_with_the_eye_in_the_path_of_the_reflection_vector():
    # Given
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, -sqrt(2) / 2, -sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
    # When
    result = m.lighting(light, position, eyev, normalv)
    # Then
    assert result == Color(1.6364, 1.6364, 1.6364)


def test_lighting_with_the_light_behind_the_surface():
    # Given
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, 10), Color(1, 1, 1))
    # When
    result = m.lighting(light, position, eyev, normalv)
    # Then
    assert result == Color(0.1, 0.1, 0.1)


def test_lighting_with_the_surface_in_shadow():
    # Given
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
    in_shadow = True
    # When
    result = m.lighting(light, position, eyev, normalv, in_shadow)
    # Then
    assert result == Color(0.1, 0.1, 0.1)


def test_lighting_with_a_pattern_applied():
    # Given
    m = Material()
    m.pattern = StripePattern(Color(1, 1, 1), Color(0, 0, 0))
    m.ambient = 1
    m.diffuse = 0
    m.specular = 0
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
    # When
    c1 = m.lighting(light, Point(0.9, 0, 0), eyev, normalv)
    c2 = m.lighting(light, Point(1.1, 0, 0), eyev, normalv)
    # Then
    assert c1 == Color(1, 1, 1)
    assert c2 == Color(0, 0, 0)
