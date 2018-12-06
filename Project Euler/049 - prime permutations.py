import itertools
from permutations import permutations
from primes import primes, is_prime

for p in primes():
    if p > 10**4:
        break

    found = []
    for perm in permutations(list(str(p))):
        n = int("".join(perm))
        if is_prime(n) and len(str(n)) == len(str(p)):
            found.append(n)

    found = list(set(found))

    for f in itertools.combinations(found, 3):
        f = list(f)
        f.sort()
        if f[1] - f[0] == f[2] - f[1]:
            print f