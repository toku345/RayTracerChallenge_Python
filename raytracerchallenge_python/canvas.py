from raytracerchallenge_python.tuple import Color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = \
            [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]
