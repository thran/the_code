from itertools import chain

import numpy as np

from adventOfCode.utils import array, SmartArray
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 10092
    part_two_test_solution = 9021

    def preprocess_input(self, lines):
        space = lines.index('')
        grid = array([tuple(line) for line in lines[:space]])
        instructions = lines[space + 1 :]
        position = tuple(map(lambda p: p[0], np.where(grid == '@')))
        grid[position] = '.'
        return grid, position, instructions

    def move(self, grid: SmartArray, robot, delta):
        position = robot
        while True:
            position = grid.change_position(position, delta)
            if grid[position] == '#':
                return robot
            if grid[position] == 'O':
                continue
            assert grid[position] == '.'
            new_position = grid.change_position(robot, delta)
            if new_position != position:
                grid[position] = 'O'
                grid[new_position] = '.'
            return new_position

    def GPS_count(self, grid):
        result = 0
        for x, y in np.transpose(np.where((grid == 'O') | (grid == '['))):
            result += 100 * x + y
        return result

    def part_one(self, grid: SmartArray, position, instructions) -> int:
        for instruction in chain(*instructions):
            position = self.move(grid, position, SmartArray.DIRECTIONS[instruction])
        return self.GPS_count(grid)

    def expand_grid(self, grid, position):
        expansion = {
            '.': '..',
            '#': '##',
            'O': '[]',
        }
        return array([tuple(''.join(map(expansion.get, line))) for line in grid]), (position[0], position[1] * 2)

    def check_position(self, grid, position, delta) -> bool:
        content = grid[position]
        if content == '.':
            return True
        if content == '#':
            return False
        next_position = grid.change_position(position, delta)
        if delta[0] == 0:
            return self.check_position(grid, next_position, delta)

        next_position_side = grid.change_position(next_position, (0, -1 if content == ']' else 1))
        return self.check_position(grid, next_position, delta) and self.check_position(grid, next_position_side, delta)

    def move_to(self, grid, position, delta):
        content = grid[position]
        assert content != '#'
        if content == '.':
            return
        next_position = grid.change_position(position, delta)
        if delta[0] == 0:
            self.move_to(grid, next_position, delta)
            grid[next_position] = content
            grid[position] = '.'
            return

        next_position_side = grid.change_position(next_position, (0, -1 if content == ']' else 1))
        self.move_to(grid, next_position, delta)
        self.move_to(grid, next_position_side, delta)
        grid[next_position] = content
        grid[position] = '.'
        position_side = grid.change_position(position, (0, -1 if content == ']' else 1))
        grid[next_position_side] = grid[position_side]
        grid[position_side] = '.'

    def part_two(self, grid: SmartArray, position, instructions) -> int:
        grid, position = self.expand_grid(grid, position)
        for instruction in chain(*instructions):
            delta = SmartArray.DIRECTIONS[instruction]
            new_position = grid.change_position(position, delta)
            if self.check_position(grid, new_position, delta):
                self.move_to(grid, new_position, delta)
                position = new_position
        return self.GPS_count(grid)


if __name__ == '__main__':
    Level().run()
