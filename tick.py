#!/usr/bin/env python3
from dataclasses import dataclass
from math import floor

from raytracerchallenge_python.tuple import Point, Vector, Color
from raytracerchallenge_python.canvas import Canvas


@dataclass
class Projectile:
    position: Point
    velocity: Vector


@dataclass
class Environment:
    gravity: Vector
    wind: Vector


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


if __name__ == "__main__":
    start = Point(0, 1, 0)
    velocity = Vector(1, 1.8, 0).normalize() * 11.25
    p = Projectile(start, velocity)

    gravity = Vector(0, -0.1, 0)
    wind = Vector(-0.01, 0, 0)
    e = Environment(gravity, wind)

    width = 900
    height = 550
    c = Canvas(width, height)

    color = Color(1, 0, 0)

    while p.position.y > 0:
        p = tick(e, p)
        x = floor(p.position.x)
        y = height - floor(p.position.y)
        if 0 <= x < width and 0 <= y < height:
            c.write_pixel(x, y, color)

    print(c.to_ppm())
