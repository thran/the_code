import math

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1227775554
    part_two_test_solution = 4174379265

    def preprocess_input(self, lines):
        ranges = []
        for range in lines[0].split(','):
            start, stop = range.split('-')
            ranges.append((int(start), int(stop)))
        return ranges

    def part_one(self, ranges) -> int:
        result = 0
        for start, stop in ranges:
            start_length = len(str(start)) / 2
            if int(start_length) == start_length:
                minimal = start // 10 ** int(start_length)
            else:
                minimal = int(10 ** math.floor(start_length))

            stop_length = len(str(stop)) / 2
            if int(stop_length) == stop_length:
                maximal = stop // 10 ** int(stop_length)
            else:
                maximal = int(10 ** math.floor(stop_length)) - 1

            for n in range(minimal, maximal + 1):
                nn = 10 ** len(str(n)) * n + n
                if nn < start or nn > stop:
                    continue
                result += nn

        return result

    def part_two(self, ranges) -> int:
        result = 0
        for start, stop in ranges:
            for n in range(start, stop + 1):
                for length in range(1, len(str(n)) // 2 + 1):
                    if len(str(n)) % length != 0:
                        continue
                    repeats = len(str(n)) // length
                    if len({n // 10 ** (i * length) % 10**length for i in range(repeats)}) == 1:
                        result += n
                        break

        return result


if __name__ == '__main__':
    Level().run()
