import math
from utils import memoize


def is_pentagonal_number(n):
    x = int(math.sqrt(2 * n / 3)+1)
    return x*(3*x-1)/2 == n


def pentagonal_numbers(n=1):
    while True:
        yield n, n * (3 * n -1) / 2
        n += 1


for n, i in pentagonal_numbers():
    print "i:", i
    last = i
    for _, j in pentagonal_numbers():
        if j - last > i:
            break
        last = j
        if is_pentagonal_number(i+j) and is_pentagonal_number(i+j+j):
            print i,
            exit()
        j += 1

