from itertools import combinations, pairwise

import numpy as np
from scipy.ndimage import label

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 50
    part_two_test_solution = 24

    def preprocess_input(self, lines):
        return np.array([tuple(map(int, line.split(','))) for line in lines])

    def part_one(self, tiles) -> int:
        return max(
            (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1) for tile1, tile2 in combinations(tiles, 2)
        )

    def part_two(self, tiles) -> int:
        xs = {x: i * 2 for i, x in enumerate(sorted(set(tiles[:, 0])))}
        ys = {y: i * 2 for i, y in enumerate(sorted(set(tiles[:, 1])))}

        transformed_tiles = np.array([(xs[x], ys[y]) for x, y in tiles])
        grid = np.zeros(transformed_tiles.max(axis=0) + 1, dtype=int)
        for tile1, tile2 in list(pairwise(transformed_tiles)) + [(transformed_tiles[0], transformed_tiles[-1])]:
            if tile1[0] == tile2[0]:
                grid[tile1[0], min(tile1[1], tile2[1]) : max(tile1[1], tile2[1]) + 1] = 1
            else:
                assert tile1[1] == tile2[1]
                grid[min(tile1[0], tile2[0]) : max(tile1[0], tile2[0]), tile1[1]] = 1

        labels, _ = label(grid == 0)

        outside = (set(labels[0, :]) | set(labels[-1, :]) | set(labels[:, 0]) | set(labels[:, -1])) - {0}
        for l in outside:
            grid[labels == l] = 2
        grid[grid == 0] = 1
        grid[grid == 2] = 0

        return max(
            (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
            for tile1, tile2 in combinations(tiles, 2)
            if (
                grid[
                    min(xs[tile1[0]], xs[tile2[0]]) : max(xs[tile1[0]], xs[tile2[0]]) + 1,
                    min(ys[tile1[1]], ys[tile2[1]]) : max(ys[tile1[1]], ys[tile2[1]]) + 1,
                ]
                == 1
            ).all()
        )


if __name__ == '__main__':
    Level().run()
