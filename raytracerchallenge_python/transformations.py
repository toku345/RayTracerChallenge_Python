from raytracerchallenge_python.matrix import Matrix


def translation(x, y, z):
    return Matrix(1, 0, 0, x,
                  0, 1, 0, y,
                  0, 0, 1, z,
                  0, 0, 0, 1)
