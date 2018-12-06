from math import sqrt
from fractions import gcd
import itertools

def el():
    i = 0
    k = 2
    while True:
        if i % 3 != 1:
            yield 1
        else:
            yield k
            k += 2
        i += 1


first, l = 2, el()


x = 100 - 1
n = 0
d = 1
for a in list(itertools.islice(el(), x))[::-1]:
    n += a * d
    g = gcd(d, n)
    d, n = n / g, d / g

n = first * d + n
print sum(map(int, str(n)))