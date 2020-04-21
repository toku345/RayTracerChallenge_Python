from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import (
    translation, scaling, rotation_z)
from raytracerchallenge_python.material import Material
from math import pi, sqrt


def test_a_ray_intersects_a_sphere_at_two_points():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0


def test_a_ray_intersects_a_sphere_at_a_tangent():
    # Then
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == 5.0
    assert xs[1].t == 5.0


def test_a_ray_misses_s_sphere():
    # Given
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 0


def test_a_ray_originates_inside_a_sphere():
    # Given
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == -1.0
    assert xs[1].t == 1.0


def test_a_sphere_is_behind_a_ray():
    # Given
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == -6.0
    assert xs[1].t == -4.0


def test_intersect_sets_the_object_on_the_intersection():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].object == s
    assert xs[1].object == s


def test_a_spheres_default_transformation():
    # Given
    s = Sphere()
    # Then
    assert s.transform == identity_matrix()


def test_changing_a_spheres_transformation():
    # Given
    s = Sphere()
    t = translation(2, 3, 4)
    # When
    s.set_transform(t)
    # Then
    assert s.transform == t


def test_intersecting_a_scaled_sphere_with_a_ray():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    s.set_transform(scaling(2, 2, 2))
    xs = s.intersect(r)
    # Then
    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7


def test_intersecting_a_translated_sphere_with_a_ray():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    # When
    s.set_transform(translation(5, 0, 0))
    xs = s.intersect(r)
    # Then
    assert len(xs) == 0


def test_the_normal_on_a_sphere_at_a_point_on_the_x_axis():
    # Given
    s = Sphere()
    # When
    n = s.normal_at(Point(1, 0, 0))
    # Then
    assert n == Vector(1, 0, 0)


def test_the_normal_on_a_sphere_at_a_point_on_the_y_axis():
    # Given
    s = Sphere()
    # When
    n = s.normal_at(Point(0, 1, 0))
    # Then
    assert n == Vector(0, 1, 0)


def test_the_normal_on_a_sphere_at_a_point_on_the_z_axis():
    # Given
    s = Sphere()
    # When
    n = s.normal_at(Point(0, 0, 1))
    # Then
    assert n == Vector(0, 0, 1)


def test_the_normal_on_a_sphere_at_a_point_at_a_nonaxial_axis():
    # Given
    s = Sphere()
    # When
    n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
    # Then
    assert n == Vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3)


def test_the_normal_is_a_normalized_vector():
    # Given
    s = Sphere()
    # When
    n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
    # Then
    assert n == n.normalize()


def test_computing_the_normal_on_a_translated_sphere():
    # Given
    s = Sphere()
    s.set_transform(translation(0, 1, 0))
    # When
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    # Then
    assert n == Vector(0, 0.70711, -0.70711)


def test_commputing_the_normal_on_a_transformed_sphere():
    # Given
    s = Sphere()
    m = scaling(1, 0.5, 1) * rotation_z(pi / 5)
    s.set_transform(m)
    # When
    n = s.normal_at(Point(0, sqrt(2) / 2, -sqrt(2) / 2))
    # Then
    assert n == Vector(0, 0.97014, -0.24254)


def test_a_sphere_has_a_default_material():
    # Given
    s = Sphere()
    # When
    m = s.material
    # Then
    assert m == Material()


def test_a_sphere_may_be_assigned_a_material():
    # Given
    s = Sphere()
    m = Material()
    m.ambient = 1
    # When
    s.material = m
    # Then
    assert s.material == m
