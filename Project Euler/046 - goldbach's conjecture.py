import math
from primes import is_prime

n = 9
while True:
    if not is_prime(n):
        ok = True
        for s in range(1, int(math.sqrt(n / 2))+1):
            if is_prime(n - 2 * s ** 2):
                ok = False
                print "{} = {} + 2 * {}^2".format(n, n - 2 * s ** 2, s)
                break

        if ok:
            print
            print n
            break

    n += 2