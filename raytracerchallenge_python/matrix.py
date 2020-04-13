from math import sqrt, floor
from raytracerchallenge_python.tuple import Tuple


class Matrix:
    def __init__(self, *elements):
        size = floor(sqrt(len(elements)))
        self._matrix = \
            [list(elements[i:i+size]) for i in range(0, len(elements), size)]

    def at(self, row, col):
        return self._matrix[row][col]

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
