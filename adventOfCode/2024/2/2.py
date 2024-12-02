from itertools import pairwise

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 2
    part_two_test_solution = 4

    def preprocess_input(self, lines):
        return [list(map(int, line.split())) for line in lines]

    def is_safe(self, report) -> bool:
        report_order = None
        for a, b in pairwise(report):
            if abs(a - b) > 3 or a == b:
                return False
            if a > b:
                order = -1
            else:
                order = 1
            if report_order is None:
                report_order = order
            else:
                if report_order != order:
                    return False
        return True

    def part_one(self, reports) -> int:
        valid = 0
        for report in reports:
            valid += int(self.is_safe(report))
        return valid

    def part_two(self, reports) -> int:
        valid = 0
        for report in reports:
            for i in range(len(report)):
                truncated_report = list(report)
                del truncated_report[i]
                if self.is_safe(truncated_report):
                    valid += 1
                    break
        return valid


if __name__ == '__main__':
    Level().run()
