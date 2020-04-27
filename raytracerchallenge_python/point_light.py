class PointLight:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def __eq__(self, other):
        return all([self.position == other.position,
                    self.intensity == other.intensity])
