# start 8:30, 1. 8:45, 2. 9:00
from pathlib import Path

from parse import parse

with Path('input.txt').open() as file:
    instructions = []
    for line in file:
        result = parse('{instruction}{value:d}', line.strip())
        instructions.append((result['instruction'], result['value']))

directions = 'ESWN'
deltas = {
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1),
    'N': (1, 0),
}


direction = 0
x, y = 0, 0
for instruction, value in instructions:
    if instruction == 'F':
        instruction = directions[direction]

    if instruction in 'LR':
        rotation = value // 90 if instruction == 'R' else -value // 90
        direction = (direction + rotation) % len(directions)
        continue

    dx, dy = deltas[instruction]
    x += value * dx
    y += value * dy

print(abs(x) + abs(y))


x, y = 0, 0
wx, wy = 1, 10
for instruction, value in instructions:
    if instruction == 'F':
        x += value * wx
        y += value * wy
        continue

    if instruction in 'LR':
        rotation = value // 90 if instruction == 'R' else (-value // 90) % len(directions)
        for _ in range(rotation):
            wx, wy = -wy, wx
        continue

    dx, dy = deltas[instruction]
    wx += value * dx
    wy += value * dy


print(abs(x) + abs(y))
