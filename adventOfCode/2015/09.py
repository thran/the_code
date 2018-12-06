import re
from collections import defaultdict
from itertools import permutations

import numpy as np

distances = defaultdict(lambda: {})

with open("09.txt") as source:
    for line in source.readlines():
        g = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
        distances[g[0]][g[1]] = int(g[2])
        distances[g[1]][g[0]] = int(g[2])

ds = []

for perm in permutations(distances.keys()):
    distance = 0
    for i, p in enumerate(perm[:-1]):
        distance += distances[p][perm[i+1]]
    print perm, distance
    ds.append(distance)

print min(ds), max(ds)
