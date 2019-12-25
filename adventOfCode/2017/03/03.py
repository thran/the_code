from collections import defaultdict

import numpy as np


def get_xy(i):
    base = 0
    while (base * 2 + 1) ** 2 < i:
        base += 1

    d = ((2 * base + 1) ** 2 - (2 * base - 1) ** 2) // 4
    s = (2 * base - 1) ** 2
    if i <= (s + 1 * d):
        x = base
        y = base - ((s + 1 * d) - i)
    elif i <= (s + 2 * d):
        y = base
        x = -base + ((s + 2 * d) - i)
    elif i <= (s + 3 * d):
        x = -base
        y = -base + ((s + 3 * d) - i)
    elif i <= (s + 4 * d):
        y = -base
        x = base - ((s + 4 * d) - i)
    return x, y


# print(d, s, base)
# print(x, y)
x, y = get_xy(277678)
print(abs(x) + abs(y))


numbers = defaultdict(int)
n = 0
while True:
    n += 1
    x, y = get_xy(n)
    v = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            v += numbers[(x + dx, y + dy)]
    if v == 0:
        v = 1
    numbers[(x, y)] = v
    print(n, x, y, v)
    if v > 277678:
        break
