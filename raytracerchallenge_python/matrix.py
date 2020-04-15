from math import sqrt, floor

from raytracerchallenge_python.tuple import Tuple
from raytracerchallenge_python.helpers import equal


class NonInvertibleMatrixError(Exception):
    def __init__(self):
        self.expression = 'Non Invertible Matrix!'
        self.text = 'Non Invertible Matrix!'


class Matrix:
    def __init__(self, *elements):
        self.size = floor(sqrt(len(elements)))
        self._matrix = \
            [list(elements[i:i+self.size])
             for i in range(0, len(elements), self.size)]

    def at(self, row, col):
        return self._matrix[row][col]

    def transpose(self):
        elements = []
        for row in range(4):
            for col in range(4):
                elements.append(self.at(col, row))
        return Matrix(*elements)

    def determinant(self):
        if self.size == 2:
            return self.at(0, 0) * self.at(1, 1) - \
                self.at(0, 1) * self.at(1, 0)
        else:
            return sum([self.at(0, col) * self.cofactor(0, col)
                        for col in range(self.size)])

    def submatrix(self, row, col):
        elements = []
        for row_index in range(self.size):
            if row_index == row:
                continue
            for col_index in range(self.size):
                if col_index == col:
                    continue
                elements.append(self.at(row_index, col_index))
        return Matrix(*elements)

    def minor(self, row, col):
        return self.submatrix(row, col).determinant()

    def cofactor(self, row, col):
        if (row + col) % 2 == 0:
            return self.minor(row, col)
        else:
            return -self.minor(row, col)

    def is_invertible(self):
        return self.determinant() != 0

    def inverse(self):
        if not self.is_invertible():
            raise NonInvertibleMatrixError

        det = self.determinant()
        elements = []
        for row in range(self.size):
            for col in range(self.size):
                c = self.cofactor(row, col)
                elements.append(c / det)

        return Matrix(*elements).transpose()

    def __repr__(self):
        lines = []
        for row in range(self.size):
            lines.append(" | ".join([str(self.at(row, col))
                                     for col in range(self.size)]))
        return "\n".join(lines)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, Matrix):
            return False

        return all([equal(self.at(r, c), other.at(r, c))
                    for r in range(self.size)
                    for c in range(self.size)])

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
