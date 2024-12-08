from itertools import combinations

import numpy as np

from adventOfCode.utils import array, SmartArray
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 14
    part_two_test_solution = 34

    def preprocess_input(self, lines):
        return array(list(map(tuple, lines)))

    def part_one(self, plan: SmartArray, harmonics=False) -> int:
        antinodes = set()
        signals = {f for f in plan.flatten()} - {'.'}
        for signal in signals:
            antennas = np.array(list(zip(*np.where(plan == signal))))
            for antenna1, antenna2 in combinations(antennas, 2):
                delta = antenna1 - antenna2
                if harmonics:
                    for direction in (-1, 1):
                        antinode = np.array(antenna1)
                        while True:
                            antinodes.add(tuple(antinode))
                            antinode += direction * delta
                            if not plan.is_valid_position(antinode):
                                break
                else:
                    for antinode in (antenna1 + delta, antenna2 - delta):
                        if plan.is_valid_position(antinode):
                            antinodes.add(tuple(antinode))
        return len(antinodes)

    def part_two(self, plan) -> int:
        return self.part_one(plan, True)


if __name__ == '__main__':
    Level().run()
