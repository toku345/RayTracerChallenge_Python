from raytracerchallenge_python.tuple import Color
from decimal import Decimal


class Canvas:
    MAXIMUM_COLOR_VALUE = 255

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = \
            [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def write_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def pixel_at(self, x, y):
        return self.pixels[y][x]

    def to_ppm(self):
        headers = ["P3",
                   f"{self.width} {self.height}",
                   str(self.MAXIMUM_COLOR_VALUE)]

        def convert(value):
            if value < 0:
                value = 0
            elif value > 1:
                value = 1
            color_value = value * self.MAXIMUM_COLOR_VALUE
            return Decimal(color_value).quantize(Decimal('1.'))

        pixel_data = []
        for xs in self.pixels:
            line = []
            for color in xs:
                r = convert(color.red)
                g = convert(color.green)
                b = convert(color.blue)
                line.append(f"{r} {g} {b}")
            pixel_data.append(" ".join(line))

        return "\n".join(headers) + "\n" + "\n".join(pixel_data)
