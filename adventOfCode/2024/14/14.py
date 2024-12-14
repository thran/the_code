from itertools import count

import numpy as np
import parse
from scipy.stats import entropy

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 12
    part_two_test_solution = -1
    skip_tests = True

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
        for second in count(1):
            positions = (positions + deltas) % shape
            x_counts = np.unique(positions[:, 0], return_counts=True)[1]
            y_counts = np.unique(positions[:, 1], return_counts=True)[1]
            score = entropy(x_counts) + entropy(y_counts)
            if score < 8:
                return second


if __name__ == '__main__':
    Level().run()
