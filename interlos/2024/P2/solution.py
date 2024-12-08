import math
from itertools import product

from tqdm import tqdm

eqs = []


def _parse(side):
    members = []
    for part in side.split('+'):
        c, u, s = part.split()
        members.append((int(c), u, int(s) - 1))
    return members


with open('input.txt') as f:
    # with open('input.test.txt') as f:
    for line in f:
        l, r = line.strip().split(' = ')
        print(l, '....', r)
        eqs.append((_parse(l), _parse(r)))


def eval_member(count, unit, price):
    if unit == 'S':
        return count * price
    if unit == 'T':
        return count * 3 * price**2
    if unit == 'B':
        return count * price**3
    if unit == 'P':
        return count * math.comb(price + 2, 3)
    if unit == 'K':
        return count * 2**price


def eval(prices, side):
    return sum(eval_member(c, u, prices[s]) for c, u, s in side)


for left, right in eqs:
    print(len({s for c, u, s in left} | {s for c, u, s in right}))


# for prices in tqdm(product(range(1, 21), range(1, 21), range(1, 21))):
#     for left, right in eqs:
#         if eval(prices, left) != eval(prices, right):
#             break
#     else:
#         print(prices)
