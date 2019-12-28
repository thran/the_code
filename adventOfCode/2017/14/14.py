from itertools import product

import numpy as np

from hash import knot

rows = []
for row in range(128):
    h = knot(f'ugkiagan-{row}')
    rows.append([int(b) for b in f'{bin(int(h, 16))[2:]:0>128}'])

rows = np.array(rows)


def neighbours(data, x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if x + dx >= 0 and y + dy >= 0 and x + dx < len(data) and y + dy < len(data):
            yield x + dx, y + dy


def explore(data, node):
    visited = {node: None}
    next = {node}
    while next:
        new = set()
        for n in next:
            for x in neighbours(rows, *n):
                if data[x] == 0:
                    continue
                if x in visited:
                    continue
                visited[x] = n
                new.add(x)
        next = new
    return visited


print(rows)
print(rows.sum())


explored = set()
c = 0
while rows.sum() - len(explored):
    for x, y in product(range(len(rows)), range(len(rows))):
        if (x, y) not in explored and rows[x, y] == 1:
            break
    explored |= set(explore(rows, (x, y)).keys())
    c += 1
print(c)
