from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 2
    part_two_test_solution = 4

    def preprocess_input(self, lines):
        lines = super().preprocess_input(lines)

        ranges = []
        for line in lines:
            first, second = line.split(',')
            ranges.append((
                tuple(map(int, first.split('-'))),
                tuple(map(int, second.split('-')))
            ))
        return ranges

    def part_one(self, ranges) -> int:
        return sum(f[0] <= s[0] and f[1] >= s[1] or f[0] >= s[0] and f[1] <= s[1] for f, s in ranges)

    def part_two(self, ranges) -> int:
        return sum(f[1] >= s[0] and f[0] <= s[1] for f, s in ranges)


Level().run()
