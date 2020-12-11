# start 8:25, 1. 8:42, 2. 8:51
from collections import defaultdict
from itertools import product
from pathlib import Path


with Path('input.txt').open() as file:
    original_layout = list(map(list, [line.strip() for line in file]))


def print_layout(l):
    for row in l:
        print(''.join(row))


def count_neighbours(cx, cy, l, part_one=True):
    counts = defaultdict(int)
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if dx == 0 and dy == 0:
            continue

        if part_one:
            x, y = cx + dx, cy + dy
            if 0 <= x < len(l) and 0 <= y < len(l[0]):
                counts[l[x][y]] += 1
        else:
            x, y = cx, cy
            while True:
                x += dx
                y += dy
                if 0 <= x < len(l) and 0 <= y < len(l[0]):
                    if layout[x][y] == '.':
                        continue
                    counts[l[x][y]] += 1
                    break
                else:
                    break

    return counts


for part_one in (True, False):
    layout = original_layout

    changed = True
    while changed:
        changed = False
        new_layout = []
        for x, row in enumerate(layout):
            new_row = []
            new_layout.append(new_row)
            for y, position in enumerate(row):
                if position == '.':
                    new_row.append('.')
                    continue

                neighbours = count_neighbours(x, y, layout, part_one=part_one)
                if position == 'L' and neighbours['#'] == 0:
                    new_row.append('#')
                    changed = True
                    continue

                if position == '#' and neighbours['#'] >= (4 if part_one else 5):
                    new_row.append('L')
                    changed = True
                    continue

                new_row.append(position)
        layout = new_layout

    print(sum(1 for row in layout for position in row if position == '#'))
