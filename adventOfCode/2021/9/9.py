import numpy as np
from scipy.ndimage import minimum_filter, measurements
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 15
    part_two_test_solution = 1134

    def preprocess_input(self, lines):
        return np.array([[int(h) for h in line.strip()] for line in lines])

    def get_minimums(self, floor):
        return minimum_filter(
            floor,
            footprint=[[0, 1, 0], [1, 0, 1], [0, 1, 0]],
            mode='constant', cval=10,
        ) > floor

    def part_one(self, floor) -> int:
        minimums = self.get_minimums(floor)
        return sum(floor[minimums] + 1)

    def part_two(self, floor):
        basin_sizes = []
        labeled, count = measurements.label(floor < 9)
        for label in range(1, count + 1):
            basin_sizes.append((labeled == label).sum())
        return np.product(sorted(basin_sizes)[-3:])


Level().run()
