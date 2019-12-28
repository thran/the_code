from fractions import Fraction
from functools import reduce
from math import sqrt
from collections import defaultdict
from utils import memoize


@memoize
def factorization(n):
    found_primes = defaultdict(lambda: 0)
    while n > 1:
        found = False
        for i in primes():
            if n % i == 0:
                found_primes[i] += 1
                n /= i
                found = True
                break
        if not found:
            found_primes[n] += 1
            break
    return found_primes


@memoize
def is_prime(n):
    if n == 2:
        return True
    for i in primes():
        if i > int(sqrt(n)):
            break
        if n % i == 0:
            return False
    return True


def primes():
    yield 2
    p = 3
    while True:
        if is_prime(p):
            yield p
        p += 2


def prime_factors(n):
    return sum(factorization(n).values())


def distinct_prime_factors(n):
    return len(factorization(n).keys())

def phi(n):
    for p, c in factorization(n).items():
        n *= (1 - Fraction(1, p))
    return n


def divisors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
