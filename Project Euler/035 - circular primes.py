from permutations import rotations
from primes import primes, is_prime

found = []
for p in primes():
    if p > 10 ** 6:
        break

    ok = True
    for r in rotations(str(p)):
        if not is_prime(int(r)):
            ok = False
            break
    if ok:
        print p
        found.append(p)

print len(found)