import math

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 288
    part_two_test_solution = 71503

    def preprocess_input(self, lines):
        return list(zip(map(int, lines[0].split()[1:]), map(int, lines[1].split()[1:])))

    def part_one(self, races) -> int:
        result = 1
        for time, length in races:
            # solving (time - solution) * solution > length
            d_root = math.sqrt(time**2 - 4 * length)
            solution_min = math.floor((time - d_root) / 2) + 1
            solution_max = math.ceil((time + d_root) / 2) - 1
            result *= solution_max - solution_min + 1
        return result

    def part_two(self, races) -> int:
        new_time, new_length = '', ''
        for time, length in races:
            new_time += str(time)
            new_length += str(length)
        return self.part_one([(int(new_time), int(new_length))])


if __name__ == '__main__':
    Level().run()
