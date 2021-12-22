import numpy as np
from parse import parse

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 474140
    part_two_test_solution = 2758514936282235

    def preprocess_input(self, lines):
        cuboids = []
        for line in lines:
            action, x1, x2, y1, y2, z1, z2 = parse('{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}', line)
            cuboids.append((action == 'on', (x1, x2), (y1, y2), (z1, z2)))
        return cuboids


    def part_one(self, cuboids) -> int:
        return self.part_two([c for c in cuboids if all(abs(z[0]) <= 50 and abs(z[1]) <= 50 for z in c[1:])])

    def part_two(self, cuboids) -> int:
        x_cuts = sorted(x for (_, (x1, x2), _, _) in cuboids for x in (x1, x2 + 1))
        y_cuts = sorted(y for (_, _, (y1, y2), _) in cuboids for y in (y1, y2 + 1))
        z_cuts = sorted(z for (_, _, _, (z1, z2)) in cuboids for z in (z1, z2 + 1))

        x_sizes = np.array([x_cuts[i + 1] - x_cuts[i] for i in range(len(x_cuts) - 1)])
        y_sizes = np.array([y_cuts[i + 1] - y_cuts[i] for i in range(len(y_cuts) - 1)])
        z_sizes = np.array([z_cuts[i + 1] - z_cuts[i] for i in range(len(z_cuts) - 1)])
        sizes = np.dot(np.outer(x_sizes, y_sizes)[:, :, None], z_sizes[None, :])

        engine = np.zeros((len(x_cuts) - 1, len(y_cuts) - 1, len(z_cuts) - 1), dtype=bool)
        for action, (x1, x2), (y1, y2), (z1, z2) in cuboids:
            engine[
                x_cuts.index(x1):x_cuts.index(x2 + 1),
                y_cuts.index(y1):y_cuts.index(y2 + 1),
                z_cuts.index(z1):z_cuts.index(z2 + 1),
            ] = action

        return (engine * sizes).sum()


Level().run()
