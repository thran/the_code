import hashlib

from utils import memoize


@memoize
def code(n, salt='ihaygndm', stretch=2016):
    c = salt + str(n)
    for i in range(stretch + 1):
        c = hashlib.md5(c.encode('utf-8')).hexdigest()
    return c


def is_valid(n):
    c = code(n)
    for i in range(len(c) - 2):
        if c[i] == c[i + 1] == c[i + 2]:
            x = c[i] * 5
            for n2 in range(1000):
                c2 = code(n + 1 + n2)
                if x in c2:
                    return c
            break
    return False

i = 0
found = 0
while found < 64:
    i += 1
    if is_valid(i):
        print(i, found + 1)
        found += 1
