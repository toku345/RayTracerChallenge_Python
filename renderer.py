#!/usr/bin/env python3
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.plane import Plane
from raytracerchallenge_python.material import Material
from raytracerchallenge_python.tuple import Color, Point, Vector
from raytracerchallenge_python.camera import Camera
from raytracerchallenge_python.world import World
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.transformations import (
    scaling, view_transform, translation)
from raytracerchallenge_python.stripe_pattern import StripePattern

from math import pi

if __name__ == "__main__":
    pattern = StripePattern(Color(1, 0, 0), Color(1, 1, 1))

    floor = Plane()
    floor.material = Material()
    # floor.material.color = Color(1, 0.9, 0.9)
    floor.material.pattern = pattern

    middle = Sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    middle.material = Material()
    # middle.material.color = Color(0.1, 1, 0.5)
    middle.material.pattern = pattern
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    right = Sphere()
    right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
    right.material = Material()
    # right.material.color = Color(0.5, 1, 0.1)
    right.material.pattern = pattern
    right.material.diffuse = 0.7
    right.material.specular = 0.3

    left = Sphere()
    left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
    left.material = Material()
    # left.material.color = Color(1, 0.8, 0.1)
    left.material.pattern = pattern
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    world = World()
    world.objects = [floor, middle, right, left]
    world.light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))

    camera = Camera(100, 50, pi / 3)
    camera.transform = view_transform(Point(0, 1.5, -5),
                                      Point(0, 1, 0),
                                      Vector(0, 1, 0))

    canvas = camera.render(world)
    print(canvas.to_ppm())
