from math import prod
from pathlib import Path

forest = list(map(lambda l: l.strip(), Path('input.txt').open().readlines()))


def get_hits(dx, dy):
    x, y = 0, 0
    hits = 0
    while x < len(forest):
        hits += 1 if forest[x][y % len(forest[x])] == '#' else 0
        x += dx
        y += dy
    return hits


print(get_hits(1, 3))

all_hits = []
for dx, dy in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    all_hits.append(get_hits(dx, dy))

print(prod(all_hits))
