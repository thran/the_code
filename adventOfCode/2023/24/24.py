from collections import Counter
from itertools import combinations, count, product

import numpy as np
from matplotlib import pyplot as plt

from core import AdventOfCode


def generate_deltas():
    for s in count():
        for x in range(s + 1):
            y = s - x
            for a, b in product([1, -1], repeat=2):
                yield x * a, y * b


class Level(AdventOfCode):
    part_one_test_solution = 0
    part_two_test_solution = 47
    # skip_tests = True

    def preprocess_input(self, lines):
        hails = []
        for line in lines:
            position, delta = line.split(' @ ')
            hails.append((np.array(tuple(map(int, position.split(',')))), np.array(tuple(map(int, delta.split(','))))))
        return hails

    def part_one(self, hails, test_area=(200000000000000, 400000000000000)) -> int:
        hits = 0
        for (p1, d1), (p2, d2) in combinations(hails, 2):
            a = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
            b = np.array([-p1[0] + p2[0], -p1[1] + p2[1]])
            try:
                t1, t2 = np.linalg.solve(a, b)
            except np.linalg.LinAlgError:
                continue

            if t1 < 0 or t2 < 0:
                continue

            intersection = t1 * d1 + p1
            if all(test_area[0] <= d <= test_area[1] for d in intersection[:2]):
                hits += 1
        return hits

    def part_two(self, hails) -> int:
        positions = np.array([p for p, d in hails])
        deltas = np.array([d for p, d in hails])
        # generate small dx, dy  of rock
        for delta in generate_deltas():
            take_hails = 4
            rows = []

            # linear equation for intersection with first `take_hails`
            # variables: t1, t2 ... tn, x, y of rock position
            for i in range(take_hails):
                for d in range(2):
                    rows.append(
                        [0] * i + [delta[d] - deltas[i, d]] + [0] * (take_hails - i - 1) + [0] * d + [1] + [0] * (1 - d)
                    )
            a = np.array(rows)
            b = np.concatenate(positions[:take_hails, :2])
            try:
                # drop some rows to make square
                mask = [True] * len(b)
                mask[-1] = False
                mask[-3] = False
                solution = np.linalg.solve(a[mask], b[mask])
            except np.linalg.LinAlgError as error:
                continue
            # check correctness on all equations
            if np.all(np.dot(a, solution) == b):
                # find z
                t1, t2, t3, t4, *position = solution
                intersection_zs = [positions[0, 2] + t1 * deltas[0, 2], positions[1, 2] + t2 * deltas[1, 2]]
                z, dz = np.linalg.solve([[1, t1], [1, t2]], intersection_zs)

                return int(sum(position) + z)


if __name__ == '__main__':
    Level().run()
