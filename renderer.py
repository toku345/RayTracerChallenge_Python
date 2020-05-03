#!/usr/bin/env python3
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.material import Material
from raytracerchallenge_python.tuple import Color, Point, Vector
from raytracerchallenge_python.camera import Camera
from raytracerchallenge_python.world import World
from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.transformations import (
    scaling, view_transform, translation, rotation_x, rotation_y)

from math import pi

if __name__ == "__main__":
    floor = Sphere()
    floor.transform = scaling(10, 0.01, 10)
    floor.material = Material()
    floor.material.color = Color(1, 0.9, 0.9)
    floor.material.specular = 0

    left_wall = Sphere()
    left_wall.transform = \
        translation(0, 0, 5) * rotation_y(-pi / 4) * \
        rotation_x(pi / 2) * scaling(10, 0.01, 10)
    left_wall.material = floor.material

    right_wall = Sphere()
    right_wall.transform = \
        translation(0, 0, 5) * rotation_y(pi / 4) * \
        rotation_x(pi / 2) * scaling(10, 0.01, 10)
    right_wall.material = floor.material

    middle = Sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    right = Sphere()
    right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
    right.material = Material()
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3

    left = Sphere()
    left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    world = World()
    world.objects = [floor, left_wall, right_wall, middle, right, left]
    world.light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))

    camera = Camera(100, 50, pi / 3)
    camera.transform = view_transform(Point(0, 1.5, -5),
                                      Point(0, 1, 0),
                                      Vector(0, 1, 0))
    print(camera.render(world).to_ppm())
