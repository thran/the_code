import itertools
from math import sqrt
from permutations import is_permutation
from primes import phi, is_prime, primes



m = 2
best = None
x = 1
for p1 in list(itertools.takewhile(lambda p: p<sqrt(10**7), primes()))[::-1]:
    print p1
    if p1 > 10 ** 7 / 2:
        break
    for p2 in primes():
        if p1 * p2 > 10 ** 7:
            break

        n = p1 * p2
        if is_permutation(str(n), str(phi(n))):
            if m > float(n / phi(n)):
                m = float(n / phi(n))
                best = n
                print best, m

print best, m