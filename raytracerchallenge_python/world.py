from raytracerchallenge_python.point_light import PointLight
from raytracerchallenge_python.tuple import Point, Color
from raytracerchallenge_python.sphere import Sphere
from raytracerchallenge_python.transformations import scaling
from raytracerchallenge_python.intersection import Intersections


class World:
    def __init__(self):
        self.objects = []
        self.light = None

    def intersect_world(self, ray):
        xs = [x
              for object in self.objects
              for x in object.intersect(ray)]
        return Intersections(*xs)

    def shade_hit(self, comps):
        return comps.object.material.lighting(self.light,
                                              comps.point,
                                              comps.eyev,
                                              comps.normalv)

    def color_at(self, ray):
        xs = self.intersect_world(ray)
        if not xs:
            return Color(0, 0, 0)
        hit = xs.hit()
        comps = hit.prepare_computations(ray)
        return self.shade_hit(comps)


def default_world():
    light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.set_transform(scaling(0.5, 0.5, 0.5))

    w = World()
    w.light = light
    w.objects = [s1, s2]
    return w
