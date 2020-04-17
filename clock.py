#!/usr/bin/env python3
from raytracerchallenge_python.tuple import Point, Color
from raytracerchallenge_python.canvas import Canvas
from raytracerchallenge_python.transformations import rotation_y

from math import floor, pi


if __name__ == "__main__":
    WIDTH = HEIGHT = 100
    COLOR = Color(1, 0, 0)

    c = Canvas(WIDTH, HEIGHT)

    twelve = Point(0, 0, 1)
    for hour in range(12):
        p = rotation_y((pi / 6) * hour) * twelve
        x = floor(WIDTH / 2 + (3 / 8 * WIDTH) * p.x)
        y = floor(HEIGHT / 2 - (3 / 8 * HEIGHT) * p.z)
        c.write_pixel(x, y, COLOR)

    print(c.to_ppm())
