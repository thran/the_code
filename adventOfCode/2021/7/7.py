# start: 9:28
# 1.:    9:35
# 2.:    9:39
import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 37
    part_two_test_solution = 168

    def preprocess_input(self, lines):
        return np.array(list(map(int, lines[0].strip().split(','))))

    def part_one(self, numbers) -> int:
        position = np.round(np.median(numbers))
        return int(abs(numbers - position).sum())

    def part_two(self, numbers) -> int:
        float_position = np.mean(numbers)
        solutions = []
        for position in (np.floor(float_position), np.ceil(float_position)):
            distance = abs(numbers - position)
            fuels = (distance * (distance + 1)) // 2
            solutions.append(fuels.sum())
        return int(min(solutions))


Level().run()
