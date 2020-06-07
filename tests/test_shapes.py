from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import (
    translation, scaling, rotation_z, rotation_y)
from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.group import Group
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.material import Material
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector

from math import pi, sqrt

import pytest


class MockShape(Shape):
    def local_intersect(self, ray):
        self.saved_ray = ray

    def local_normal_at(self, p):
        return Vector(p.x, p.y, p.z)


def test_the_default_transformation():
    # Given
    s = MockShape()
    # Then
    assert s.transform == identity_matrix()


def test_assigning_a_transformation():
    # Given
    s = MockShape()
    # When
    s.transform = translation(2, 3, 4)
    # Then
    assert s.transform == translation(2, 3, 4)


def test_the_default_material():
    # Given
    s = MockShape()
    # When
    m = s.material
    # Then
    assert m == Material()


def test_assigning_a_material():
    # Given
    s = MockShape()
    m = Material()
    m.ambient = 1
    # When
    s.material = m
    # Then
    assert s.material == m


def test_raise_exception_when_not_implement_local_instance():
    class BadShape(Shape):
        def local_normal_at(self, point):
            pass

    with pytest.raises(TypeError):
        BadShape()


def test_intersecting_a_scaled_shape_with_a_ray():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = MockShape()
    # When
    s.transform = scaling(2, 2, 2)
    _ = s.intersect(r)
    # Then
    assert s.saved_ray.origin == Point(0, 0, -2.5)
    assert s.saved_ray.direction == Vector(0, 0, 0.5)


def test_intersecting_a_translated_shape_with_a_ray():
    # Given
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = MockShape()
    # When
    s.transform = translation(5, 0, 0)
    _ = s.intersect(r)
    # Then
    assert s.saved_ray.origin == Point(-5, 0, -5)
    assert s.saved_ray.direction == Vector(0, 0, 1)


def test_raise_exception_when_not_implement_local_normal_at():
    class BadShape(Shape):
        def local_intersect(self, ray):
            pass

    with pytest.raises(TypeError):
        BadShape()


def test_computing_the_normal_on_a_translated_shape():
    # Given
    s = MockShape()
    # When
    s.transform = translation(0, 1, 0)
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    # Then
    assert n == Vector(0, 0.70711, -0.70711)


def test_computing_the_normal_on_a_transformed_shape():
    # Given
    s = MockShape()
    m = scaling(1, 0.5, 1) * rotation_z(pi / 5)
    # When
    s.transform = m
    n = s.normal_at(Point(0, sqrt(2) / 2, -sqrt(2) / 2))
    # Then
    assert n == Vector(0, 0.97014, -0.24254)


def test_a_shape_has_a_parent_shape():
    # Given
    s = MockShape()
    # Then
    assert s.parent is None


def test_converting_a_point_from_world_to_object_space():
    # Given
    g1 = Group()
    g1.transform = rotation_y(pi / 2)
    g2 = Group()
    g2.transform = scaling(2, 2, 2)
    g1.add_child(g2)
    s = Sphere()
    s.transform = translation(5, 0, 0)
    g2.add_child(s)
    # When
    p = s.world_to_object(Point(-2, 0, -10))
    # Then
    assert p == Point(0, 0, -1)


def test_converting_a_normal_from_object_to_world_space():
    # Given
    g1 = Group()
    g1.transform = rotation_y(pi / 2)
    g2 = Group()
    g2.transform = scaling(1, 2, 3)
    g1.add_child(g2)
    s = Sphere()
    s.transform = translation(5, 0, 0)
    g2.add_child(s)
    # When
    n = s.normal_to_world(Vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
    # Then
    assert n == Vector(0.28571, 0.42857, -0.85714)


def test_finding_the_normal_on_a_child_object():
    # Given
    g1 = Group()
    g1.transform = rotation_y(pi / 2)
    g2 = Group()
    g2.transform = scaling(1, 2, 3)
    g1.add_child(g2)
    s = Sphere()
    s.transform = translation(5, 0, 0)
    g2.add_child(s)
    # When
    n = s.normal_at(Point(1.7321, 1.1547, -5.5774))
    # Then
    assert n == Vector(0.2857, 0.42854, -0.85716)
