from raytracerchallenge_python.matrix import identity_matrix
from raytracerchallenge_python.tuple import Point
from raytracerchallenge_python.ray import Ray
from raytracerchallenge_python.canvas import Canvas

from math import tan


class Camera:
    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = identity_matrix()

        self._calc_pixel_size()

    def _calc_pixel_size(self):
        half_view = tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize

    def ray_for_pixel(self, px, py):
        # the offsets from the edge of the canvas to the pixel's center
        xoffset = (px + 0.5) * self.pixel_size
        yoffset = (py + 0.5) * self.pixel_size

        # the untransformed coordinates of the pixel in world space.
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        pixel = self.transform.inverse() * Point(world_x, world_y, -1)
        origin = self.transform.inverse() * Point(0, 0, 0)
        direction = (pixel - origin).normalize()

        return Ray(origin, direction)

    def render(self, world):
        image = Canvas(self.hsize, self.vsize)
        for y in range(self.vsize):
            for x in range(self.hsize):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.write_pixel(x, y, color)
        return image
