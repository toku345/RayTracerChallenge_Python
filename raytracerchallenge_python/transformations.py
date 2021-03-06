from raytracerchallenge_python.matrix import Matrix

from math import sin, cos


def translation(x, y, z):
    return Matrix(1, 0, 0, x,
                  0, 1, 0, y,
                  0, 0, 1, z,
                  0, 0, 0, 1)


def scaling(x, y, z):
    return Matrix(x, 0, 0, 0,
                  0, y, 0, 0,
                  0, 0, z, 0,
                  0, 0, 0, 1)


def rotation_x(radian):
    return Matrix(1, 0, 0, 0,
                  0, cos(radian), -sin(radian), 0,
                  0, sin(radian), cos(radian), 0,
                  0, 0, 0, 1)


def rotation_y(radian):
    return Matrix(cos(radian), 0, sin(radian), 0,
                  0, 1, 0, 0,
                  -sin(radian), 0, cos(radian), 0,
                  0, 0, 0, 1)


def rotation_z(radian):
    return Matrix(cos(radian), -sin(radian), 0, 0,
                  sin(radian), cos(radian), 0, 0,
                  0, 0, 1, 0,
                  0, 0, 0, 1)


def shearing(xy, xz, yx, yz, zx, zy):
    return Matrix(1, xy, xz, 0,
                  yx, 1, yz, 0,
                  zx, zy, 1, 0,
                  0, 0, 0, 1)


def view_transform(f, to, up):
    forward = (to - f).normalize()
    upn = up.normalize()
    left = forward.cross(upn)
    true_up = left.cross(forward)
    orientation = Matrix(left.x, left.y, left.z, 0,
                         true_up.x, true_up.y, true_up.z, 0,
                         -forward.x, -forward.y, -forward.z, 0,
                         0, 0, 0, 1)
    return orientation * translation(-f.x, -f.y, -f.z)
