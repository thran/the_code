from utils import memoize


@memoize
def factorial(n):
    if n < 2: return 1
    return n * factorial(n-1)


for i in range(3, 10**6):
    s = 0
    for d in str(i):
        s += factorial(int(d))
    if s == i:
        print i