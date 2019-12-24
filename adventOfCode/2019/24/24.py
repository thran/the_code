from collections import defaultdict

import numpy as np


class Field:
    def __init__(self, size):
        self.size = size
        self.field = defaultdict(lambda: np.zeros((self.size, self.size)))
        with open('input.txt') as f:
            for r, line in enumerate(f):
                for c, s in enumerate(line.strip()):
                    if s == '#':
                        self.field[0][r,c] = 1

    def show(self, z=0):
        for row in self.field[-z]:
            r = ''
            for s in row:
                r += '#' if s else '.'
            print(r)
        print()

    def neighbours(self, x, y, z):
        if x == 0:
            yield 1, 2, z + 1
        elif x == 3 and y == 2:
            for i in range(5):
                yield 4, i, z - 1
        else:
            yield x - 1, y, z

        if y == 0:
            yield 2, 1, z + 1
        elif y == 3 and x == 2:
            for i in range(5):
                yield i, 4, z - 1
        else:
            yield x, y - 1, z

        if x == 4:
            yield 3, 2, z + 1
        elif x == 1 and y == 2:
            for i in range(5):
                yield 0, i, z - 1
        else:
            yield x + 1, y, z

        if y == 4:
            yield 2, 3, z + 1
        elif y == 1 and x == 2:
            for i in range(5):
                yield i, 0, z - 1
        else:
            yield x, y + 1, z

    def tick(self):
        new = defaultdict(lambda: np.zeros((self.size, self.size)))
        for z in range(min(self.field.keys()) - 1, max(self.field.keys()) + 2):
            for x in range(self.size):
                for y in range(self.size):
                    if x == 2 and y == 2:
                        continue
                    s = 0
                    for nx, ny, nz in self.neighbours(x, y, z):
                        if self.field[nz][nx, ny] == 1:
                            s += 1
                        assert nx != 2 or ny != 2
                    if self.field[z][x, y] == 1 and s == 1:
                        new[z][x, y] = 1
                    if self.field[z][x, y] == 0 and (s == 1 or s == 2):
                        new[z][x, y] = 1
        self.field = new

    def rating(self):
        r = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.field[x, y]:
                    r += 2 ** (x * self.size + y)
        return r

    def run(self):
        ratings = {self.rating()}
        while True:
            self.tick()
            r = self.rating()
            if r in ratings:
                print(r)
                break
            ratings.add(r)

        self.show()

    def run2(self, n):
        for _ in range(n):
            self.tick()


net = Field(5)
net.run2(200)
# for i in range(-5, 6):
#     net.show(i)
print(sum(f.sum() for z, f in net.field.items()))
