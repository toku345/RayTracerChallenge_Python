from math import sqrt, floor


class Matrix:
    def __init__(self, *numbers):
        size = floor(sqrt(len(numbers)))
        self._matrix = \
            [list(numbers[i:i+size]) for i in range(0, len(numbers), size)]

    def at(self, row, col):
        return self._matrix[row][col]
