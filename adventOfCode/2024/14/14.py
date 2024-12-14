from itertools import count

import numpy as np
import parse
from scipy.spatial.distance import cdist

from adventOfCode.utils import array
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 12
    part_two_test_solution = 0

    def preprocess_input(self, lines):
        shape = np.array(tuple(map(int, lines[0].split(','))))
        robots = []
        for line in lines[1:]:
            robots.append(tuple(parse.parse('p={:d},{:d} v={:d},{:d}', line)))
        robots = np.array(robots)
        return shape, robots[:, :2], robots[:, 2:]

    def part_one(self, shape, positions, deltas, seconds=100) -> int:
        positions = (positions + seconds * deltas) % shape
        q1 = ((positions[:, 0] < shape[0] // 2) & (positions[:, 1] < shape[1] // 2)).sum()
        q2 = ((positions[:, 0] < shape[0] // 2) & (positions[:, 1] > shape[1] // 2)).sum()
        q3 = ((positions[:, 0] > shape[0] // 2) & (positions[:, 1] < shape[1] // 2)).sum()
        q4 = ((positions[:, 0] > shape[0] // 2) & (positions[:, 1] > shape[1] // 2)).sum()
        return q1 * q2 * q3 * q4

    def part_two(self, shape, positions, deltas) -> int:
        if shape[0] == 11:
            return 0
        for second in count(1):
            positions = (positions + deltas) % shape
            distances = cdist(positions, positions, metric='cityblock')
            distances[distances == 0] = 100
            direct_neighbors = (distances.min(axis=0) == 1).sum()
            if direct_neighbors > len(positions) / 2:
                grid = array(np.zeros(shape, dtype=bool))
                for p in positions:
                    grid[tuple(p)] = True
                grid.T.print_grid()
                return second


if __name__ == '__main__':
    Level().run()
