from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = None
    part_two_test_solution = None

    def preprocess_input(self, lines):
        return lines

    def part_one(self, lines) -> int:
        ...

    def part_two(self, lines) -> int:
        ...


if __name__ == '__main__':
    Level().run()
