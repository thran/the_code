import numpy as np

data = []
with open('input.txt') as f:
    for line in f:
        data.append(list(line[:-1]))

data = np.array(data)

d = data[:, 0] != ' '
if d.sum() > 0:
    for i, v in enumerate(d):
        if v:
            x, y = i, 0
            direction = 1
            break
d = data[:, -1] != ' '
if d.sum() > 0:
    for i, v in enumerate(d):
        if v:
            x, y = i, data.shape[1] - 1
            direction = 3
            break
d = data[0, :] != ' '
if d.sum() > 0:
    for i, v in enumerate(d):
        if v:
            x, y = 0, i
            direction = 2
            break
d = data[-1, :] != ' '
if d.sum() > 0:
    for i, v in enumerate(d):
        if v:
            x, y = data.shape[0], i
            direction = 3
            break

move = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


def m(p, d):
    x, y = p
    dx, dy = move[d]
    return x + dx, y + dy


print(x, y, direction)


found = ''
current = x, y
steps = 1
while True:
    new = m(current, direction)
    v = data[new]
    if v == ' ':
        for dd in [-1, 1]:
            nd = (direction + dd) % 4
            if data[m(current, nd)] != ' ':
                direction = nd
                break
        else:
            break
        continue
    if v not in '|-+':
        found += v
    current = new
    steps += 1
    # print(new, data[new])

print(found, steps)
