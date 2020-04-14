from math import sqrt, floor
from raytracerchallenge_python.tuple import Tuple


class Matrix:
    def __init__(self, *elements):
        size = floor(sqrt(len(elements)))
        self._matrix = \
            [list(elements[i:i+size]) for i in range(0, len(elements), size)]

    def at(self, row, col):
        return self._matrix[row][col]

    def transpose(self):
        elements = []
        for row in range(4):
            for col in range(4):
                elements.append(self.at(col, row))
        return Matrix(*elements)

    def determinant(self):
        return self.at(0, 0) * self.at(1, 1) - self.at(0, 1) * self.at(1, 0)

    def submatrix(self, row, col):
        size = len(self._matrix)
        elements = []
        for row_index in range(size):
            if row_index == row:
                continue
            for col_index in range(size):
                if col_index == col:
                    continue
                elements.append(self.at(row_index, col_index))
        return Matrix(*elements)

    def minor(self, row, col):
        return self.submatrix(row, col).determinant()

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, Matrix):
            return False

        return self._matrix == other._matrix

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self._multiply_matices(other)
        else:
            return self._multiply_by_tuple(other)

    def _multiply_matices(self, other):
        elements = []
        for row in range(4):
            for col in range(4):
                element = sum([self.at(row, 0) * other.at(0, col),
                               self.at(row, 1) * other.at(1, col),
                               self.at(row, 2) * other.at(2, col),
                               self.at(row, 3) * other.at(3, col)])
                elements.append(element)
        return Matrix(*elements)

    def _multiply_by_tuple(self, other):
        other_list = other.to_list()
        elements = []
        for row in range(4):
            element = sum([self.at(row, 0) * other_list[0],
                           self.at(row, 1) * other_list[1],
                           self.at(row, 2) * other_list[2],
                           self.at(row, 3) * other_list[3]])
            elements.append(element)
        return Tuple(*elements)


def identity_matrix():
    return Matrix(1, 0, 0, 0,
                  0, 1, 0, 0,
                  0, 0, 1, 0,
                  0, 0, 0, 1)
