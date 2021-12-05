# start: 11:14
# 1.:    11:23
# 2.:    11:31
from collections import defaultdict

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 5
    part_two_test_solution = 12

    def preprocess_input(self, lines):
        result = []
        for line in lines:
            p1, p2 = line.strip().split(' -> ')
            x1, y1 = map(int, p1.split(','))
            x2, y2 = map(int, p2.split(','))
            result.append(((x1, y1), (x2, y2)))
        return result

    def get_overlaps(self, lines, only_straight=False):
        points = defaultdict(int)
        for (x1, y1), (x2, y2) in lines:
            dx = np.sign(x2 - x1)
            dy = np.sign(y2 - y1)
            if only_straight and dx * dy != 0:
                continue
            length = max(abs(x1 - x2), abs(y1 - y2))
            for i in range(length + 1):
                points[(
                    x1 + i * dx,
                    y1 + i * dy,
                )] += 1

        return len([1 for point, count in points.items() if count > 1])

    def part_one(self, lines) -> int:
        return self.get_overlaps(lines, only_straight=True)

    def part_two(self, lines) -> int:
        return self.get_overlaps(lines)


Level().run()
