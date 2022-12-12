import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 31
    part_two_test_solution = 29

    def preprocess_input(self, lines):

        grid = []
        s_position, e_position = None, None
        normalization = ord('a')
        for row, line in enumerate(lines):
            if 'S' in line:
                s_position = row, line.find('S')
                line = line.replace('S', 'a')
            if 'E' in line:
                e_position = row, line.find('E')
                line = line.replace('E', 'z')
            grid.append([ord(h) - normalization for h in line])

        return np.array(grid), s_position, e_position

    @staticmethod
    def find_min_distance(grid, starts, end):
        positions_by_distance = [{end}]
        visited_positions = {end}
        steps = 0
        while all(start not in positions_by_distance[-1] for start in starts):
            steps += 1
            new_positions = set()
            for position in positions_by_distance[-1]:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_position = x, y = position[0] + dx, position[1] + dy
                    if (
                        0 <= x < grid.shape[0]
                        and 0 <= y < grid.shape[1]
                        and grid[new_position] >= grid[position] - 1
                        and new_position not in visited_positions
                    ):
                        new_positions.add(new_position)
                        visited_positions.add(new_position)
            positions_by_distance.append(new_positions)
        return steps

    def part_one(self, grid, s_position, e_position) -> int:
        return self.find_min_distance(grid, (s_position,), e_position)

    def part_two(self, grid, s_position, e_position) -> int:
        starts = tuple(tuple(s) for s in np.transpose((grid == 0).nonzero()))
        return self.find_min_distance(grid, starts, e_position)


Level().run()
