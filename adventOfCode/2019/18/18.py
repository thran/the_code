from collections import defaultdict
from operator import itemgetter
from random import choice

import numpy as np
from tqdm import tqdm

from utils import memoize


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

    def is_free(self, x, y, keys, ignore_doors=False):
        s = self.data[x, y]
        if s == '.':
            return True
        if s == '#':
            return False
        if s.lower() == s:
            return True
        if s.upper() == s:
            return ignore_doors or s.lower() in keys
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

    def is_door(self, x, y):
        s = self.data[x, y]
        if s == '.':
            return False
        if s == '#':
            return False
        if s.upper() == s:
            return s
        return False

    def get_distances(self):
        self.distances = distances = {}
        self.doors = doors = {}
        for k, (x, y) in list(self.keys.items()) + [('@', (self.initial_x, self.initial_y))]:
            for k2, (d, ds) in self.available_keys(x, y, [k], get_doors=True).items():
                distances[(k, k2)] = d
                doors[(k, k2)] = ds
        return distances, doors

    def get_graph(self):
        x = self.initial_x
        y = self.initial_y
        visited = {(x, y): '@'}
        next = {(x, y)}
        while len(next) > 0:
            new = set()
            for x, y in sorted(next):
                for d in [0, 1, 2, 3]:
                    nx, ny = self.get_next_position(d, x, y)
                    if (nx, ny) in visited:
                        continue
                    if not self.is_free(nx, ny, {}, ignore_doors=True):
                        continue
                    k = self.is_key(x, y)
                    if k:
                        visited[(nx, ny)] = k
                    else:
                        visited[(nx, ny)] = visited[(x, y)]
                    new.add((nx, ny))
            next = new
        self.graph = {}
        for key, (x, y) in self.keys.items():
            self.graph[key] = visited[(x, y)]
        self.leaves = set(self.keys.keys()) - set(self.graph.values())
        return self.leaves

    def available_keys(self, x, y, keys, get_doors=False, fast=None):
        available = {}
        if fast:
            for key in self.keys.keys():
                if key == fast or key in keys:
                    continue
                if self.doors[(fast, key)] <= set(keys):
                    available[key] = self.distances[(fast, key)]
            return available

        visited = {(x, y): None}
        doors = defaultdict(set)
        steps = 0
        next = {(x, y)}
        while len(next) > 0:
            new = set()
            for x, y in sorted(next):
                k = self.is_key(x, y)
                if k and k not in keys:
                    available[k] = steps
                    if not get_doors:
                        continue
                for d in [0, 1, 2, 3]:
                    nx, ny = self.get_next_position(d, x, y)
                    if (nx, ny) == visited[(x, y)]:
                        continue
                    if (nx, ny) in visited:
                        continue
                    if not self.is_free(nx, ny, keys, ignore_doors=get_doors):
                        continue
                    if get_doors:
                        nd = doors[(x, y)]
                        d = self.is_door(nx, ny)
                        if d:
                            nd = nd | {d.lower()}
                        doors[(nx, ny)] = nd
                    visited[(nx, ny)] = x, y
                    new.add((nx, ny))
            next = new
            steps += 1
        if get_doors:
            return {k: (d, doors[self.keys[k]]) for k, d in available.items()}
        return available


field = Field()
field.show()
# print(field.keys)
# print(field.available_keys(field.initial_x, field.initial_y, set(field.keys.keys())))

field.best = None
field.get_distances()
field.get_graph()


@memoize
def solve(key='@', keys=''):
    if len(keys) == len(field.keys):
        return 0

    available = field.available_keys(None, None, keys, fast=key)

    options = []
    for k, d in available.items():
        options.append(d + solve(k, ''.join(sorted(keys + k))))
    return min(options)

print(solve())
print(field.best)

