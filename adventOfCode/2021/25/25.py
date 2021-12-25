import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 58
    part_two_test_solution = None

    def preprocess_input(self, lines):
        return np.array([
            [1 if l == '>' else (2 if l == 'v' else 0)for l in line]
            for line in lines
        ])

    def step(self, floor, cucumber_type):
        axis = 1 if cucumber_type == 1 else 0

        new_spaces = np.roll(floor == cucumber_type, 1, axis=axis) & (floor == 0)
        floor[np.roll(new_spaces, -1, axis=axis)] = 0
        floor[new_spaces] = cucumber_type
        return floor, new_spaces.sum()

    def part_one(self, floor) -> int:
        steps = 0
        while True:
            steps += 1
            floor, moves_east = self.step(floor, 1)
            floor, moves_south = self.step(floor, 2)
            if moves_east + moves_south == 0:
                break
        return steps

    def part_two(self, floor) -> int:
        ...


Level().run()
