import heapq
from tqdm import tqdm
import numpy as np


class Map:
    def __init__(self, tx, ty, depth):
        self.depth = depth
        self.tx = tx
        self.ty = ty
        self.modulo = 20183

        self.map = np.zeros((tx + 2000, ty + 500))

        self.erosion_level()
        self.map = self.EL % 3

    def erosion_level(self):
        self.EL = np.zeros(self.map.shape, dtype=int)

        for x in range(self.map.shape[0]):
            for y in range(self.map.shape[1]):
                if (x == 0 and y == 0) or (x == tx and y == ty):
                    value = 0
                elif x == 0:
                    value = y * 48271
                elif y == 0:
                    value = x * 16807
                else:
                    value = self.EL[x - 1, y] * self.EL[x, y - 1]
                self.EL[x, y] = (value + self.depth) % self.modulo
        self.EL %= self.modulo

    def search(self):
        # 0 = torch
        # 1 = climb
        # 2 = nothing
        pass
        heap = []
        visited = set()
        heapq.heappush(heap, (0, 0, 0, 0))
        paths = {}

        with tqdm() as t:
            while True:
                time, x, y, g = heapq.heappop(heap)
                # print(time, x, y, g, visited)
                if (x, y, g) in visited:
                    # print('cont')
                    continue
                visited.add((x, y, g))
                t.update(time - t.n)

                if x == self.tx and y == self.ty and g == 0:
                    print(time)
                    break

                for dx, dy, in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0:
                        continue

                    if (self.map[nx, ny] - 1) % 3 == g:
                        continue

                    heapq.heappush(heap, (time + 1, nx, ny, g))
                    paths[(nx, ny, g)] = x, y, g

                for ng in [0, 1, 2]:
                    if ng == g:
                        continue
                    if (self.map[x, y] - 1) % 3 == ng:
                        continue
                    heapq.heappush(heap, (time + 7, x, y, ng))
                    paths[(x, y, ng)] = x, y, g
        return paths

    def __str__(self):
        r = ''
        for x in range(self.map.shape[0]):
            for y in range(self.map.shape[1]):
                if self.map[x, y] == 0:
                    r += '.'
                if self.map[x, y] == 1:
                    r += '='
                if self.map[x, y] == 2:
                    r += '|'
            r += '\n'
        return r


depth = 510
tx, ty = 10, 10

depth = 3198
tx, ty = 12, 757


m = Map(tx, ty, depth)
# print(m.EL.T)
# print(m)
print(m.map[:tx +1, :ty+1].sum().sum())
paths = m.search()

exit()

c = paths[(tx, ty, 0)]
print(c)
while c != (0, 0, 0):
    print(c)
    c = paths[c]
