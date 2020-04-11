#!/usr/bin/env python3
from dataclasses import dataclass
from raytracerchallenge_python.tuple import Point, Vector


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
    # projectile starts one unit above the origin.
    # velocity is normalized to 1 unit/tick.
    p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normalize())

    # gravity -0.1 unit/tick, and wind is -0.01 unit/tick
    e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

    while p.position.y > 0:
        p = tick(e, p)
        print("[Projectile position] x: ", p.position.x,
              " y: ", p.position.y,
              " z: ", p.position.z)
