import re

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 161
    part_two_test_solution = 48

    def part_one(self, lines) -> int:
        result = 0
        for line in lines:
            for mul in re.findall(r'mul\(\d{1,3},\d{1,3}\)', line):
                a, b = map(int, mul[4:-1].split(','))
                result += a * b
        return result

    def part_two(self, lines) -> int:
        result = 0
        enabled = True
        for line in lines:
            for mul, do, dont in re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', line):
                if do:
                    enabled = True
                    continue
                if dont:
                    enabled = False
                    continue
                if enabled:
                    a, b = map(int, mul[4:-1].split(','))
                    result += a * b
        return result


if __name__ == '__main__':
    Level().run()


# 102631226
