# start 9:03, 1. 9:24, 2. 9:27
from collections import defaultdict
from itertools import product
from pathlib import Path


def load_grid(dimensions):
    grid = set()
    with Path('input.txt').open() as file:
        for y, line in enumerate(file):
            for x, cube in enumerate(line.strip()):
                if cube == '#':
                    grid.add((x, y) + tuple(0 for _ in range(dimensions - 2)))
    return grid


def neighbours(coordinates, dimensions):
    for delta in product([-1, 0, 1], repeat=dimensions):
        if all(d == 0 for d in delta):
            continue
        yield tuple(c + dc for c, dc in zip(coordinates, delta))


def active_neighbours(coordinates, grid, dimensions):
    for n in neighbours(coordinates, dimensions):
        if n in grid:
            yield n


for dimensions in [3, 4]:
    grid = load_grid(dimensions)
    for _ in range(6):
        new_grid = set()

        for c in grid:
            if sum(1 for n in active_neighbours(c, grid, dimensions)) in (2, 3):
                new_grid.add(c)

        candidates = set(n for c in grid for n in neighbours(c, dimensions))
        for c in candidates:
            if sum(1 for n in active_neighbours(c, grid, dimensions)) == 3:
                new_grid.add(c)
        grid = new_grid

    print(len(grid))
