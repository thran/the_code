# start: 11:07
# 1.:    11:15
# 2.:    11:17
from collections import defaultdict

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 5934
    part_two_test_solution = 26984457539

    def preprocess_input(self, lines):
        return list(map(int, lines[0].split(',')))

    def simulate(self, timers, days):
        counts = defaultdict(int)
        for timer in timers:
            counts[timer] += 1
        for i in range(days):
            new_counts = defaultdict(int)
            for timer, count in counts.items():
                if timer > 0:
                    new_counts[timer - 1] += count
                else:
                    new_counts[6] += count
                    new_counts[8] = count

            counts = new_counts
        return sum(counts.values())

    def part_one(self, timers) -> int:
        return self.simulate(timers, 80)

    def part_two(self, timers) -> int:
        return self.simulate(timers, 256)


Level().run()
