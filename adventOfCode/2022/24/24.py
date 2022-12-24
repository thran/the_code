import math
from itertools import product

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 18
    part_two_test_solution = 54

    def preprocess_input(self, lines):
        blizzards = []
        for row, line in enumerate(lines[1:-1]):
            for col, place in enumerate(line[1:-1]):
                match place:
                    case '<':
                        blizzards.append(((row, col), (0, -1)))
                    case '>':
                        blizzards.append(((row, col), (0, +1)))
                    case '^':
                        blizzards.append(((row, col), (-1, 0)))
                    case 'v':
                        blizzards.append(((row, col), (+1, 0)))

        return (
            blizzards,
            (len(lines) - 2, len(lines[0]) - 2),
            (-1, lines[0].index('.') - 1),
            (len(lines) - 2, lines[-1].index('.') - 1),
        )

    @staticmethod
    def get_empty_spaces(blizzards, size):
        cycle_length = math.lcm(*size)
        empties = [np.ones(size, dtype=bool) for _ in range(cycle_length)]
        for ((x, y), (dx, dy)), step in product(blizzards, range(cycle_length)):
            nx, ny = (x + dx * step) % size[0], (y + dy * step) % size[1]
            empties[step][nx, ny] = False
        return empties

    @staticmethod
    def min_steps_to_goal(empties, start, goal, step=0):
        positions = {start}
        visited = set()
        while goal not in positions:
            new_positions = set()
            next_normalized_step = (step + 1) % len(empties)
            empty = empties[next_normalized_step]
            for x, y in positions:
                for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < empty.shape[0]
                        and 0 <= ny < empty.shape[1]
                        and empty[nx, ny]
                        or (nx, ny) in (start, goal)
                    ):
                        state = (nx, ny), next_normalized_step
                        if state not in visited:
                            new_positions.add((nx, ny))
                            visited.add(state)
            positions = new_positions
            step += 1
        return step

    def part_one(self, blizzards, size, start, goal) -> int:
        empties = self.get_empty_spaces(blizzards, size)
        return self.min_steps_to_goal(empties, start, goal)

    def part_two(self, blizzards, size, start, goal) -> int:
        empties = self.get_empty_spaces(blizzards, size)
        step = self.min_steps_to_goal(empties, start, goal, 0)
        step = self.min_steps_to_goal(empties, goal, start, step)
        return self.min_steps_to_goal(empties, start, goal, step)


if __name__ == '__main__':
    Level().run()
