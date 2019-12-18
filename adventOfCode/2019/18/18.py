from operator import itemgetter
from random import choice

import numpy as np
from tqdm import tqdm


class Field:

    def __init__(self):
        self.data = []
        self.keys = {}
        with open('input.txt') as f:
            for row, line in enumerate(f):
                self.data.append([s for s in line.strip().replace('@', '.')])
                if '@' in line:
                    self.initial_x = line.index('@')
                    self.initial_y = row
                for col, s in enumerate(line.strip()):
                    if s.lower() == s and s not in '.#@':
                        self.keys[s] = col, row
        self.data = np.array(self.data).T

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

    def is_free(self, x, y, keys):
        s = self.data[x, y]
        if s == '.':
            return True
        if s == '#':
            return False
        if s.lower() == s:
            return True
        if s.upper() == s:
            return s.lower() in keys
        assert False

    def is_key(self, x, y):
        s = self.data[x, y]
        if s == '.':
            return False
        if s == '#':
            return False
        if s.lower() == s:
            return s
        return False

    def available_keys(self, x, y, keys):
        visited = {(x, y): None}
        steps = 0
        next = {(x, y)}
        available = {}
        while len(next) > 0:
            new = set()
            for x, y in sorted(next):
                k = self.is_key(x, y)
                if k and k not in keys:
                    available[k] = steps
                for d in [0, 1, 2, 3]:
                    nx, ny = self.get_next_position(d, x, y)
                    if (nx, ny) in visited:
                        continue
                    if not self.is_free(nx, ny, keys):
                        continue
                    visited[(nx, ny)] = x, y
                    new.add((nx, ny))
            next = new
            steps += 1
        return available


field = Field()
field.show()
# print(field.keys)
# print(field.available_keys(field.initial_x, field.initial_y, 'a'))

field.best = None


def solve(x=field.initial_x, y=field.initial_y, keys='', distance=0):
    if len(keys) == len(field.keys):
        if field.best is None or distance < field.best:
            field.best = distance
            print(field.best, keys)

    available = field.available_keys(x, y, keys)
    # print(x, y, len(field.keys) - len(keys), available, s)

    for k, d in sorted(available.items(), key=itemgetter(1)):
        nx, ny = field.keys[k]
        solve(nx, ny, keys + k, distance + d)

solve()
