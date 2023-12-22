from collections import defaultdict

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 5
    part_two_test_solution = 7

    def preprocess_input(self, lines):
        bricks = []
        for line in lines:
            start, end = line.split('~')
            bricks.append((tuple(map(int, start.split(','))), tuple(map(int, end.split(',')))))
        return bricks

    @staticmethod
    def build_tower(bricks):
        max_x = max(max(s[0], e[0]) for s, e in bricks)
        max_y = max(max(s[1], e[1]) for s, e in bricks)

        tops_height = np.zeros((max_x + 1, max_y + 1), dtype=int)
        tops_brick = np.empty_like(tops_height)
        tops_brick.fill(-1)
        lies_on = {}
        for brick_number, (start, end) in enumerate(sorted(bricks, key=lambda b: b[0][2])):
            xs, ys = slice(start[0], end[0] + 1), slice(start[1], end[1] + 1)
            target_z = tops_height[xs, ys].max() + 1
            lies_on[brick_number] = set(tops_brick[xs, ys][tops_height[xs, ys] == target_z - 1]) - {-1}
            tops_height[xs, ys] = target_z + end[2] - start[2]
            tops_brick[xs, ys] = brick_number

        return lies_on

    def part_one(self, bricks) -> int:
        lies_on = self.build_tower(bricks)
        can_be_removed = np.ones(len(lies_on), dtype=bool)
        for lie_on in lies_on.values():
            if len(lie_on) == 1:
                can_be_removed[tuple(lie_on)[0]] = False
        return sum(can_be_removed)

    def part_two(self, bricks) -> int:
        lies_on = self.build_tower(bricks)
        is_under = defaultdict(set)
        for brick_number, lie_on in lies_on.items():
            for b in lie_on:
                is_under[b].add(brick_number)

        result = 0
        for brick in lies_on:
            falls = {brick}
            candidates = is_under[brick]
            while True:
                for b in candidates - falls:
                    if b in falls:
                        continue
                    if all(l in falls for l in lies_on[b]):
                        falls.add(b)
                        candidates -= {b}
                        candidates |= is_under[b]
                        break
                else:
                    break
            result += len(falls) - 1
        return result


if __name__ == '__main__':
    Level().run()
