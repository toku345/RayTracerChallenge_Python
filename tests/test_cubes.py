from raytracerchallenge_python.cube import Cube
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.ray import Ray


def test_a_ray_intersects_a_cube():
    EXAMPLES = [
        # origin         , direction      , t1, t2
        (Point(5, 0.5, 0), Vector(-1, 0, 0), 4, 6),  # +x
        (Point(-5, 0.5, 0), Vector(1, 0, 0), 4, 6),  # -x
        (Point(0.5, 5, 0), Vector(0, -1, 0), 4, 6),  # +y
        (Point(0.5, -5, 0), Vector(0, 1, 0), 4, 6),  # -y
        (Point(0.5, 0, 5), Vector(0, 0, -1), 4, 6),  # +z
        (Point(0.5, 0, -5), Vector(0, 0, 1), 4, 6),  # -z
        (Point(0, 0.5, 0), Vector(0, 0, 1), -1, 1),  # inside
    ]
    for origin, direction, t1, t2 in EXAMPLES:
        # Given
        c = Cube()
        r = Ray(origin, direction)
        # When
        xs = c.local_intersect(r)
        # Then
        assert len(xs) == 2
        assert xs[0].t == t1
        assert xs[1].t == t2


def test_a_ray_misses_a_cube():
    EXAMPLES = [
        # origin,         direction
        (Point(-2, 0, 0), Vector(0.2673, 0.5345, 0.8018)),
        (Point(0, -2, 0), Vector(0.8018, 0.2673, 0.5345)),
        (Point(0, 0, -2), Vector(0.5345, 0.8018, 0.2673)),
        (Point(2, 0, 2),  Vector(0, 0, -1)),
        (Point(0, 2, 2),  Vector(0, -1, 0)),
        (Point(2, 2, 0),  Vector(-1, 0, 0)),
    ]
    for origin, direction in EXAMPLES:
        # Given
        c = Cube()
        r = Ray(origin, direction)
        # When
        xs = c.local_intersect(r)
        # Then
        assert len(xs) == 0


def test_the_normal_on_the_surface_of_a_cube():
    EXAMPLES = [
        # point,               normal
        (Point(1, 0.5, -0.8),  Vector(1, 0, 0)),
        (Point(-1, -0.2, 0.9), Vector(-1, 0, 0)),
        (Point(-0.4, 1, -0.1), Vector(0, 1, 0)),
        (Point(0.3, -1, -0.7), Vector(0, -1, 0)),
        (Point(-0.6, 0.3, 1),  Vector(0, 0, 1)),
        (Point(0.4, 0.4, -1),  Vector(0, 0, -1)),
        (Point(1, 1, 1),       Vector(1, 0, 0)),
        (Point(-1, -1, -1),    Vector(-1, 0, 0)),
    ]
    for point, normal in EXAMPLES:
        # Given
        c = Cube()
        p = point
        # When
        n = c.local_normal_at(p)
        # Then
        assert normal == n
