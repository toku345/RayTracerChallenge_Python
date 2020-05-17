from raytracerchallenge_python.helpers import EPSILON


class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object

    def prepare_computations(self, ray, xs=[]):
        comps = Computations(t=self.t,
                             object=self.object,
                             point=ray.position(self.t),
                             eyev=-ray.direction)

        containers = []
        for i in xs:
            if i == self:
                if len(containers) < 1:
                    comps.n1 = 1.0
                else:
                    comps.n1 = containers[-1].material.refractive_index

            if i.object in containers:
                containers.remove(i.object)
            else:
                containers.append(i.object)

            if i == self:
                if len(containers) < 1:
                    comps.n2 = 1.0
                else:
                    comps.n2 = containers[-1].material.refractive_index

                break

        return comps


class Computations:
    def __init__(self, t, object, point, eyev):
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev

        normalv = self.object.normal_at(self.point)
        if normalv.dot(self.eyev) < 0:
            self.inside = True
            self.normalv = -normalv
        else:
            self.inside = False
            self.normalv = normalv

        self.over_point = self.point + self.normalv * EPSILON
        self.under_point = self.point - self.normalv * EPSILON

        self.reflectv = (-eyev).reflect(self.normalv)

    def schlick(self):
        cos = self.eyev.dot(self.normalv)

        if self.n1 > self.n2:
            n = self.n1 / self.n2
            sin2_t = n ** 2 * (1.0 - cos ** 2)
            if sin2_t > 1.0:
                return 1.0
        return 0.0


class Intersections:
    def __init__(self, *intersections):
        self.sorted_intersections = sorted(intersections, key=lambda i: i.t)

    def __len__(self):
        return len(self.sorted_intersections)

    def __getitem__(self, key):
        return self.sorted_intersections[key]

    def hit(self):
        xs = list(filter(lambda x: x.t >= 0, self.sorted_intersections))

        if len(xs) < 1:
            return None

        return xs[0]
