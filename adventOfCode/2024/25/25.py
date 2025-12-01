from itertools import product

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 3
    part_two_test_solution = None

    def preprocess_input(self, lines):
        locks, keys = [], []
        i = 0
        while i * 8 < len(lines):
            schema = lines[i * 8 : i * 8 + 7]
            if schema[0] == '#####':
                locks.append(np.array(tuple(map(lambda l: tuple(map(lambda s: s == '#', l)), schema[1:]))).sum(axis=0))
            else:
                keys.append(np.array(tuple(map(lambda l: tuple(map(lambda s: s == '#', l)), schema[:6]))).sum(axis=0))
            i += 1
        return np.array(locks, dtype=np.uint8), np.array(keys, dtype=np.uint8)

    def part_one(self, locks, keys) -> int:
        return sum(1 for lock, key in product(locks, keys) if (lock + key <= 5).all())

    def part_two(self, lines) -> int:
        ...


if __name__ == '__main__':
    Level().run()
