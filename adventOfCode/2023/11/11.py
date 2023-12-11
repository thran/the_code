import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 374
    part_two_test_solution = 82000210

    def preprocess_input(self, lines):
        return np.array(list(map(list, lines))) == '#'

    def part_one(self, space, expansion=2) -> int:
        y_spaces = np.where(space.sum(axis=0) == 0)[0]
        x_spaces = np.where(space.sum(axis=1) == 0)[0]
        x_locations, y_locations = np.where(space)

        s = 0
        for locations, spaces in ((x_locations, x_spaces), (y_locations, y_spaces)):
            locations.sort()
            for x in locations:
                s += np.abs(locations - x).sum() / 2  # / 2 because we're counting each pair twice
            for space in spaces:
                space_position = np.searchsorted(locations, space)
                s += space_position * (len(locations) - space_position) * (expansion - 1)
        assert int(s) == s
        return int(s)

    def part_two(self, space) -> int:
        return self.part_one(space, expansion=10**6)


if __name__ == '__main__':
    Level().run()
