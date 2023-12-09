from core import AdventOfCode
from itertools import pairwise, cycle


class Level(AdventOfCode):
    part_one_test_solution = 114
    part_two_test_solution = 2

    def preprocess_input(self, lines):
        return [list(map(int, line.split())) for line in lines]

    @staticmethod
    def predict(series, past=False):
        ends, starts = [], []
        while any(s != 0 for s in series):
            ends.append(series[-1])
            starts.append(series[0])
            series = [s2 - s1 for s1, s2 in pairwise(series)]
        if past:
            return sum(e * c for e, c in zip(starts, cycle((1, -1))))
        return sum(ends)

    def part_one(self, series) -> int:
        return sum(self.predict(s) for s in series)

    def part_two(self, series) -> int:
        return sum(self.predict(s, True) for s in series)


if __name__ == '__main__':
    Level().run()
