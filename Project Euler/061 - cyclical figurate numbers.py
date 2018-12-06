from collections import defaultdict
from sequences import *


def successors(list, n):
    n = str(n)[-2:]
    for m in list:
        if n == str(m)[:2]:
            yield m


def check(lst, m):
    if len(lst) == 1:
        return len(m[lst[0]]) > 0
    a = []
    new = {}
    for x in m[lst[0]]:
        for l in lst:
            n = m[l][:]
            if x in n:
                n.remove(x)
            new[l] = n
        a.append(check(lst[1:], new))
    return any(a)


# print check([1, 2], {1: [0], 2:[0]})
# exit()

numbers = []
m = defaultdict(lambda: [])
for i in range(3, 9):
    for n in seq_numbers(i):
        if n < 1000:
            continue
        if n > 9999:
            break
        numbers.append(n)
        m[n].append(i)


seqs = [[n] for n in m.keys()]
for i in range(2, 7):
    new = []
    for seq in seqs:
        for suc in successors(m.keys(), seq[-1]):
            if check(seq + [suc], m):
                new.append(seq + [suc])

    seqs = new

for seq in seqs:
    if str(seq[-1])[-2:] == str(seq[0])[:2]:
        print seq, sum(seq)