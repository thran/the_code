from random import choice

import numpy as np

from intcode import IntCode


class Droid:
    def __init__(self):
        memory = list(map(int, open('input.txt').readlines()[0].split(',')))
        self.droid = IntCode(memory)
        self.field = {(0, 0): 0}
        self.x, self.y = 0, 0

        self.DIRECTION_MAP = {
            0: 1,
            1: 4,
            2: 2,
            3: 3,
        }

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
        for d in [0, 1, 2, 3]:
            if self.get_next_position(d) not in self.field:
                output = self.droid.run(inputs=[self.DIRECTION_MAP[d]], halt_on_output=True)
                if output == 0:
                    self.field[self.get_next_position(d)] = 1
                if output in [1, 2]:
                    assert self.droid.run(inputs=[self.DIRECTION_MAP[(d + 2) % 4]], halt_on_output=True) == 1
                    self.field[self.get_next_position(d)] = 0 if output == 1 else 2

        output = self.droid.run(inputs=[self.DIRECTION_MAP[direction]], halt_on_output=True)
        if output == 0:
            return output
        if output in [1, 2]:
            self.x, self.y = self.get_next_position(direction)
        return output

    def run(self):
        last_direction = None
        while True:
            # options = [v for v in [0, 1, 2, 3] if self.get_next_position(v) not in self.field and (v + 2) % 2 == last_direction ]
            # if not options:
            #     options = [0, 1, 2, 3]
            # direction = choice(options)
            path = self.search_unknown()
            if type(path) is int:
                break
            for direction in path:
                output = self.step(direction)

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
                    row += 'D'
                    continue
                if x == 0 and y == 0:
                    row += 'X'
                    continue
                o = self.field.get((x, y), -1)
                if o == 0:
                    row += ' '
                elif o == 1:
                    row += '#'
                elif o == 2:
                    row += 'O'
                else:
                    row += '?'
            print(row)
        print()


d = Droid()
d.run()
d.show()

x, y = [(x, y) for (x, y), v in d.field.items() if v == 2][0]
print(x, y)
print(d.search_unknown(x, y))
