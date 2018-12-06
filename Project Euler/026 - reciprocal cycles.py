from math import sqrt
from collections import defaultdict


def factorization(n):
    primes = defaultdict(lambda: 0)
    while n > 1:
        found = False
        for i in range(2, int(sqrt(n)+2)):
            if n % i == 0:
                primes[i] += 1
                n /= i
                found = True
                break
        if not found:
            primes[n] += 1
            break
    return primes


def get_cycle_len(n):
    n_primes = factorization(n)
    if set(n_primes.keys()) <= {2, 5}:
        return 0

    bad_n = 1
    for p, c in n_primes.items():
        if p != 2 and p!=5:
            bad_n *= p ** c

    cycle = 1
    while True:
        x = 10 ** cycle - 1
        if x % bad_n == 0:
            return cycle
        cycle += 1


# print get_cycle_len(17)

l = []
for i in range(2, 1000):
    l.append(get_cycle_len(i))

print max(l)