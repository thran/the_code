# start: 9:28
# 1.:    9:35
# 2.:    9:39


from functools import partial

import numpy as np

from core import AdventOfCode
from utils import memoize


# suggest function on integers with single minimum between lower and upper
def search_for_minimum(fce, lower, upper):
    @memoize
    def _fce(n):
        return fce(n)

    mid = (lower + upper) // 2
    # search for triple with the lowest mid => new invariant
    while _fce(mid) > min(_fce(lower), _fce(upper)):
        assert _fce(mid) < max(_fce(lower), _fce(upper))
        if _fce(mid) > _fce(lower):
            upper = mid
        else:
            lower = mid
        mid = (lower + upper) // 2

    # reduce triple to 3 adjacent numbers
    while not (lower == mid - 1 and upper == mid + 1):
        if upper > mid + 1:
            new_upper = (mid + upper) // 2
            assert _fce(new_upper) <= _fce(upper)
            if _fce(new_upper) < _fce(mid):
                lower, mid = mid, new_upper
            else:
                upper = new_upper

        if lower < mid - 1:
            new_lower = (mid + lower) // 2
            assert _fce(new_lower) <= _fce(lower)
            if _fce(new_lower) < _fce(mid):
                upper, mid = mid, new_lower
            else:
                lower = new_lower

    return mid


class Level(AdventOfCode):
    part_one_test_solution = 37
    part_two_test_solution = 168

    def preprocess_input(self, lines):
        return np.array(list(map(int, lines[0].strip().split(','))))

    def part_one(self, numbers) -> int:
        position = np.round(np.median(numbers))
        return int(abs(numbers - position).sum())

    def wrong_but_working_part_two(self, numbers) -> int:
        float_position = np.mean(numbers)
        solutions = []
        for position in (np.floor(float_position), np.ceil(float_position)):
            distance = abs(numbers - position)
            fuels = (distance * (distance + 1)) // 2
            solutions.append(fuels.sum())
        return int(min(solutions))

    def _compute_cost(self, positions, target):
        distance = abs(positions - target)
        fuels = (distance * (distance + 1)) // 2
        return fuels.sum()

    def good_but_ugly_part_two(self, numbers) -> int:
        start_position = np.round(np.mean(numbers))

        solutions = []
        for dx in [-1, 1]:
            d = 0
            solutions.append(self._compute_cost(numbers, start_position))
            while True:
                d += 1
                solution = self._compute_cost(numbers, start_position + d * dx)
                if solution >= solutions[-1]:
                    break
                solutions.append(solution)

        return int(min(solutions))

    def part_two(self, numbers) -> int:
        position = search_for_minimum(partial(self._compute_cost, numbers), min(numbers), max(numbers))
        return int(self._compute_cost(numbers, position))

Level().run()
