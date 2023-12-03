from collections import defaultdict

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 4361
    part_two_test_solution = 467835

    def preprocess_input(self, lines):
        return np.array([list(l) for l in super().preprocess_input(lines)])

    def get_symbol(self, schematics, row, start, end):
        row_start = max(row - 1, 0)
        row_end = min(row + 1, schematics.shape[0] - 1)
        col_start = max(start - 1, 0)
        col_end = min(end + 1, schematics.shape[1] - 1)
        neighborhood = schematics[row_start : row_end + 1, col_start : col_end + 1]
        symbol = [s for s in neighborhood.flatten() if s != '.' and not s.isdigit()]
        if not symbol:
            return None
        symbol = symbol[0]
        indexes = np.where(neighborhood == symbol)
        return symbol, (indexes[0][0] + row_start, indexes[1][0] + col_start)

    def get_numbers(self, schematics):
        for row, line in enumerate(schematics):
            start = 0
            while start < len(line):
                if line[start].isdigit():
                    end = start
                    while end + 1 < len(line) and line[end + 1].isdigit():
                        end += 1
                    symbol = self.get_symbol(schematics, row, start, end)
                    if symbol:
                        yield int(''.join(line[start : end + 1])), symbol
                    start = end + 2
                else:
                    start += 1

    def part_one(self, schematics) -> int:
        return sum([n for n, s in self.get_numbers(schematics)])

    def part_two(self, schematics) -> int:
        gears = defaultdict(list)
        for n, (symbol, location) in self.get_numbers(schematics):
            if symbol == '*':
                gears[location].append(n)

        return sum([gear[0] * gear[1] for gear in gears.values() if len(gear) == 2])


if __name__ == '__main__':
    Level().run()
