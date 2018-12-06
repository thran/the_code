import re

with open('22.txt') as f:
    nodes = {}
    for l in f.readlines():
        node = dict(zip(
            ['x', 'y', 'Size', 'Used', 'Avail'],
            map(int, re.search('node-x(\d+)-y(\d+) *(\d+)T *(\d+)T *(\d+)T ', l).groups())
        ))
        nodes[(node['x'], node['y'])] = '_' if node['Used'] == 0 else '#' if node['Used'] > 100 else '.'


def get_viables(nodes):
    viables = []
    for (ax, ay), (a_used, a_avail) in nodes.items():
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            bx, by = ax + dx, ay + dy
            if (bx, by) not in nodes:
                continue
            b_used, b_avail = nodes[(bx, by)]
            d = abs(ax - bx), abs(ay - by)
            if sorted(d) == [0, 1] and 0 < a_used <= b_avail:
                viables.append(((ax, ay), (bx, by)))
    return viables
directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}


moves = 0
target = (max(nodes.keys())[0], 0)
nodes[target] = 'G'
empty = [k for k, v in nodes.items() if v == '_'][0]

steps = 0
def move(direction):
    global empty, steps
    x, y = empty
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    if nodes[(nx, ny)] == '#':
        print('wall')
        exit()
    nodes[(x, y)], nodes[(nx, ny)] = nodes[(nx, ny)], nodes[(x, y)]
    empty = nx, ny
    steps += 1

# print(len(get_viables(nodes)))

for _ in range(7):
    move('U')
for _ in range(28):
    move('L')
for _ in range(33):
    move('D')
for _ in range(33):
    move('R')
    move('U')
    move('U')
    move('L')
    move('D')

for i in range(max(nodes.keys())[0] + 1):
    for j in range(max(nodes.keys())[1] + 1):
        print(nodes[(i, j)], end=' ')
    print()

print(steps)