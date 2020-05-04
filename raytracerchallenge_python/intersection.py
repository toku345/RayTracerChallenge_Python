from raytracerchallenge_python.helpers import EPSILON


class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object

    def prepare_computations(self, ray):
        return Computations(t=self.t,
                            object=self.object,
                            point=ray.position(self.t),
                            eyev=-ray.direction)


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

        # after computing and (if appropriate) negating
        # the normal vector...
        self.over_point = self.point + self.normalv * EPSILON


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
