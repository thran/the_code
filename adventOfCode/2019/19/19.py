from collections import defaultdict
from functools import partial
from random import choice

import numpy as np

from intcode import IntCode
from utils import binary_search

memory = list(map(int, open('input.txt').readlines()[0].split(',')))
size=100

def get_state(x, y):
    # print(x, y)
    system = IntCode(memory.copy())
    return int(system.run(inputs=[x, y])[0])


def get_x(y):
    _, l = binary_search(partial(get_state, y=y), 0.5, 1, upper_search_increment=lambda x: x + y // 10)
    # r, _ = binary_search(lambda x: 1-get_state(x, y), 0.5, l, upper_search_increment=lambda x: x + y // 5)
    # print(l, r)
    return l


def is_ok(y):
    x = get_x(y)
    return get_state(x + size - 1, y - size + 1)

# print(is_ok(15))
y = binary_search(is_ok, 0.5, 10)[1]


while y > 100:
    if is_ok(y):
        x = get_x(y)
        print(x, y, x * 10000 + y - size + 1)
    y -= 1


if False:
    size = 50
    map = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            map[x, y] = get_state(x, y)

    for row in map.T:
        o = ''
        for v in row:
            o += '.' if v == 0 else '#'
        print(o)
    print(map.sum())
