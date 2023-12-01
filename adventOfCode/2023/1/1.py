from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = None
    part_two_test_solution = 281
    NUMBERS = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    def part_one(self, lines) -> int:
        s = 0
        for line in lines:
            digits = [s for s in line if s.isdigit()]
            s += int(digits[0] + digits[-1])
            print(int(digits[0] + digits[-1]))
        return s

    def part_two(self, lines) -> int:
        s = 0
        for line in lines:
            start = line
            first = None
            while start and first is None:
                if start[0].isdigit():
                    first = start[0]
                    break
                for number, n in self.NUMBERS.items():
                    if start.startswith(number):
                        first = str(n)
                        break
                start = start[1:]

            end = line
            last = None
            while end and last is None:
                if end[-1].isdigit():
                    last = end[-1]
                    break
                for number, n in self.NUMBERS.items():
                    if end.endswith(number):
                        last = str(n)
                        break
                end = end[:-1]
            s += int(first+last)
        return s


Level().run()
