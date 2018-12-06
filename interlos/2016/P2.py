import os

import time

h = 0
def is_good(n, number):
    global h
    for i in range(1, n + 1):
        first = None
        for j, c in enumerate(number):
            if ((c - 1) % n) + 1 == i:
                if first is None:
                    first = j
                else:
                    if (j - first) != i:
                        return False
                    first = None
                    break
        if first and len(number) - first > i:
            return False
    return True


def permutations(l, start=None):
    if start is not None and not is_good(n, start):
        return
    if start is None:
        start = []
    if len(l) == 1:
        yield l
    for pre in l:
        if pre - n in l:
            continue
        list_without = l[:]
        list_without.remove(pre)
        for post in permutations(list_without, start + [pre]):
            if is_good(n, start + [pre] + post):
                yield [pre] + post


def generate(n, used=None):
    results = []
    for number in permutations(range(1, n * 2 + 1)):
        results.append("".join(map(str, map(lambda x: (x - 1) % n + 1, number))))
    return results

n = 8
x = time.time()
r = sorted(generate(n))
print(r, len(r))
print(time.time() - x, h)

# print is_good(n, [1, 5, 4, 2, 3, 6, 8, 7])

