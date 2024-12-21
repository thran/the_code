from functools import cache
from itertools import pairwise

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 126384
    part_two_test_solution = 0
    skip_tests = True

    NUMPAD = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']])
    DPAD = np.array([[None, '^', 'A'], ['<', 'v', '>']])

    @cache
    def travel_and_press_steps(self, key_from, key_to, depth, numpad=False) -> int:
        pad = self.NUMPAD if numpad else self.DPAD
        position_from = np.argwhere(pad == key_from)[0]
        position_to = np.argwhere(pad == key_to)[0]
        delta = position_to - position_from

        if depth == 1:
            return np.abs(delta).sum() + 1

        parts = []
        if delta[0] < 0:
            parts.append(('^', -delta[0]))
        if delta[1] > 0:
            parts.append(('>', delta[1]))
        if delta[0] > 0:
            parts.append(('v', delta[0]))
        if delta[1] < 0:
            parts.append(('<', -delta[1]))
        if len(parts) == 1:
            direction, count = parts[0]
            return self.count_steps(direction * count + 'A', depth - 1)
        assert len(parts) == 2

        options = []
        for (direction1, count1), (direction2, count2) in [parts, parts[::-1]]:
            # avoid empty corners
            if numpad and direction1 == 'v' and position_from[1] == 0 and position_to[0] == 3:
                continue
            if numpad and direction1 == '<' and position_from[0] == 3 and position_to[1] == 0:
                continue
            if not numpad and direction1 == '<' and position_from[0] == 0 and position_to[1] == 0:
                continue
            if not numpad and direction1 == '^' and position_from[1] == 0 and position_to[0] == 0:
                continue
            options.append(direction1 * count1 + direction2 * count2 + 'A')

        return min(self.count_steps(o, depth - 1) for o in options)

    def count_steps(self, sequence, depth, numpad=False) -> int:
        result = 0
        for position_from, position_to in pairwise('A' + sequence):
            if position_from == position_to:
                result += 1
            else:
                result += self.travel_and_press_steps(position_from, position_to, depth, numpad)

        return result

    def part_one(self, codes, robots=3) -> int:
        result = 0
        for code in codes:
            result += self.count_steps(code, robots, True) * int(code[:-1])
        return result

    def part_two(self, codes) -> int:
        return self.part_one(codes, 26)


if __name__ == '__main__':
    Level().run()
