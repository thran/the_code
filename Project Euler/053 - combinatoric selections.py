import math


def choose(n, k):
    f = math.factorial
    return f(n) / f(k) / f(n - k)


hits = 0
for n in range(101):
    for k in range(n+1):
        if choose(n, k) > 10**6:
            hits += 1

print hits