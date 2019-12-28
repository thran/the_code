import re
from collections import defaultdict

data = []
with open('input.txt') as f:
    for line in f:
        parts = re.split('[<>]',line.strip())
        p = tuple(map(int, parts[1].split(',')))
        v = tuple(map(int, parts[3].split(',')))
        a = tuple(map(int, parts[5].split(',')))
        data.append((p, v, a))

by_a = defaultdict(list)
for i, (p, v, a) in enumerate(data):
    by_a[sum(map(abs, a))].append(i)

best_a = min(by_a)
for x in by_a[best_a]:
    print(x, data[x], sum(map(abs, data[x][1])))


while True:
    new = defaultdict(list)
    for i, (p, v, a) in enumerate(data):
        px, py, pz = p
        vx, vy, vz = v
        ax, ay, az = a
        nvx, nvy, nvz = vx + ax, vy + ay, vz + az
        npx, npy, npz = px + nvx, py + nvy, pz + nvz

        new[(npx, npy, npz)].append(((npx, npy, npz), (nvx, nvy, nvz), a))

    data = [d[0] for p, d in new.items() if len(d) == 1]
    print(len(data))
