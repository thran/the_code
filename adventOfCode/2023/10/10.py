import numpy as np
from scipy.ndimage import convolve

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 8
    part_two_test_solution = 10
    PIPE_TYPES = {
        '|': 'NS',
        '-': 'WE',
        'L': 'NE',
        'J': 'NW',
        'F': 'SE',
        '7': 'SW',
    }
    RIGHTS = {
        'NS': [(0, -1)],
        'WE': [(1, 0)],
        'NE': [(1, -1), (1, 0), (0, -1)],
        'NW': [(-1, -1), (-1, 0), (0, -1)],
        'SE': [(1, 1), (1, 0), (0, 1)],
        'SW': [(-1, 1), (-1, 0), (0, 1)],
    }
    OPPOSITES = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

    def preprocess_input(self, lines):
        rows = []
        for i, line in enumerate(lines):
            row = []
            for j, s in enumerate(line):
                if s in self.PIPE_TYPES:
                    row.append(self.PIPE_TYPES[s])
                elif s == 'S':
                    start = i, j
                    row.append('S')
                else:
                    row.append('  ')
            rows.append(row)

        pipe = ''
        if start[0] > 0 and 'S' in rows[start[0] - 1][start[1]]:
            pipe += 'N'
        if start[0] < len(rows) - 1 and 'N' in rows[start[0] + 1][start[1]]:
            pipe += 'S'
        if start[1] > 0 and 'E' in rows[start[0]][start[1] - 1]:
            pipe += 'W'
        if start[1] < len(rows[0]) - 1 and 'W' in rows[start[0]][start[1] + 1]:
            pipe += 'E'
        assert len(pipe) == 2, pipe
        rows[start[0]][start[1]] = pipe
        return np.array(rows), start

    def find_loop(self, field, start):
        position = start
        direction = field[position][0]
        loop = {position}
        rights = np.zeros(field.shape, dtype=bool)
        while True:
            match direction:
                case 'N':
                    position = position[0] - 1, position[1]
                case 'S':
                    position = position[0] + 1, position[1]
                case 'W':
                    position = position[0], position[1] - 1
                case 'E':
                    position = position[0], position[1] + 1
            direction = field[position].replace(self.OPPOSITES[direction], '')

            # mark right side
            diffs = self.RIGHTS[field[position]]
            if direction == field[position][0]:  # we go in other direction
                diffs = [(d[0] * -1, d[1] * -1) for d in diffs]
            for right_diff in diffs:
                right_position = position[0] + right_diff[0], position[1] + right_diff[1]
                if 0 <= right_position[0] < field.shape[0] and 0 <= right_position[1] < field.shape[1]:
                    rights[right_position] = True

            if position == start:
                break
            loop.add(position)
        return loop, rights

    def part_one(self, field, start) -> int:
        return len(self.find_loop(field, start)[0]) // 2

    def part_two(self, field, start) -> int:
        loop, rights = self.find_loop(field, start)
        field = np.zeros(field.shape, dtype=int)
        for position in loop:
            field[position] = 1

        rights[field == 1] = False
        kernel = np.ones((3, 3), dtype=int)
        while True:
            growth = convolve(rights, kernel, mode='constant') & ~field & ~rights
            if growth.sum() == 0:
                break
            rights |= growth.astype(bool)

        return rights.sum()


if __name__ == '__main__':
    Level().run()
