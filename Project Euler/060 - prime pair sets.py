from primes import is_prime, primes
from itertools import combinations, islice


def check(list):
    for p1 in list:
        for p2 in list:
            if p1 != p2 and not is_prime(int(str(p1)+str(p2))):
                return False
    return True


def ps(b=500):
    for ps in combinations(islice(primes(), 1, b), 4):
        if check(ps):
            yield ps


def not_working():
    for s in ps():
        print s
        for p in primes():
            if p > 10**6:
                break
            if p > s[-1]:
                t = list(s)
                t.append(p)
                if check(t):
                    print "win"
                    print t
                    print sum(t)
                    break

found = []

for p in primes():
    print p
    for f in found:
        if f[-1] < p:
            new = f + [p]
            if check(new):
                found.append(new)
                if len(new) == 5:
                    print new
                    print sum(new)
                    exit()

    for sp in primes():
        if sp == p:
            break
        if check([p, sp]):
            found.append([sp, p])