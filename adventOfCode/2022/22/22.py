import inspect
from collections import defaultdict
from itertools import product

import numpy as np

from core import AdventOfCode

cube_test = '''
    12  
    34  
211334  
655778  
    7884
    5662
'''

cube = '''
  1226
  3448
  34  
  78  
3778  
1556  
15    
26    
'''


class Level(AdventOfCode):
    part_one_test_solution = 6032
    part_two_test_solution = 5031
    strip_only_new_lines = True

    def preprocess_input(self, lines):
        map_ = lines[:-2]
        width = max(len(l) for l in map_)
        map_ = np.array([[-1 if t == ' ' else 0 if t == '.' else 1 for t in l] + [-1] * (width - len(l)) for l in map_])

        path = []
        number = 0
        for part in lines[-1]:
            if part in 'LR':
                path.append(number)
                number = 0
                path.append(part)
            else:
                number = number * 10 + int(part)
        path.append(number)

        return map_, path

    def init(self, map_, skips=None, size=None):
        self.map = map_
        self.orientation = 0
        self.position = 0, list(self.map[0]).index(0)
        self.skips = skips
        self.size = size

    def get_next_position(self, x, y):
        nx, ny = x, y
        if self.orientation == 0:
            ny += 1
        if self.orientation == 1:
            nx += 1
        if self.orientation == 2:
            ny -= 1
        if self.orientation == 3:
            nx -= 1

        if self.skips:
            if not (0 <= nx < self.map.shape[0] and 0 <= ny < self.map.shape[1]) or self.map[nx, ny] == -1:
                for condition, edge1, edge2 in self.skips:
                    if condition(x, y):
                        return (
                            self.skip_over_edge((x, y), edge1, edge2),
                            (self.get_edge_orientation(edge2, self.size) + 2) % 4,
                        )
                else:
                    assert False

        nx, ny = nx % self.map.shape[0], ny % self.map.shape[1]
        if self.map[nx, ny] == -1:
            return self.get_next_position(nx, ny)
        return (nx, ny), self.orientation

    def go(self, path):
        for command in path:
            if command == 'L':
                self.orientation = (self.orientation - 1) % 4
                continue
            if command == 'R':
                self.orientation = (self.orientation + 1) % 4
                continue
            for _ in range(command):
                new_position, new_orientation = self.get_next_position(*self.position)
                if self.map[new_position] == 1:
                    break
                self.position = new_position
                self.orientation = new_orientation

    def get_password(self):
        return 1000 * (self.position[0] + 1) + 4 * (self.position[1] + 1) + self.orientation

    @staticmethod
    def scale_edge(edge, size):
        (x1, y1), (x2, y2) = edge
        return (
            ((x1 // 2 + x1 % 2) * size - x1 % 2, (y1 // 2 + y1 % 2) * size - y1 % 2),
            ((x2 // 2 + x2 % 2) * size - x2 % 2, (y2 // 2 + y2 % 2) * size - y2 % 2),
        )

    @staticmethod
    def get_on_edge_condition(edge):
        (x1, y1), (x2, y2) = edge
        return lambda x, y: min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    @staticmethod
    def get_edge_orientation(edge, size):
        (x1, y1), (x2, y2) = edge
        if x1 == x2:
            return 3 if x1 % size == 0 else 1
        else:
            return 2 if y1 % size == 0 else 0

    @staticmethod
    def skip_over_edge(position, edge1, edge2):
        def iterate_edge(edge):
            (x1, y1), (x2, y2) = edge
            position = list(product(range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)))
            if x1 < x2 or y1 < y2:
                return position
            return position[::-1]

        for p1, p2 in zip(iterate_edge(edge1), iterate_edge(edge2)):
            if position == p1:
                return p2
        assert False

    def get_cube_skips(self, cube, size):
        cube = np.array([list(map(int, l)) for l in cube.replace(' ', '0').split('\n') if l])
        edges = defaultdict(list)
        for x in range(cube.shape[0] // 2):
            for y in range(cube.shape[1]):
                if cube[2 * x, y]:
                    v1, v2 = cube[2 * x, y], cube[2 * x + 1, y]
                    if v1 < v2:
                        edges[v1, v2].append(self.scale_edge(((2 * x, y), (2 * x + 1, y)), size))
                    else:
                        edges[v2, v1].append(self.scale_edge(((2 * x + 1, y), (2 * x, y)), size))

        for x in range(cube.shape[0]):
            for y in range(cube.shape[1] // 2):
                if cube[x, 2 * y]:
                    v1, v2 = cube[x, 2 * y], cube[x, 2 * y + 1]
                    if v1 < v2:
                        edges[v1, v2].append(self.scale_edge(((x, 2 * y), (x, 2 * y + 1)), size))
                    else:
                        edges[v2, v1].append(self.scale_edge(((x, 2 * y + 1), (x, 2 * y)), size))
        skips = []
        for name, (edge1, edge2) in edges.items():
            skips.append((self.get_on_edge_condition(edge1), edge1, edge2))
            skips.append((self.get_on_edge_condition(edge2), edge2, edge1))

        return skips

    def part_one(self, map_, path) -> int:
        self.init(map_)
        self.go(path)
        return self.get_password()

    def part_two(self, map_, path) -> int:
        if map_.shape[0] < 50:
            size = 4
            skips = self.get_cube_skips(cube_test, size)
        else:
            size = 50
            skips = self.get_cube_skips(cube, size)
        self.init(map_, skips, size)
        self.go(path)
        return self.get_password()


Level().run()
