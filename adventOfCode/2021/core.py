from pathlib import Path
from icecream import install

install()


class AdventOfCode:
    part_one_test_solution = None
    part_two_test_solution = None

    @property
    def test_input(self):
        return self.load_file('input.test.txt')

    @property
    def input(self):
        return self.load_file('input.txt')

    def load_file(self, file_path):
        with Path(file_path).open() as f:
            input_ = self.preprocess_input(map(lambda l: l.strip(), f.readlines()))
            if type(input_) is not tuple:
                return (input_, )
            return input_

    def preprocess_input(self, lines):
        lines = [line.strip() for line in lines]
        if all(line.isnumeric() for line in lines):
            lines = list(map(int, lines))
        if len(lines) == 0:
            return lines[0]

        return list(lines)

    def part_one(self, *input_) -> int:
        pass

    def part_two(self, *input_) -> int:
        pass

    def run(self):
        part_one = self.part_one(*self.test_input)
        assert part_one == self.part_one_test_solution, f'invalid solution {part_one}'
        print(f'part 1: {self.part_one(*self.input)}')

        if self.part_two_test_solution is not None:
            part_two = self.part_two(*self.test_input)
            assert  part_two == self.part_two_test_solution, f'invalid solution {part_two}'
            print(f'part 2: {self.part_two(*self.input)}')
