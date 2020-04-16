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
