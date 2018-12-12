import re

import numpy as np

initial_state = '###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#'
steps = 150
offset = steps + 2

breed = set()
with open('input.txt') as f:
    for line in f:
        pattern, result = re.match(r'(.....) => (.)', line.strip()).groups()
        if result == '#':
            breed.add(pattern)


field = np.zeros(len(initial_state) + 2 * offset)

for i, plant in enumerate(initial_state):
    if plant == '#':
        field[i + offset] = 1


def step(field):
    new_field = np.zeros(len(field))
    for i in range(len(field) - 4):
        if ''.join('#' if f  else '.' for f in field[i:i+5]) in breed:
            new_field[i+2] = 1
    return new_field


print(''.join('#' if f  else '.' for f in field))
for _ in range(steps):
    field = step(field)
    print(''.join('#' if f  else '.' for f in field))


s = 0
for i, plant in enumerate(field):
    if plant:
        s += i - offset

count = sum(field)
print(s + (50000000000 - steps) * count)
