import math


def is_prime(p):
    if p == 2: return True
    for d in range(2, int(math.sqrt(p))+2):
        if p % d == 0:
            return False
    return True



n = 10001
p = 1
while n > 0:
    p +=1
    if is_prime(p):
        n -= 1
        print p

print p