from collections import defaultdict

import numpy as np

from core import AdventOfCode


class V(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __add__(self, other: 'V'):
        return V(self[0] + other[0], self[1] + other[1])


class Level(AdventOfCode):
    part_one_test_solution = 110
    part_two_test_solution = 20

    DIRECTIONS = [
        (V(-1, 0), [V(-1, -1), V(-1, 0), V(-1, 1)]),
        (V(1, 0), [V(1, -1), V(1, 0), V(1, 1)]),
        (V(0, -1), [V(-1, -1), V(0, -1), V(1, -1)]),
        (V(0, 1), [V(-1, 1), V(0, 1), V(1, 1)]),
    ]

    def preprocess_input(self, lines):
        elves = set()
        for x, line in enumerate(lines):
            for y, tile in enumerate(line):
                if tile == '#':
                    elves.add(V(x, y))

        return elves

    @staticmethod
    def get_cave(elves):
        x_min = min(x for x, y in elves)
        x_max = max(x for x, y in elves)
        y_min = min(y for x, y in elves)
        y_max = max(y for x, y in elves)

        cave = np.zeros((x_max - x_min + 1, y_max - y_min + 1))
        for x, y in elves:
            cave[x - x_min, y - y_min] = 1
        return cave

    @staticmethod
    def print_cave(cave):
        for row in cave:
            print(''.join('#' if e else '.' for e in row))

    def simulate(self, elves: set[V], steps: int = None):
        step_number = 0
        while steps is None or step_number < steps:
            step_number += 1
            proposes = defaultdict(list)
            for elv in elves:
                elv_proposes = []
                for d in range(4):
                    direction, neighbours = self.DIRECTIONS[(step_number + d - 1) % 4]
                    if all((elv + n) not in elves for n in neighbours):
                        elv_proposes.append(direction)
                if len(elv_proposes) in (0, 4):
                    continue
                proposes[elv + elv_proposes[0]].append(elv)

            for new_place, proposers in proposes.items():
                if len(proposers) > 1:
                    continue
                elves.remove(proposers[0])
                elves.add(new_place)
            if not proposes:
                break

        return step_number

    def part_one(self, elves) -> int:
        self.simulate(elves, 10)
        return (self.get_cave(elves) == 0).sum()

    def part_two(self, elves) -> int:
        return self.simulate(elves)


Level().run()
