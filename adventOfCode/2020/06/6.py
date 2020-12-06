# start 7:43, 1. 7:49, 2: 7:54
from collections import defaultdict
from pathlib import Path


groups = []
with Path('input.txt').open() as file:
    group = set()
    for line in file.readlines() + ['\n']:
        if not line.strip():
            groups.append(group)
            group = set()
            continue
        group |= set(line.strip())

print(sum(map(len, groups)))


groups = []
with Path('input.txt').open() as file:
    group = defaultdict(int)
    count = 0
    for line in file.readlines() + ['\n']:
        if not line.strip():
            groups.append([q for q, v in group.items() if v == count])
            group = defaultdict(int)
            count = 0
            continue

        count += 1
        for l in line.strip():
            group[l] += 1

print(sum(map(len, groups)))
