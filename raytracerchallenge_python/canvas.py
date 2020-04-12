from raytracerchallenge_python.tuple import Color


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
        lines = ["P3",
                 f"{self.width} {self.height}",
                 str(self.MAXIMUM_COLOR_VALUE)]

        def split_line(line):
            split_index = 70
            while line[split_index] != " ":
                split_index -= 1
            return [line[:split_index], line[split_index+1:]]

        for xs in self.pixels:
            ppm_pixels = \
                [color.ppm_pixel_str(self.MAXIMUM_COLOR_VALUE) for color in xs]
            line = " ".join(ppm_pixels)
            if len(line) > 70:
                lines += split_line(line)
            else:
                lines.append(line)

        return "\n".join(lines) + "\n"
