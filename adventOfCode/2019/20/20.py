from collections import defaultdict
from operator import itemgetter
from random import choice

import numpy as np
from tqdm import tqdm

from utils import memoize


class Field:

    def __init__(self):
        self.data = []
        self.portals = {}
        self.portals_rev = defaultdict(list)
        with open('input.txt') as f:
            for row, line in enumerate(f):
                r = []
                self.data.append(r)
                for col, s in enumerate(line.replace('\n', '')):
                    r.append(s)
        self.data = np.array(self.data).T

        for x, column in enumerate(self.data):
            for y, s in enumerate(column):
                if s not in '.# ':
                    if any(self.get_next_symbol(d, x, y) == '.' for d in [0, 1, 2, 3]):
                        for d in [0, 1, 2, 3]:
                            n = self.get_next_symbol(d, x, y)
                            if n not in '#. ':
                                port = ''.join(sorted([s, n]))
                            if n == '.':
                                nx, ny = self.get_next_position(d, x, y)
                        is_outer = x == 1 or x == self.data.shape[0] - 2 or y == 1 or y == self.data.shape[1] - 2
                        self.portals[(nx, ny)] = port, (-1 if is_outer else 1)
                        self.portals_rev[port].append((nx, ny))
        print(self.portals)

    def show(self):
        for row in self.data.T:
            p = ''
            for s in row:
                p += s
            print(p)

    def get_next_position(self, direction, x, y):
        if direction == 0:
            return x, y - 1
        elif direction == 1:
            return x + 1, y
        elif direction == 2:
            return x, y + 1
        elif direction == 3:
            return x - 1, y

    def get_next_symbol(self, direction, x, y):
        x, y = self.get_next_position(direction, x, y)
        if x < 0 or y < 0 or x >= self.data.shape[0] or y >= self.data.shape[1]:
            return None
        return self.data[x, y]

    def is_free(self, x, y):
        s = self.data[x, y]
        if s == '.':
            return True
        if s == '#':
            return False
        if s == ' ':
            assert False
        assert x, y in self.portals
        return False

    def neighbours(self, x, y, z):
        for d in [0, 1, 2, 3]:
            nx, ny = self.get_next_position(d, x, y)
            if self.is_free(nx, ny):
                yield nx, ny, z
        if (x, y) in self.portals:
            portal, dz = self.portals[(x, y)]
            for nx, ny in self.portals_rev[portal]:
                if (x, y) != (nx, ny) and z + dz >= 0:
                    yield nx, ny, z + dz

    def shortest_path(self, start, end):
        visited = {start: None}
        steps = 0
        next = {start}
        while len(next) > 0:
            new = set()
            for position in sorted(next):
                for new_position in self.neighbours(*position):
                    if new_position in visited:
                        continue
                    visited[new_position] = position
                    new.add(new_position)
                    if new_position == end:
                        return steps + 1
            next = new
            steps += 1


field = Field()
field.show()
# print(' | '.join(map(str, field.neighbours(2, 15, 0))))
print(field.shortest_path(field.portals_rev['AA'][0] + (0, ), field.portals_rev['ZZ'][0] + (0, )))
