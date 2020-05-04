from raytracerchallenge_python.world import World, default_world
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.tuple import Point, Vector, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.transformations import scaling, translation
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.intersection import Intersection


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


def test_shading_an_intersection():
    # Given
    w = default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = w.objects[0]
    i = Intersection(4, shape)
    # When
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    # Then
    assert c == Color(0.38066, 0.47583, 0.2855)


def test_shading_an_intersection_from_the_inside():
    # Given
    w = default_world()
    w.light = PointLight(Point(0, 0.25, 0), Color(1, 1, 1))
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = w.objects[1]
    i = Intersection(0.5, shape)
    # When
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    # Then
    assert c == Color(0.90498, 0.90498, 0.90498)


def test_the_color_when_a_ray_misses():
    # Given
    w = default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
    # When
    c = w.color_at(r)
    # Then
    assert c == Color(0, 0, 0)


def test_the_color_when_a_ray_hits():
    # Given
    w = default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    # When
    c = w.color_at(r)
    # Then
    assert c == Color(0.38066, 0.47583, 0.2855)


def test_the_color_with_an_intersection_behind_the_ray():
    # Given
    w = default_world()
    outer = w.objects[0]
    outer.material.ambient = 1
    inner = w.objects[1]
    inner.material.ambient = 1
    r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    # When
    c = w.color_at(r)
    # Then
    assert c == inner.material.color


def test_there_is_no_shadow_when_nothing_is_collinear_with_point_and_light():
    # Given
    w = default_world()
    p = Point(0, 10, 0)
    # Then
    assert w.is_shadowed(p) is False


def test_the_shadow_when_an_object_is_between_the_point_and_the_light():
    # Given
    w = default_world()
    p = Point(10, -10, 10)
    # Then
    assert w.is_shadowed(p) is True


def test_there_is_no_shadow_when_an_object_is_behind_the_light():
    # Given
    w = default_world()
    p = Point(-20, 20, -20)
    # Then
    assert w.is_shadowed(p) is False


def test_there_is_no_shadow_when_an_object_is_behind_the_point():
    # Given
    w = default_world()
    p = Point(-2, 2, -2)
    # Then
    assert w.is_shadowed(p) is False


def test__shade_hit__is_given_an_intersection_in_shadow():
    # Given
    w = World()
    w.light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
    s1 = Sphere()
    w.objects.append(s1)
    s2 = Sphere()
    s2.transform = translation(0, 0, 10)
    w.objects.append(s2)
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    i = Intersection(4, s2)
    # When
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    # Then
    assert c == Color(0.1, 0.1, 0.1)
