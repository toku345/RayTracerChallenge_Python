from raytracerchallenge_python.cylinder import Cylinder
from raytracerchallenge_python.tuple import Point, Vector
from raytracerchallenge_python.ray import Ray


def test_a_ray_misses_a_cylinder():
    EXAMPLES = [
        # origin          direction
        (Point(1, 0, 0),  Vector(0, 1, 0)),
        (Point(0, 0, 0),  Vector(0, 1, 0)),
        (Point(0, 0, -5), Vector(1, 1, 1)),
    ]
    for origin, direction in EXAMPLES:
        # Given
        cyl = Cylinder()
        dir = direction.normalize()
        r = Ray(origin, dir)
        # When
        xs = cyl.local_intersect(r)
        # Then
        assert len(xs) == 0
