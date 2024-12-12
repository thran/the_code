import numpy as np
from scipy.ndimage import label

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1930
    part_two_test_solution = 1206

    def preprocess_input(self, lines):
        return np.array([tuple(line) for line in lines])

    def get_borders(self, region):
        region = np.pad(region, 1).astype(np.int8)
        return region[:-1] - region[1:], region[:, :-1] - region[:, 1:]

    def part_one(self, grid, corners=False) -> int:
        result = 0
        for plant in np.unique(grid):
            regions, regions_count = label(grid == plant)
            for region_number in range(regions_count):
                region = regions == region_number + 1
                if corners:
                    vertical_borders, _ = self.get_borders(region)
                    _, corner_counts = self.get_borders(vertical_borders)
                    sides = np.abs(corner_counts).sum()
                else:
                    vertical_borders, horizontal_borders = self.get_borders(region)
                    sides = np.abs(vertical_borders).sum() + np.abs(horizontal_borders).sum()
                result += region.sum() * sides
        return result

    def part_two(self, grid) -> int:
        return self.part_one(grid, True)


if __name__ == '__main__':
    Level().run()
