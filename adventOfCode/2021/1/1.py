# start: 9:33
# 1.:    9:37
# 2.:    9:41

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 7
    part_two_test_solution = 5

    def get_increases(self, values):
        increases = 0
        last_value = values[0]
        for depth in values[1:]:
            if last_value < depth:
                increases += 1
            last_value = depth
        return increases

    def part_one(self, depths) -> int:
        return self.get_increases(depths)

    def part_two(self, depths) -> int:
        return self.get_increases([sum(depths[i:i + 3]) for i in range(len(depths) - 2)])


Level().run()
