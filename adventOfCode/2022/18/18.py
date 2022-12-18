from itertools import product

import numpy as np
from scipy.ndimage import label

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 64
    part_two_test_solution = 58

    def preprocess_input(self, lines):
        cubes = set()
        for line in lines:
            cubes.add(tuple(map(int, line.split(','))))
        return cubes

    @staticmethod
    def compute_surface(cubes):
        def _get_cube_surface(cube):
            surface = 0
            for dimension, direction in product(range(3), [-1, 1]):
                neighbour = tuple(cube[i] + direction * (dimension == i) for i in range(3))
                if neighbour not in cubes:
                    surface += 1
            return surface

        return sum(_get_cube_surface(c) for c in cubes)

    def part_one(self, cubes) -> int:
        return self.compute_surface(cubes)

    def part_two(self, cubes) -> int:
        space = np.zeros(tuple(max(c[d] for c in cubes) + 1 for d in range(3)))
        for cube in cubes:
            space[cube] = 1

        surface = self.compute_surface(cubes)
        hole_map, holes_count = label(1 - space)  # find connected empty parts
        for component in range(2, holes_count + 1):  # 0 are cubes a 1 is outside
            hole = set(tuple(e) for e in np.transpose((hole_map == component).nonzero()))
            surface -= self.compute_surface(hole)

        return surface


Level().run()
