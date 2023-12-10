import time
from pathlib import Path
from icecream import install

install()


def measure(function, input_):
    t = time.process_time()
    result = function(*input_)
    return result, time.process_time() - t


class AdventOfCode:
    part_one_test_solution = None
    part_two_test_solution = None
    skip_tests = False
    strip_only_new_lines = False

    @property
    def test_input(self):
        return self.load_file('input.test.txt')

    @property
    def test_input2(self):
        if Path('input.test2.txt').exists():
            return self.load_file('input.test2.txt')
        return self.test_input

    @property
    def input(self):
        return self.load_file('input.txt')

    def load_file(self, file_path):
        with Path(file_path).open() as f:
            if self.strip_only_new_lines:
                lines = list(map(lambda l: l.rstrip('\n'), f.readlines()))
            else:
                lines = list(map(lambda l: l.strip(), f.readlines()))
            input_ = self.preprocess_input(lines)
            if type(input_) is not tuple:
                return (input_,)
            return input_

    def preprocess_input(self, lines):
        if all(line.isnumeric() or line[0] == '-' and line[1:].isnumeric() for line in lines):
            lines = list(map(int, lines))
        if len(lines) == 1:
            return lines[0]

        return list(lines)

    def part_one(self, *input_) -> int:
        pass

    def part_two(self, *input_) -> int:
        pass

    def run(self):
        if self.part_one_test_solution is not None:
            if not self.skip_tests:
                part_one = self.part_one(*self.test_input)
                assert part_one == self.part_one_test_solution, f'invalid solution {part_one}'
            result, t = measure(self.part_one, self.input)
            print(f'part 1: {result:<20} in {t:.3g}s')

        if self.part_two_test_solution is not None:
            if not self.skip_tests:
                part_two = self.part_two(*self.test_input2)
                assert part_two == self.part_two_test_solution, f'invalid solution {part_two}'
            result, t = measure(self.part_two, self.input)
            print(f'part 2: {result:<20} in {t:.3g}s')
