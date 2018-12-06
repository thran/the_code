from fractions import gcd
from math import sqrt
import itertools
from primes import is_prime
from utils import is_square
def get_period(n):
    b = 1
    a = -int(sqrt(n))
    l = []
    first = -a
    sign = a, b

    done = False
    while sign != (a, b) or not done:
        done = True
        a = -a
        b = (n - a ** 2) / b
        new = 0
        while a > 0 or (a-b) ** 2 < n:
            new += 1
            a -= b
        l.append(new)

    return first, l

def period_to_generator(l):
    i = 0
    while True:
        yield l[i % len(l)]
        i += 1

def fracs(x):
    first, l = get_period(x)
    n = 0
    d = 1
    for a in period_to_generator(l):
        n += a * d
        g = gcd(d, n)
        d, n = n / g, d / g
        yield first * d + n, d


def find_solution(D):

    for x, y in fracs(D):
        if x ** 2 - D * y ** 2 == 1:
            return x, y

m = 0
best = 0
for D in range(1001):
    if not is_square(D):
        x, y = find_solution(D)
        print D, x, y
        if x > m:
            best = D
            m = x

print m, best
#
# print find_solution(61)