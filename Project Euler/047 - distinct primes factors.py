from primes import *

n = 4

x = 1
while True:
    ok = True
    for i in range(n):
        if not distinct_prime_factors(x + i) == n:
            ok = False

    if ok:
        print x
        break
    x += 1
