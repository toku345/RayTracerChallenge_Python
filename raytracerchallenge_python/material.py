from raytracerchallenge_python.tuple import Color


class Material:
    def __init__(self):
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __eq__(self, other):
        return all([self.color == other.color,
                    self.ambient == other.ambient,
                    self.diffuse == other.diffuse,
                    self.specular == other.specular,
                    self.shininess == other.shininess])
