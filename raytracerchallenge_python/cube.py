from raytracerchallenge_python.shape import Shape
from raytracerchallenge_python.intersection import Intersection
from raytracerchallenge_python.tuple import Vector

from raytracerchallenge_python.helpers import EPSILON


class Cube(Shape):

    def local_normal_at(self, point):
        maxc = max(abs(point.x), abs(point.y), abs(point.z))

        if maxc == abs(point.x):
            return Vector(point.x, 0, 0)
        elif maxc == abs(point.y):
            return Vector(0, point.y, 0)
        else:
            return Vector(0, 0, point.z)

    def local_intersect(self, ray):
        def check_axis(origin, direction):
            tmin_numerator = (-1 - origin)
            tmax_numerator = (1 - origin)

            if abs(direction) >= EPSILON:
                tmin = tmin_numerator / direction
                tmax = tmax_numerator / direction
            else:
                tmin = tmin_numerator * float('inf')
                tmax = tmax_numerator * float('inf')

            if tmin > tmax:
                tmin, tmax = tmax, tmin

            return (tmin, tmax)

        xtmin, xtmax = check_axis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = check_axis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = check_axis(ray.origin.z, ray.direction.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        if tmin > tmax:
            return ()
        else:
            return (Intersection(tmin, self), Intersection(tmax, self))
