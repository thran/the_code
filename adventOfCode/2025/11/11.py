from functools import cache

from black.trans import defaultdict

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 0
    part_two_test_solution = 2

    def preprocess_input(self, lines):
        self.cables = cables = defaultdict(list)
        for line in lines:
            start, *ends = line.replace(':', '').split()
            for end in ends:
                cables[end].append(start)
        return cables

    def part_one(self, cables) -> int:
        @cache
        def paths(start='you', end='out'):
            if start == end:
                return 1
            return sum(paths(start, i) for i in self.cables[end])

        return paths()

    def part_two(self, cables) -> int:
        @cache
        def paths(start, end):
            if start == end:
                return 1
            return sum(paths(start, i) for i in self.cables[end])

        return paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out')


if __name__ == '__main__':
    Level().run()
