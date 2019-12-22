from math import gcd
from utils import memoize

deck_size = 10007
deck = list(range(deck_size))


def deal(deck):
    return deck[::-1]


def cut(n, deck):
    return deck[n:] + deck[:n]


def deal_increment(n, deck):
    assert gcd(n, len(deck)) == 1
    new = [None] * len(deck)
    for i, v in enumerate(deck):
        new[(i * n) % len(deck)] = v
    return new


with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if 'deal with increment' in line:
            increment = int(line.split()[-1])
            deck = deal_increment(increment, deck)
        if line == 'deal into new stack':
            deck = deal(deck)
        if 'cut' in line:
            n = int(line.split()[-1])
            deck = cut(n, deck)

print(deck.index(2019))
print()


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


@memoize
def inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


deck_size = 119315717514047
repeats = 101741582076661
position = 2020


ps = []
a, b = 1, 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines[::-1]:
        line = line.strip()
        if 'deal with increment' in line:
            increment = int(line.split()[-1])
            x = inv(increment, deck_size)
            a = (a * x) % deck_size
            b = (b * x) % deck_size
        if line == 'deal into new stack':
            a = (-a) % deck_size
            b = (-b - 1) % deck_size
        if 'cut' in line:
            n = int(line.split()[-1])
            b = (b + n) % deck_size
        ps.append((a * position + b) % deck_size)

an = pow(a, repeats, deck_size)
print((an * position + b * (an - 1) * inv(a - 1, deck_size)) % deck_size)
