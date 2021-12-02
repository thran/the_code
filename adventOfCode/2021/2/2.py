# start: 9:46
# 1.:    9:51
# 2.:    9:54

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 150
    part_two_test_solution = 900

    def part_one(self, lines) -> int:
        depth = 0
        position = 0
        for line in lines:
            match line.split():
                case 'down', n:
                    depth += int(n)
                case 'up', n:
                    depth -= int(n)
                    assert depth >= 0
                case 'forward', n:
                    position += int(n)

        return depth * position

    def part_two(self, lines) -> int:
        depth = 0
        aim = 0
        position = 0
        for line in lines:
            match line.split():
                case 'down', n:
                    aim += int(n)
                case 'up', n:
                    aim -= int(n)
                case 'forward', n:
                    n = int(n)
                    position += n
                    depth += n * aim
        return depth * position


Level().run()
