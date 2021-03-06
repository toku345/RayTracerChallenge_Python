from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.tuple import Point, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.transformations import scaling
from raytracerchallenge_python.intersection import Intersections
from raytracerchallenge_python.ray import Ray

from math import sqrt


class World:
    def __init__(self):
        self.objects = []
        self.light = None

    def intersect_world(self, ray):
        xs = [x
              for object in self.objects
              for x in object.intersect(ray)]
        return Intersections(*xs)

    def shade_hit(self, comps, remaining=4):
        shadowed = self.is_shadowed(comps.over_point)
        surface = comps.object.material.lighting(comps.object,
                                                 self.light,
                                                 comps.over_point,
                                                 comps.eyev,
                                                 comps.normalv,
                                                 shadowed)
        reflected = self.reflected_color(comps, remaining)
        refracted = self.refracted_color(comps, remaining)

        material = comps.object.material
        if material.reflective > 0 and material.transparency > 0:
            reflectance = comps.schlick()
            return surface + reflected * reflectance + \
                refracted * (1 - reflectance)
        else:
            return surface + reflected + refracted

    def color_at(self, ray, remaining=4):
        xs = self.intersect_world(ray)
        if not xs:
            return Color(0, 0, 0)

        hit = xs.hit()
        if not hit:
            return Color(0, 0, 0)

        comps = hit.prepare_computations(ray, xs)
        return self.shade_hit(comps, remaining)

    def is_shadowed(self, point):
        v = self.light.position - point
        distance = v.magnitude()
        direction = v.normalize()

        r = Ray(point, direction)
        intersections = self.intersect_world(r)

        h = intersections.hit()
        if h and h.t < distance:
            return True
        else:
            return False

    def reflected_color(self, comps, remaining=4):
        if comps.object.material.reflective == 0 or remaining <= 0:
            return Color(0, 0, 0)
        reflect_ray = Ray(comps.over_point, comps.reflectv)
        color = self.color_at(reflect_ray, remaining - 1)

        return color * comps.object.material.reflective

    def refracted_color(self, comps, remaining):
        if remaining == 0 or comps.object.material.transparency == 0:
            return Color(0, 0, 0)

        n_ratio = comps.n1 / comps.n2
        cos_i = comps.eyev.dot(comps.normalv)
        sin2_t = n_ratio ** 2 * (1 - cos_i ** 2)
        if sin2_t > 1:
            return Color(0, 0, 0)

        cos_t = sqrt(1.0 - sin2_t)
        direction = comps.normalv * \
            (n_ratio * cos_i - cos_t) - comps.eyev * n_ratio

        refracted_ray = Ray(comps.under_point, direction)
        color = self.color_at(refracted_ray, remaining - 1)

        return color * comps.object.material.transparency


def default_world():
    light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.transform = scaling(0.5, 0.5, 0.5)

    w = World()
    w.light = light
    w.objects = [s1, s2]
    return w
