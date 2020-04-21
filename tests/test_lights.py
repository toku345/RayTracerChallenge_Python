from raytracerchallenge_python.tuple import Color, Point
from raytracerchallenge_python.point_light import PointLight


def test_a_point_light_has_a_position_and_intensity():
    # Given
    intensity = Color(1, 1, 1)
    position = Point(0, 0, 0)
    # When
    light = PointLight(position, intensity)
    # Then
    assert light.position == position
    assert light.intensity == intensity
