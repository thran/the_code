import re
from collections import defaultdict

import numpy as np


def hsh(p):
    return ''.join(v for r in p for v in r)


patterns = {}
with open('input.txt') as pattern:
    for line in pattern:
        pattern, target = line.strip().split(' => ')
        pattern = np.array(list(map(list, pattern.split('/'))))
        target = np.array(list(map(list, target.split('/'))))
        for transformed_pattern in [pattern, pattern.T]:
            for _ in range(4):
                transformed_pattern = np.rot90(transformed_pattern)
                patterns[hsh(transformed_pattern)] = target

M = np.array(list(map(list, ['.#.', '..#', '###'])))

for _ in range(18):
    if M.shape[0] % 2 == 0:
        N = np.empty((M.shape[0] // 2 * 3, M.shape[0] // 2 * 3), dtype=str)
        for x in range(M.shape[0] // 2):
            for y in range(M.shape[0] // 2):
                n = patterns[hsh(M[x * 2: (x + 1) * 2, y * 2: (y + 1) * 2])]
                N[x * 3: (x + 1) * 3, y * 3: (y + 1) * 3] = n
    else:
        N = np.empty((M.shape[0] // 3 * 4, M.shape[0] // 3 * 4), dtype=str)
        for x in range(M.shape[0] // 3):
            for y in range(M.shape[0] // 3):
                n = patterns[hsh(M[x * 3: (x + 1) * 3, y * 3: (y + 1) * 3])]
                N[x * 4: (x + 1) * 4, y * 4: (y + 1) * 4] = n

    M = N

print((M == '#').sum())
