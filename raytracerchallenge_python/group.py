from raytracerchallenge_python.matrix import identity_matrix


class Group:
    def __init__(self):
        self.transform = identity_matrix()
        self.children = []

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def add_child(self, shape):
        self.children.append(shape)
        shape.parent = self
