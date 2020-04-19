#!/usr/bin/env python3
from raytracerchallenge_python.tuple import Point, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.intersection import Intersections
from raytracerchallenge_python.canvas import Canvas

# from raytracerchallenge_python.transformations import (
#     scaling, rotation_z, shearing)
# from math import pi

if __name__ == "__main__":
    ray_origin = Point(0, 0, -5)
    wall_z = 10
    wall_size = 7.0
    canvas_pixcels = 100
    pixel_size = wall_size / canvas_pixcels
    half = wall_size / 2

    canvas = Canvas(canvas_pixcels, canvas_pixcels)
    color = Color(1, 0, 0)
    shape = Sphere()

    # # shrink it along the y axis
    # shape.set_transform(scaling(1, 0.5, 1))

    # # shrink it along the x axis
    # shape.set_transform(scaling(0.5, 1, 1))

    # # shrink it, and rotate it!
    # shape.set_transform(rotation_z(pi / 4) * scaling(0.5, 1, 1))

    # shrink it, and skew it!
    # shape.set_transform(shearing(1, 0, 0, 0, 0, 0) * scaling(0.5, 1, 1))

    # for each row of pixels in the canvas
    for y in range(canvas_pixcels):
        # compute the world y coordinate (top = +half, bottom = -half)
        world_y = half - pixel_size * y

        for x in range(canvas_pixcels):
            # compute the world x coordinate (left = -half, right = half)
            world_x = -half + pixel_size * x

            # describe the point on the wall that the ray will target
            position = Point(world_x, world_y, wall_z)

            r = Ray(ray_origin, (position - ray_origin).normalize())
            xs = shape.intersect(r)

            if isinstance(xs, Intersections):
                canvas.write_pixel(x, y, color)

    print(canvas.to_ppm())
