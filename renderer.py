#!/usr/bin/env python3
from math import pi
from raytracerchallenge_python.gradient_pattern import GradientPattern
from raytracerchallenge_python.transformations import (
    scaling, view_transform, translation, rotation_y, rotation_x)
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.world import World
from raytracerchallenge_python.camera import Camera
from raytracerchallenge_python.tuple import Color, Point, Vector
from raytracerchallenge_python.material import Material
from raytracerchallenge_python.sphere import Sphere, glass_sphere
from raytracerchallenge_python.plane import Plane
from raytracerchallenge_python.cube import Cube
# from raytracerchallenge_python.stripe_pattern import StripePattern
# from raytracerchallenge_python.checkers_pattern import CheckersPattern
# from raytracerchallenge_python.ring_pattern import RingPattern


if __name__ == "__main__":
    # pattern = StripePattern(Color(1, 0, 0), Color(1, 1, 1))
    # pattern = CheckersPattern(Color(1, 0, 0), Color(1, 1, 1))
    pattern = GradientPattern(Color(1, 0, 0), Color(1, 1, 1))
    # pattern = RingPattern(Color(1, 0, 0), Color(1, 1, 1))
    pattern.transform = scaling(0.2, 0.2, 0.2)

    floor = Plane()
    floor.material = Material()
    floor.material.color = Color(1, 0.9, 0.9)
    # floor.material.pattern = pattern

    backdrop = Plane()
    backdrop.transform = \
        rotation_y(pi / 3) * translation(0, 0, 5) * rotation_x(pi / 2)

    backdrop2 = Plane()
    backdrop2.transform = \
        rotation_y(-pi / 3) * translation(0, 0, 5) * rotation_x(pi / 2)

    middle = Sphere()
    # middle = glass_sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    # middle.reflective = 1.0
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    # middle.material.pattern = pattern
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    # middle.material.reflective = 1.0

    # right = Sphere()
    right = glass_sphere()
    right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
    right.material.reflective = 0.9
    right.material.transparency = 0.9
    right.material.refractive_index = 1.5
    # right.material = Material()
    # right.material.color = Color(0.5, 1, 0.1)
    # right.material.pattern = pattern
    # right.material.diffuse = 0.7
    # right.material.specular = 0.3
    right.material.diffuse = 0
    right.material.specular = 0

    left = Sphere()
    left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    # left.material.pattern = pattern
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    cube = Cube()
    cube.transform = translation(
        0, 0, 1) * rotation_y(pi / 4) * scaling(0.5, 0.5, 0.5)

    world = World()
    # world.objects = [floor, backdrop, backdrop2, middle, right, left]
    world.objects = [cube]
    world.light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))

    camera = Camera(100, 50, pi / 3)
    camera.transform = view_transform(Point(0, 1.5, -5),
                                      Point(0, 1, 0),
                                      Vector(0, 1, 0))

    canvas = camera.render(world)
    print(canvas.to_ppm())
