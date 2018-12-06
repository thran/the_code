from itertools import chain, combinations


def power_sets(s):
    return chain.from_iterable(combinations(s, n) for n in range(len(s) + 1))


def priority(g):
    return len(g), reduce(lambda a, b: a * b, g, 1)

# packages = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11}
packages = {3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 ,59 ,67 ,71 ,73 ,79 ,83 ,89 ,97 ,101 ,103 ,107 ,109 , 113}
s = sum(packages) / 4
groups = []
for group in power_sets(packages):
    if sum(group) != s:
        continue
    groups.append(group)

groups.sort(key=priority)
print priority(groups[0])[1]
