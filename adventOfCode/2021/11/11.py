from itertools import product

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1656
    part_two_test_solution = 195

    def preprocess_input(self, lines):
        return np.array([[int(n) for n in line.strip()] for line in lines])

    def increase_energy(self, point, grid):
        x, y = point
        for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[0]:
                grid[nx, ny] += 1

    def step(self, grid):
        grid += 1
        flashes = np.zeros_like(grid).astype(bool)
        while True:
            new_flashes = (grid > 9) & ~flashes
            if new_flashes.sum() == 0:
                break
            for flash in zip(*np.where(new_flashes)):
                self.increase_energy(flash, grid)

            flashes = new_flashes | flashes
        grid[flashes] = 0
        return flashes


    def part_one(self, grid) -> int:
        flashes_count = 0
        for i in range(100):
            flashes = self.step(grid)
            flashes_count += flashes.sum()
        return flashes_count

    def part_two(self, grid) -> int:
        step = 0
        while True:
            step += 1
            flashes = self.step(grid)
            if flashes.all():
                break
        return step


Level().run()
