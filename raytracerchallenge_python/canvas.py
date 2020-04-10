from raytracerchallenge_python.tuple import Color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = \
            [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def write_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def pixel_at(self, x, y):
        return self.pixels[y][x]
