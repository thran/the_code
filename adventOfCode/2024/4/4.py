import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 18
    part_two_test_solution = 9

    WORD = 'XMAS'

    def preprocess_input(self, lines):
        rows = []
        for line in lines:
            rows.append([self.WORD.index(s) for s in line])
        return np.array(rows)

    def part_one(self, sky: np.array) -> int:
        founds = 0
        solutions = [(0, 1, 2, 3), (3, 2, 1, 0)]
        for i in range(sky.shape[0]):
            for j in range(sky.shape[1]):
                square = sky[i : i + 4, j : j + 4]
                for candidate in (
                    square[0],
                    square[:, 0],
                    square.diagonal(),
                    np.fliplr(square).diagonal(),
                ):
                    if len(candidate) < 4:
                        continue
                    if tuple(candidate) in solutions:
                        founds += 1
        return founds

    def part_two(self, sky) -> int:
        founds = 0

        corners = [1, 1, 3, 3]
        corner_possibilities = []
        for _ in range(4):
            corner_possibilities.append(tuple(corners))
            corners = corners[1:] + [corners[0]]
        for i in range(sky.shape[0] - 2):
            for j in range(sky.shape[1] - 2):
                square = sky[i : i + 3, j : j + 3]
                if square[1, 1] != 2:
                    continue
                corners = (square[0, 0], square[2, 0], square[2, 2], square[0, 2])
                if corners in corner_possibilities:
                    founds += 1
        return founds


if __name__ == '__main__':
    Level().run()
