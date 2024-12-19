from functools import cache

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 6
    part_two_test_solution = 16

    def preprocess_input(self, lines):
        self.towels = lines[0].split(', ')
        return self.towels, lines[2:]

    @cache
    def is_pattern_valid(self, pattern: str, hack) -> int:  # hack to keep test cache separated
        if pattern == '':
            return 1
        return sum(self.is_pattern_valid(pattern[len(t) :], hack) for t in self.towels if pattern.startswith(t))

    def part_one(self, towels, patterns) -> int:
        return sum(self.is_pattern_valid(pattern, len(towels)) > 0 for pattern in patterns)

    def part_two(self, towels, patterns) -> int:
        return sum(self.is_pattern_valid(pattern, len(towels)) for pattern in patterns)


if __name__ == '__main__':
    Level().run()
