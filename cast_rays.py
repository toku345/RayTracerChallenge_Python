#!/usr/bin/env python3
from raytracerchallenge_python.tuple import Point, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.intersection import Intersections
from raytracerchallenge_python.canvas import Canvas
from raytracerchallenge_python.material import Material
from raytracerchallenge_python.point_light import PointLight

if __name__ == "__main__":
    ray_origin = Point(0, 0, -5)
    wall_z = 10
    wall_size = 7.0
    canvas_pixcels = 100
    pixel_size = wall_size / canvas_pixcels
    half = wall_size / 2

    canvas = Canvas(canvas_pixcels, canvas_pixcels)
    shape = Sphere()
    shape.material = Material()
    shape.material.color = Color(1, 0.2, 1)

    light_position = Point(-10, 10, -10)
    light_color = Color(1, 1, 1)
    light = PointLight(light_position, light_color)

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
                hit = xs[0]
                point = r.position(hit.t)
                normal = hit.object.normal_at(point)
                eye = -r.direction
                color = hit.object.material.lighting(light, point, eye, normal)

                canvas.write_pixel(x, y, color)

    print(canvas.to_ppm())
