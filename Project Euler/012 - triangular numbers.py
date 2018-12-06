from collections import defaultdict
from math import sqrt


def divisors(n):
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

    divs = 1
    for _, c in primes.items():
        divs *= c+1

    return divs

x = 1
n = 1
count = 1
while count <= 500:
    count = divisors(n)
    print n, count
    x += 1
    n += x

print count