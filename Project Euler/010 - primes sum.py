import math


def is_prime(p):
    if p == 2: return True
    for d in range(2, int(math.sqrt(p))+2):
        if p % d == 0:
            return False
    return True


sum = 0
for p in range(2, 2 * 10**6):
    if is_prime(p):
        sum += p

print sum