class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def transform(self, matrix):
        return Ray(matrix * self.origin, matrix * self.direction)
