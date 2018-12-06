from primes import *


def is_truncatable(p):
    p = str(p)
    for i in range(1, len(p)):
        if not (is_prime(int(p[:-i])) and is_prime(int(p[i:]))):
            return False
    return True

print is_truncatable(97)

count = 0
found = []
for p in primes():
    if p > 10:
        if is_truncatable(p):
            count += 1
            found.append(p)
            print p
    if count == 11:
        break

print sum(found)