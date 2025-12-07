from math import prod
from pathlib import Path

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 4277556
    part_two_test_solution = 3263827

    strip_only_new_lines = True

    def preprocess_input(self, lines):
        lines = [list(line) for line in lines]
        width = max(len(line) for line in lines)
        return np.array([line + [" "] * (width - len(line)) for line in lines])

    def part_one(self, grid) -> int:
        numbers = np.array([list(map(int, ''.join(line).split())) for line in grid[:-1]])
        operations = ''.join(grid[-1]).split()

        s = 0
        for column, operation in enumerate(operations):
            if operation == '+':
                s += numbers[:, column].sum()
            elif operation == '*':
                s += numbers[:, column].prod()
        return s

    def part_two(self, grid) -> int:
        s = 0
        numbers = []
        for column in grid.T[::-1]:
            number = ''.join(column[:-1]).strip()
            if not number:
                continue
            numbers += [int(number)]
            if operation := column[-1].strip():
                if operation == '+':
                    s += sum(numbers)
                elif operation == '*':
                    s += prod(numbers)
                numbers = []
        return s


if __name__ == '__main__':
    Level().run()
