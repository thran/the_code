import numpy as np
from scipy.signal import convolve2d

from adventOfCode.utils import array, SmartArray
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 13
    part_two_test_solution = 43

    def preprocess_input(self, lines):
        floor = array([list(line) for line in lines])
        return array(floor == '@')

    def removable(self, floor: SmartArray):
        return (
            (row, column)
            for row, line in enumerate(floor)
            for column, cell in enumerate(line)
            if cell and sum(floor[p] for p in floor.neighbors((row, column))) < 4
        )

    def removable_fast(self, floor: SmartArray) -> np.array:
        pattern = np.ones((3, 3), dtype=np.int8)
        pattern[1, 1] = False

        return (convolve2d(floor, pattern, mode='same') < 4) & floor

    def part_one(self, floor: SmartArray) -> int:
        return self.removable_fast(floor).sum()

    def part_two(self, floor: SmartArray) -> int:
        removed = 0
        while (to_remove := self.removable_fast(floor)).any():
            removed += to_remove.sum()
            floor[to_remove] = False
        return removed

    def part_one_slow(self, floor: SmartArray) -> int:
        return len(tuple(self.removable(floor)))

    def part_two_slow(self, floor: SmartArray) -> int:
        removed = 0
        while len(to_remove := array(list(self.removable(floor)))):
            removed += len(to_remove)
            floor[to_remove[:, 0], to_remove[:, 1]] = False
        return removed


if __name__ == '__main__':
    Level().run()
