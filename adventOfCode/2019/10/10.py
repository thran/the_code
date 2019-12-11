from collections import defaultdict
from math import gcd, sqrt

import numpy as np
import pandas as pd


def show(field):
    for row in field.T:
        print(''.join(['.' if v == 0 else '#' for v in row]))


def get_directions(field, x, y):
    directions = defaultdict(list)
    for i, col in enumerate(field):
        for j, value in enumerate(col):
            if value == 0 or (x == i and y == j):
                continue
            dx, dy = i - x, j - y
            cd = gcd(abs(dx), abs(dy))
            direction = dx // cd, dy // cd
            directions[direction].append((i, j))

    return directions


field = []
with open('input.txt') as f:
    for line in f:
        field.append([0 if x == '.' else 1 for x in line.strip()])

field = np.array(field).T
# show(field)

detects = {}
for i, col in enumerate(field):
    for j, value in enumerate(col):
        if value == 0:
            continue
        detects[(i, j)] = get_directions(field, i, j)


(bx, by), views = max(detects.items(), key=lambda x: len(x[1]))

print(bx, by, len(views))

data = []
for direction, asteroids in views.items():
    distances = []
    for i, j in asteroids:
        dx, dy = i - bx, j - by
        distance = sqrt(dx ** 2 + dy ** 2)
        angel = (np.pi / 2 - np.arcsin(-dy / distance)) if dx >= 0 else (np.pi + np.arcsin(-dy / distance))
        data.append({
            'dx': dx,
            'dy': dy,
            'x': i,
            'y': j,
            'distance': distance,
            'angel': angel,
        })
        distances.append(distance)
    for i, idx in enumerate(np.argsort(distances)):
        data[-(len(distances) - idx)]['order'] = i

df = pd.DataFrame(data)

df = df.sort_values(['order', 'angel'])
df = df.reset_index()
print(df)

selected = df.ix[200 - 1]
print(selected)
print(selected['x'] * 100 + selected['y'])
