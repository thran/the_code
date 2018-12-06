from collections import defaultdict
from itertools import combinations, chain

containers = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13 ,50 ,44 ,48 ,6 ,24, 41 ,30 , 42]

liters = 150


def power_sets(s):
    return chain.from_iterable(combinations(s, n) for n in range(len(s) + 1))

count = defaultdict(lambda:0)
for s in power_sets(containers):
    if liters == sum(s):
        count[len(s)] += 1

print count[min(count.keys())]
print count