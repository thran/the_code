import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 405
    part_two_test_solution = 400

    def preprocess_input(self, lines):
        patterns = []
        while lines:
            pattern = []
            while lines and (line := lines.pop(0)):
                pattern.append([1 if s == '#' else 0 for s in line])
            patterns.append(np.array(pattern))
        return patterns

    @staticmethod
    def find_mirror(elements, smudges=0):
        for m in range(1, len(elements)):
            distances_from_mirror = range(0, min(len(elements) - m, m))
            if sum(np.abs(elements[m - d - 1] - elements[m + d]).sum() for d in distances_from_mirror) == smudges:
                return m
        return 0

    def part_one(self, patterns, smudges=0) -> int:
        result = 0
        for pattern in patterns:
            result += self.find_mirror(pattern.T, smudges)
            result += 100 * self.find_mirror(pattern, smudges)
        return result

    def part_two(self, lines) -> int:
        return self.part_one(lines, 1)


if __name__ == '__main__':
    Level().run()
