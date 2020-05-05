from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.transformations import translation, scaling
from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.material import Material
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.tuple import Point, Vector

import pytest


class MockShape(Shape):
    def local_intersect(self):
        pass


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
