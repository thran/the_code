import numpy as np

from adventOfCode.utils import array, SmartArray, DFS
from core import AdventOfCode


class Search(DFS):
    # state = start, position, current or None  for part 1
    # state = path, position, current or None   for part 2

    def __init__(self, grid: SmartArray, with_paths=False):
        super().__init__([None])
        self.grid = grid
        self.with_paths = with_paths
        self.trails = 0

    def next_states(self, state):
        if state is None:
            for x, y in np.transpose(np.where(self.grid == 0)):
                if self.with_paths:
                    yield ((x, y),), (x, y), 0
                else:
                    yield (x, y), (x, y), 0
            return

        if self.with_paths:
            path, position, current = state
        else:
            start, position, current = state
        if current == 9:
            return
        for new_position in self.grid.direct_neighbors(position):
            if self.grid[new_position] == current + 1:
                if self.with_paths:
                    yield path + (new_position,), new_position, current + 1
                else:
                    yield start, new_position, current + 1

    def on_state_visit(self, state):
        if state is None:
            return
        start, position, current = state
        if current == 9:
            self.trails += 1


class Level(AdventOfCode):
    part_one_test_solution = 36
    part_two_test_solution = 81

    def preprocess_input(self, lines):
        return array([tuple(map(int, line)) for line in lines])

    def part_one(self, grid: SmartArray, with_paths=False) -> int:
        search = Search(grid, with_paths)
        search()
        return search.trails

    def part_two(self, grid) -> int:
        return self.part_one(grid, True)


if __name__ == '__main__':
    Level().run()
