from raytracerchallenge_python.world import World, default_world
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.tuple import Point, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.transformations import scaling


def test_createing_a_world():
    # Given
    w = World()
    # Then
    assert len(w.objects) == 0
    assert w.light is None


def test_default_world():
    # Given
    light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.set_transform(scaling(0.5, 0.5, 0.5))
    # When
    w = default_world()
    # Then
    assert w.light == light
    assert s1 in w.objects
    assert s2 in w.objects
