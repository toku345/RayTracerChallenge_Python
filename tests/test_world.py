from raytracerchallenge_python.world import World, default_world
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.tuple import Point, Vector, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.transformations import scaling
from raytracerchallenge_python.ray import Ray


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


def test_intersect_a_world_with_a_ray():
    # Given
    w = default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    # When
    xs = w.intersect_world(r)
    # Then
    assert len(xs) == 4
    assert xs[0].t == 4
    assert xs[1].t == 4.5
    assert xs[2].t == 5.5
    assert xs[3].t == 6
