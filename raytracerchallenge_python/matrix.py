from math import sqrt, floor


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
        elements = []
        for row in range(4):
            for col in range(4):
                element = sum([self.at(row, 0) * other.at(0, col),
                               self.at(row, 1) * other.at(1, col),
                               self.at(row, 2) * other.at(2, col),
                               self.at(row, 3) * other.at(3, col)])
                elements.append(element)
        return Matrix(*elements)
