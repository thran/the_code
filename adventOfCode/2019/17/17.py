from collections import defaultdict
from random import choice

import numpy as np

from intcode import IntCode


class Droid:
    def __init__(self):
        self.field = defaultdict(int)
        self.x, self.y = None, None
        self.direction = None

        memory = list(map(int, open('input.txt').readlines()[0].split(',')))

        outputs = IntCode(list(memory)).run(halt_on_missing_input=True)
        self.process_view(outputs)

        memory[0] = 2
        self.droid = IntCode(memory)


    def get_next_position(self, direction, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y

        if direction == 0:
            return x, y - 1
        elif direction == 1:
            return x + 1, y
        elif direction == 2:
            return x, y + 1
        elif direction == 3:
            return x - 1, y

    def step(self, direction):
        pass

    def run(self, main, A, B, C):
        instructions = map(ord, f'{main}\n{A}\n{B}\n{C}\nn\n')
        outputs = self.droid.run(inputs=instructions, halt_on_missing_input=True)
        return outputs

    def process_view(self, view):
        row, col = 0, 0
        ps = ''
        for v in view:
            p = chr(v)
            ps += p
            if p == '\n':
                row += 1
                col = 0
                continue
            if p == '.':
                self.field[(col, row)] = 0
            elif p == '#':
                self.field[(col, row)] = 1
            else:
                self.field[(col, row)] = 1
                self.x, self.y = col, row
                if p == '^':
                    self.direction = 0
                elif p == '>':
                    self.direction = 1
                elif p == 'v':
                    self.direction = 2
                elif p == '<':
                    self.direction = 3
                else:
                    assert False
            col += 1

    def search_unknown(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        visited = {(x, y): None}
        steps = 0
        next = {(x, y)}
        found = False
        while len(next) > 0 and not found:
            new = set()
            for x, y in sorted(next):
                for d in [0, 1, 2, 3]:
                    nx, ny = self.get_next_position(d, x ,y)
                    if (nx, ny) in visited:
                        continue
                    if (nx, ny) not in self.field:
                        visited[(nx, ny)] = x, y
                        found = nx, ny
                        continue
                    if self.field[(nx, ny)] == 1:
                        continue
                    visited[(nx, ny)] = x, y
                    new.add((nx, ny))
            next = new
            steps += 1

        if found:
            position = found
            path = []
            while visited[position] is not None:
                x, y = position
                nx, ny = visited[position]
                if nx > x:
                    path.append(3)
                elif nx < x:
                    path.append(1)
                elif ny < y:
                    path.append(2)
                elif ny > y:
                    path.append(0)
                position = nx, ny
            return path[::-1]
        return steps -1

    def show(self):
        xs = [i for i, j in self.field.keys()]
        ys = [j for i, j in self.field.keys()]
        for y in range(min(ys), max(ys) + 1):
            row = ''
            for x in range(min(xs), max(xs) + 1):
                if self.x == x and self.y == y:
                    row += '^>v<'[self.direction]
                    continue
                o = self.field.get((x, y), -1)
                if o == 0:
                    row += '.'
                elif o == 1:
                    row += '#'
                else:
                    row += '?'
            print(row)
        print()

    def intersections(self):
        xs = [i for i, j in self.field.keys()]
        ys = [j for i, j in self.field.keys()]
        s = 0
        for y in range(min(ys), max(ys) + 1):
            for x in range(min(xs), max(xs) + 1):
                if \
                    self.field.get((x+1, y), 0) == 1 and \
                    self.field.get((x, y+1), 0) == 1 and \
                    self.field.get((x-1, y), 0) == 1 and \
                    self.field.get((x, y-1), 0) == 1 and self.field.get((x, y), 0) == 1:
                    s += x * y
        return s

    def get_path(self):
        path = []
        steps = 0
        while True:
            if self.field[self.get_next_position(self.direction)] == 1:
                steps += 1
                self.x, self.y = self.get_next_position(self.direction)
                continue
            if steps > 0:
                path.append(steps)
                steps = 0
            if self.field[self.get_next_position((self.direction + 1) % 4)] == 1:
                self.direction = (self.direction + 1 ) % 4
                path.append('R')
                continue
            if self.field[self.get_next_position((self.direction - 1) % 4)] == 1:
                self.direction = (self.direction - 1) % 4
                path.append('L')
                continue
            break
        return path


d = Droid()
# d.run()
d.show()
# print(d.intersections())
path = d.get_path()

C = 'R,4,R,10,R,8,R,4'
A = 'R,4,L,12,R,6,L,12'
B = 'R,10,R,6,R,4'
main = ','.join(map(str, path)) \
            .replace(C, 'C') \
            .replace(A, 'A') \
            .replace(B, 'B')

print(d.run(main, A, B, C))

