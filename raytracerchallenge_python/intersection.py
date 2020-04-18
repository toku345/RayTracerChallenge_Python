class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object


class Intersections:
    def __init__(self, *intersections):
        self.intersections = intersections

    def __len__(self):
        return len(self.intersections)

    def __getitem__(self, key):
        return self.intersections[key]
