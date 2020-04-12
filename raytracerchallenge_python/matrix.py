class Matrix:
    def __init__(self, *numbers):
        self._matrix = \
            [list(numbers[i:i+4]) for i in range(0, len(numbers), 4)]

    def at(self, row, col):
        return self._matrix[row][col]
