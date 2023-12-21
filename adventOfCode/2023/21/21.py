from itertools import product

from adventOfCode.utils import array, BFS, SmartArray
from core import AdventOfCode


class Walk(BFS):
    def __init__(self, garden, start, max_steps):
        self.garden: SmartArray = garden
        self.max_steps = max_steps
        super().__init__([(start, 0)])

    def next_states(self, state):
        position, step = state
        for next_position in self.garden.direct_neighbors(position):
            if self.garden[next_position] == '.':
                yield next_position, step + 1

    def get_state_hash(self, state):
        return state[0]

    def end_condition(self, state) -> bool:
        return state[1] > self.max_steps


class Level(AdventOfCode):
    part_one_test_solution = 42
    part_two_test_solution = 0
    skip_tests = True

    def preprocess_input(self, lines):
        rows = []
        for i, line in enumerate(lines):
            row = []
            for j, s in enumerate(line):
                row.append('#' if s == '#' else '.')
                if s == 'S':
                    start = i, j
            rows.append(row)
        return array(rows), start

    def part_one(self, garden, start, steps=64) -> int:
        walk = Walk(garden, start, steps)
        walk()
        return len([position for position in walk.visited_states if (sum(position) + steps) % 2 == sum(start) % 2])

    def part_two(self, garden, start, steps=26501365) -> int:
        assert garden.shape[0] == garden.shape[1]
        garden_size = garden.shape[0]
        assert start[0] == start[1] == garden.shape[1] / 2 - 0.5
        to_edge = start[0]

        fully_reachable_tile_distance = steps // garden_size - 1

        total = 0

        # tips of square
        steps_from_edge = steps - garden_size * fully_reachable_tile_distance - to_edge - 1
        top = self.part_one(garden, (garden_size - 1, start[1]), steps_from_edge)
        bottom = self.part_one(garden, (0, start[1]), steps_from_edge)
        right = self.part_one(garden, (start[0], 0), steps_from_edge)
        left = self.part_one(garden, (start[0], garden_size - 1), steps_from_edge)
        total += top + bottom + right + left

        # edges of square
        edge_tile_length = fully_reachable_tile_distance
        steps_from_corner = steps_from_edge - to_edge - 1
        for position in product([garden_size - 1, 0], repeat=2):
            total += self.part_one(garden, position, steps_from_corner + garden_size) * edge_tile_length  # inner edge
            total += self.part_one(garden, position, steps_from_corner) * (edge_tile_length + 1)  # inner edge

        full_odd = self.part_one(garden, start, garden_size * 2 + steps % 2 + fully_reachable_tile_distance % 2)
        total += full_odd * (fully_reachable_tile_distance + 1) ** 2
        full_even = self.part_one(garden, start, garden_size * 2 + steps % 2 + fully_reachable_tile_distance % 2 + 1)
        total += full_even * fully_reachable_tile_distance**2

        return total


if __name__ == '__main__':
    Level().run()
