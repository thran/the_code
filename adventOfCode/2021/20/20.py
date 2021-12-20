import numpy as np

from core import AdventOfCode
from scipy.ndimage import filters


class Level(AdventOfCode):
    part_one_test_solution = 35
    part_two_test_solution = 3351

    def preprocess_input(self, lines):
        code = [int(s == '#') for s in lines[0]]

        floor = np.array([
            [int(s == '#') for s in line]
            for line in lines[2:]
        ])
        return code, floor

    def step(self, floor, code, all_other):
        def _filter(x):
            index = int(''.join([str(int(s)) for s in x]), 2)
            return code[index]

        return filters.generic_filter(
            np.pad(floor, ((1, 1), (1, 1)), constant_values=all_other),
            _filter, size=3,
            mode='constant', cval=all_other,
        )

    def simulate(self, code, floor, steps):
        all_other = 0
        for i in range(steps):
            floor = self.step(floor, code, all_other)
            all_other = code[0 if all_other == 0 else len(code) - 1]
        return int(floor.sum())

    def part_one(self, code, floor) -> int:
        return self.simulate(code, floor, 2)

    def part_two(self, code, floor) -> int:
        return self.simulate(code, floor, 50)


Level().run()
