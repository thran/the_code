from collections import defaultdict

from tqdm import tqdm

move = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


def show(field):
    xs = [i for i, j in field.keys()]
    ys = [j for i, j in field.keys()]
    for x in range(min(xs), max(xs) + 1):
        row = ''
        for y in range(min(ys), max(ys) + 1):
            row += field[x, y] + ' '
        print(row)
    print()


field = defaultdict(lambda: '.')
with open('input.txt') as f:
    for x, line in enumerate(f):
        s = len(line.strip()) // 2
        for y, v in enumerate(line.strip()):
            field[x, y] = v

x, y, direction = s, s, 0

bursts = 0
for i in tqdm(range(10000000)):
    v = field[x, y]
    if v == '#':
        direction = (direction + 1) % 4
        field[x, y] = 'F'
    elif v == 'F':
        direction = (direction - 2) % 4
        field[x, y] = '.'
    elif v == 'W':
        field[x, y] = '#'
        bursts += 1
    elif v == '.':
        direction = (direction - 1) % 4
        field[x, y] = 'W'

    dx, dy = move[direction]
    x, y = x + dx, y + dy

show(field)

print(bursts)
