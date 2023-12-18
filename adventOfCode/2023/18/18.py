from collections import defaultdict

import numpy as np
from more_itertools import batched

from adventOfCode.utils import SmartArray
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 62
    part_two_test_solution = 952408144115

    DELTAS = {'r': (0, 1), 'l': (0, -1), 'd': (1, 0), 'u': (-1, 0)}

    def preprocess_input(self, lines):
        instructions = []
        for line in lines:
            direction, distance, color = line.split(' ')
            instructions.append((direction.lower(), int(distance), color[2:-1]))
        return instructions

    @staticmethod
    def update_intervals(intervals, pairs):
        length_decreased = 0  # how much length was decreased (increases ignoring)
        for pair in pairs:
            for i, interval in enumerate(intervals):
                if interval[0] == pair[1]:  # join on start
                    intervals[i] = (pair[0], interval[1])
                    break
                if interval[1] == pair[0]:  # join on end
                    intervals[i] = (interval[0], pair[1])
                    break
                if interval[0] == pair[0]:  # cut start
                    if interval[1] == pair[1]:  # same interval
                        del intervals[i]
                        length_decreased += pair[1] - pair[0] + 1
                    else:
                        length_decreased += pair[1] - pair[0]
                        intervals[i] = (pair[1], interval[1])
                    break
                if interval[1] == pair[1]:  # cut end
                    length_decreased += pair[1] - pair[0]
                    intervals[i] = (interval[0], pair[0])
                    break
                if interval[0] < pair[0] and interval[1] > pair[1]:  # split
                    length_decreased += pair[1] - pair[0] - 1
                    intervals[i] = (interval[0], pair[0])
                    intervals.append((pair[1], interval[1]))
                    break
            else:
                intervals.append(pair)

        positions = sorted(p for interval in intervals for p in interval)
        joined_intervals = list(batched((p for p in positions if positions.count(p) == 1), 2))
        return joined_intervals, length_decreased  # join intervals

    def part_one(self, instructions) -> int:
        position = (0, 0)
        turns = defaultdict(list)
        for direction, distance, _ in instructions:
            position = SmartArray.change_position(position, np.array(self.DELTAS[direction]) * distance)
            turns[position[0]].append(position[1])
        for ys in turns.values():
            ys.sort()

        intervals = []
        last_x = None
        area = 0
        for x, ys in sorted(turns.items()):
            if last_x is not None:
                area += (x - last_x - 1) * sum(b - a + 1 for a, b in intervals)  # for lines above
            last_x = x
            intervals, length_decreased = self.update_intervals(intervals, batched(ys, 2))
            intervals_length = sum(b - a + 1 for a, b in intervals)
            area += intervals_length + length_decreased  # for current line

        return area

    def part_two(self, instructions) -> int:
        new_instructions = []
        for _, _, color in instructions:
            new_instructions.append(('rdlu'[int(color[-1])], int(color[:5], 16), None))
        return self.part_one(new_instructions)


if __name__ == '__main__':
    Level().run()
