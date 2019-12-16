from itertools import repeat, islice, cycle

import numpy as np
from tqdm import tqdm

from utils import memoize

# raw = '03081770884921959731165446850517'
raw = '59708072843556858145230522180223745694544745622336045476506437914986923372260274801316091345126141549522285839402701823884690004497674132615520871839943084040979940198142892825326110513041581064388583488930891380942485307732666485384523705852790683809812073738758055115293090635233887206040961042759996972844810891420692117353333665907710709020698487019805669782598004799421226356372885464480818196786256472944761036204897548977647880837284232444863230958576095091824226426501119748518640709592225529707891969295441026284304137606735506294604060549102824977720776272463738349154440565501914642111802044575388635071779775767726626682303495430936326809'
f = 10000
l = len(raw) * f
input = np.array(list((map(int, raw))) * f, dtype=np.int8)
offset = int(raw[:7]) % l
print(offset, l)


x = input[::-1][:l // 2]
print(len(x))
for i in tqdm(range(100)):
    s = 0
    y = []
    for v in x:
        s += v
        y.append(abs(s) % 10)
    x = y

print(x)
offset -= l // 2
assert offset > 0
print(''.join(map(str, x[::-1][offset:offset + 8])))

exit()


def pattern_gen(i, n):
    while True:
        for p in [0, 1, 0, -1]:
            for _ in range(i):
                yield p


@memoize
def get_pattern(i):
    return list(islice(pattern_gen(i, l), 1, l + 1))


def get_item(position, iteration):
    # print(position, iteration)
    if iteration == 0:
        return input[position % len(raw)]
    result = 0
    for i, p in enumerate(get_pattern(position + 1)):
        if p == 0:
            continue
        result += p * get_item(i, iteration - 1)
    return abs(result) % 10

patters = np.array(list([get_pattern(i + 1) for i in tqdm(range(l))]), dtype=np.int8)
print(patters)

for i in range(l-1, 0, -1):
    print(patters[i-1] - patters[i])

exit()

for phrase in tqdm(range(100)):
    input = np.abs(np.multiply(patters, input).sum(axis=1)) % 10


print(''.join(map(str, input))[:8])
print(''.join(map(str, input * 2))[offset:offset + 8])
