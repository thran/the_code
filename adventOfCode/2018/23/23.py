import re
from itertools import product, combinations

import pandas as pd
import numpy as np
from tqdm import tqdm
import seaborn as sns
import pylab as plt

data = []
with open('input.txt') as f:
    for line in f:
        x, y, z, r = re.match('pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)', line.strip()).groups()
        data.append({
            'x': int(x),
            'y': int(y),
            'z': int(z),
            'r': int(r),
        })


def in_range(x, y, z):
    return np.absolute(coords - [x, y, z]).sum(axis=1) <= df.r


def search_around(x, y, z, epsilon=10):
    res = []
    for dx, dy, dz in tqdm(product(*[range(-epsilon, epsilon + 1)] * 3)):
        nx, ny, nz = x + dx, y + dy, z + dz
        res.append((-in_range(nx, ny, nz), nx + ny + nz))
        print(nx, ny, nz, in_range(nx, ny, nz), nx + ny + nz)

    return(min(res))


def dist(x, y, z):
    return abs(x) + abs(y) + abs(z)


def get_V(sel):
    if type(sel) != pd.DataFrame:
        sel = df[sel]

    best = None
    for da, db, dc in product(*([[1, -1]] * 3)):

        fa = max if da == 1 else min
        fb = max if db == 1 else min
        fc = max if dc == 1 else min

        c = fa(sel.z + sel.x + sel.y - da * sel.r)
        b = fb(sel.z - sel.x + sel.y - db * sel.r)
        # d = max(sel.z + sel.x - sel.y - sel.r)
        a = fc(sel.z - sel.x - sel.y - dc * sel.r)

        m = (c - b) / 2, (b - a) / 2, (c + a) / 2
        if in_range(*m).sum() < len(sel):
            continue
        if int(m[0]) != m[0] or int(m[1]) != m[1] or int(m[1]) != m[1]:
            continue
        if best is None or dist(*m) < dist(*best):
            best = m
    return best




# blacklist = [131, 692, 560, 292, 612, 318, 944, 269, 291, 427, 237, 89, 520, 24, 831, 263, 781, 656, 482]
df = pd.DataFrame(data)
# df = df[~df.index.isin(blacklist)]
coords = df[['x', 'y', 'z']].values

s = 0
for d in tqdm(df.itertuples()):
    if d.r >= (abs(d.x - 54127927) + abs(d.y - 17023759) + abs(d.z - 30447854)):
        s += 1

print(s)


print(in_range(54127927, 17023759, 30447854).sum())


# print(df)


m = np.absolute(coords - (0.5 * 10 ** 8, 0.2 * 10 ** 8, 0.3 * 10 ** 8)).sum(axis=1) < 2 *10 ** 8
print(m.sum())
p = get_V(m)
print(p)
print(sum(p), in_range(*p).sum())


if False:
    d = df[~m]

    for c in d.itertuples():
        plt.plot(c.x, c.y, '.')
        plt.plot([c.x - c.r, c.x, c.x + c.r, c.x, c.x - c.r],
                    [c.y, c.y - c.r, c.y, c.y + c.r, c.y],)
        plt.text(c.x, c.y, c.Index)
    # plt.show()

if False:
    d = df[m]

    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.plot(d.x, d.y, '.b')
    plt.plot(p[0], p[1], '.r')
    plt.subplot(132)
    plt.plot(d.x, d.z, '.b')
    plt.plot(p[0], p[2], '.r')
    plt.subplot(133)
    plt.plot(d.y, d.z, '.b')
    plt.plot(p[1], p[2], '.r')
    plt.show()

    exit()


if True:

    counts = []
    for x, y, z, r in tqdm(df[['x', 'y', 'z', 'r']].sort_values('r', ascending=False).values):
        counts.append((np.absolute(coords - [x, y, z]).sum(axis=1) <= r).sum())


    res = []
    with tqdm() as t:
    #     for i, j in combinations(np.argsort(counts)[::-1], 2):
        while True:
            i, j, k = np.random.randint(0, 999, 3)
            t.update(1)
            sel = df.loc[[i, j]]
            p = get_V(sel)
            if p is None:
                continue
            res.append((-sum(in_range(*p)), sum(p)))
            if t.n % 1000 == 0:
                print(min(res))

    print(min(res))

    exit()

# x, y, z = map(int, np.average(coords, axis=0, weights=1 / df.r))
# x, y, z = 0, 0, 0
# mask = in_range(x, y, z)
mask = m
print(get_V(mask), sum(get_V(mask)))

while True:
    res = {}
    for i, v in enumerate(mask):
        if v:
            continue
        mask[i] = True
        p = get_V(mask)
        if p is None:
            continue
        print(sum(p), in_range(*p).sum())
        m = in_range(*p)
        # print(i, m.sum(), (mask == m).sum(), np.argmin((mask == m)))
        res[m.sum()] = m
        mask[i] = False

    new_mask = res[max(res)]
    if new_mask.sum() == mask.sum():
        break
    mask = new_mask

print(get_V(mask), sum(get_V(mask)))
