from raytracerchallenge_python.matrix import identity_matrix


class Group:
    def __init__(self):
        self.transform = identity_matrix()
        self.children = []

    def __len__(self):
        return len(self.children)
