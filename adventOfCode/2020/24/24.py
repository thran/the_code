# start 10:20, 1. 10:39, 2. 10:50
from collections import deque
from pathlib import Path


with Path('input.txt').open() as file:
    instructions = [line.strip() for line in file]


def instructions_to_position(instruction):
    instruction = list(instruction)
    x, y = 0, 0
    while instruction:
        c = instruction.pop(0)
        if c == 'w':
            y -= 1
            continue
        if c == 'e':
            y += 1
            continue
        c2 = instruction.pop(0)
        if c == 'n':
            x -= 1
            if c2 == 'e':
                y += 1
        if c == 's':
            x += 1
            if c2 == 'w':
                y -= 1

    return x, y


blacks = set()
for instruction in instructions:
    x, y = instructions_to_position(instruction)
    if (x, y) in blacks:
        blacks.remove((x, y))
    else:
        blacks.add((x, y))

print(len(blacks))


deltas = list(map(instructions_to_position, ('e', 'w', 'sw', 'nw', 'se', 'ne')))
def neighbours(x, y):
    for dx, dy, in deltas:
        yield x + dx, y + dy


def black_neighbours(position, blacks):
    for n in neighbours(*position):
        if n in blacks:
            yield n


for _ in range(100):
    new_blacks = set()

    for tile in blacks:
        if sum(1 for n in black_neighbours(tile, blacks)) in (1, 2):
            new_blacks.add(tile)

    candidates = set(n for tile in blacks for n in neighbours(*tile) if n not in blacks)
    for tile in candidates:
        if sum(1 for n in black_neighbours(tile, blacks)) == 2:
            new_blacks.add(tile)
    blacks = new_blacks

print(len(blacks))
