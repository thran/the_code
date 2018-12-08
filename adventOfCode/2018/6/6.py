from itertools import product

import numpy as np

points = []
with open('input.txt') as f:
    for line in f:
        x, y = line.strip().split(', ')
        points.append((int(x), int(y)))


min_x = min([x for x, y in points])
min_y = min([y for x, y in points])

points = [(x - min_x, y - min_y) for x, y in points]
max_x = max([x for x, y in points])
max_y = max([y for x, y in points])


field = np.zeros((max_x + 1, max_y + 1), dtype=int)
field.fill(-1)

for i, (x, y) in enumerate(points):
    field[x, y] = i


def get_neighbors(field, x, y):
    neighbors = []
    sx, sy = field.shape
    for ox, oy in product([-1, 0, 1], [-1, 0, 1]):
        if (ox == 0 and oy == 0) or ox * oy != 0:
            continue
        if 0 <= x + ox < sx and 0 <= y + oy < sy:
            neighbors.append(field[x + ox, y + oy])
    return neighbors


def update(field):
    new_field = np.empty(field.shape, dtype=int)
    for x in range(field.shape[0]):
        for y in range(field.shape[1]):
            if field[x, y] != -1:
                new_field[x, y] = field[x, y]
                continue
            neighbors = get_neighbors(field, x, y)
            ns = set(neighbors) - {-1}
            if len(ns) > 1:
                new_field[x, y] = -2
            if len(ns) == 1:
                new_field[x, y] = list(ns)[0]
            if len(ns) == 0:
                new_field[x, y] = -1

    return new_field


if False:
    while -1 in field:
        field = update(field)

    print(field.T)

    border = set(field[:, 0]) | set(field[:, -1]) | set(field[0, :]) | set(field[-1, :])

    finite = set(range(len(points))) - border

    print(max([(field == i).sum() for i in finite]))


distances = np.zeros((max_x + 1, max_y + 1), dtype=int)
for x in range(field.shape[0]):
    for y in range(field.shape[1]):
        for px, py in points:
            distances[x, y] += abs(x - px) + abs(y - py)

print(distances < 10**4)
print((distances < 10**4).sum())
