from adventOfCode.utils import array, SmartArray
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 13
    part_two_test_solution = 43

    def preprocess_input(self, lines):
        floor = array([list(line) for line in lines])
        return array(floor == '@')

    def removable(self, floor: SmartArray):
        return (
            (row, column)
            for row, line in enumerate(floor)
            for column, cell in enumerate(line)
            if cell and sum(floor[p] for p in floor.neighbors((row, column))) < 4
        )

    def part_one(self, floor: SmartArray) -> int:
        return len(tuple(self.removable(floor)))

    def part_two(self, floor: SmartArray) -> int:
        removed = 0
        while len(to_remove := array(list(self.removable(floor)))):
            removed += len(to_remove)
            floor[to_remove[:, 0], to_remove[:, 1]] = False
        return removed


if __name__ == '__main__':
    Level().run()
