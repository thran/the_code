from collections import deque

import numpy as np

from adventOfCode.utils import array, SmartArray, PrioritySearch
from core import AdventOfCode


class Search(PrioritySearch):
    DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # state = score, position, orientation, last_position

    def __init__(self, grid: SmartArray, start, end):
        super().__init__([(0, start, 0, (start, 0))])
        self.grid = grid
        self.end = end

        self.visited_positions = {}  # position, orientation -> score, {previous state}
        self.solutions = []

    def next_states(self, state):
        score, position, orientation, last_state = state
        if (position, orientation) in self.visited_positions:
            if score == self.visited_positions[position, orientation][0]:
                self.visited_positions[position, orientation][1].add(last_state)
            return
        self.visited_positions[position, orientation] = score, {last_state}

        new_position = self.grid.change_position(position, self.DELTAS[orientation])
        if not self.grid.get(new_position, True):
            yield score + 1, new_position, orientation, (position, orientation)

        for new_orientation in [(orientation + 1) % 4, (orientation - 1) % 4]:
            if not self.grid.get(self.grid.change_position(position, self.DELTAS[new_orientation]), True):
                yield score + 1000, position, new_orientation, (position, orientation)

    def end_condition(self, state) -> bool:
        score, position, orientation, last_position = state
        if self.solutions and score > self.solutions[0][0]:
            return True
        if position != self.end:
            return False
        self.solutions.append(state)
        return False


class Level(AdventOfCode):
    part_one_test_solution = 11048
    part_two_test_solution = 64

    def preprocess_input(self, lines):
        grid = array([tuple(line) for line in lines])
        start = tuple(map(lambda p: p[0], np.where(grid == 'S')))
        end = tuple(map(lambda p: p[0], np.where(grid == 'E')))
        grid[start] = '.'
        grid[end] = '.'
        return array(grid == '#'), start, end

    def part_one(self, grid: SmartArray, start, end) -> int:
        search = Search(grid, start, end)
        search()
        return search.solutions[0][0]

    def part_two(self, grid, start, end) -> int:
        search = Search(grid, start, end)
        search()
        to_explore = deque([(end, i) for i in range(4)])
        paths = set(to_explore)
        while to_explore:
            state = to_explore.pop()
            for previous_state in search.visited_positions.get(state, (None, {}))[1]:
                if previous_state not in paths:
                    paths.add(previous_state)
                    to_explore.append(previous_state)
        return len(set(p for p, o in paths))


if __name__ == '__main__':
    Level().run()
