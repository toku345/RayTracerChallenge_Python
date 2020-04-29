class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object

    def prepare_computations(self, ray):
        point = ray.position(self.t)
        return Computations(t=self.t,
                            object=self.object,
                            point=point,
                            eyev=-ray.direction,
                            normalv=self.object.normal_at(point))


class Computations:
    def __init__(self, t, object, point, eyev, normalv):
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev
        self.normalv = normalv


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
