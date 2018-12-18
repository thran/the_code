import re
import sys

import numpy as np


def pprint(field):
    for row in field.T:
        r = ''
        for f in row:
            if f == 0:
                r += ' '
            if f == 1:
                r += '#'
            if f == 2:
                r += '|'
            if f == 3:
                r += '~'
        print(r)


xs = []
ys = []
with open('input.txt') as f:
    for line in f:
        a, b, c = re.match(r'.=(\d+), .=(\d+)..(\d+)', line.strip()).groups()
        if line[0] == 'x':
            xs.append(int(a))
            ys.append(int(b))
            ys.append(int(c))
        if line[0] == 'y':
            ys.append(int(a))
            xs.append(int(b))
            xs.append(int(c))

# print(xs, ys)

x_offset = min(xs) - 2
y_offset = min(ys)
field = np.zeros((max(xs) + 5 - x_offset, max(ys) - y_offset + 1))


with open('input.txt') as f:
    for line in f:
        a, b, c = re.match(r'.=(\d+), .=(\d+)..(\d+)', line.strip()).groups()
        if line[0] == 'x':
            field[int(a) - x_offset, int(b) - y_offset:int(c) - y_offset + 1] = 1
        if line[0] == 'y':
            field[int(b) - x_offset:int(c) - x_offset + 1, int(a) - y_offset] = 1


def drop(x, y):
    if field[x, y] == 3 or field[x, y] == 2:
        return
    while field[x, y] == 0:
        assert field[x, y] < 2
        field[x, y] = 2
        y += 1
        if y >= field.shape[1] or field[x, y] == 2:
            return
    spread(x, y - 1)
    # pprint(field)


def spread(x, y):
    left = right = x
    left_drop, right_drop = False, False
    while field[left - 1, y] in [0, 2]:
        left -= 1
        if field[left, y + 1] == 0:
            left_drop = True
            break

    while field[right + 1, y] in [0, 2]:
        right += 1
        if field[right, y + 1] == 0:
            right_drop = True
            break

    if not left_drop and not right_drop:
        field[left:right+1, y] = 3
        spread(x, y - 1)
    else:
        field[left:right + 1, y] = 2
        if left_drop:
            drop(left, y + 1)
        if right_drop:
            drop(right, y + 1)


sys.setrecursionlimit(2000)
drop(500 - x_offset, 0)
pprint(field)


print((field > 1).sum())
print((field > 2).sum())
print(field.shape, x_offset)