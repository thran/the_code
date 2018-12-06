import json
import re
from collections import defaultdict
from itertools import permutations

hep = defaultdict(lambda: defaultdict(lambda: 0))

with open("13.txt") as source:
    for line in source.readlines():
        g = re.match(r'(\w+) .* (gain|lose) (\d+) .* (\w+).', line).groups()
        hep[g[0]][g[3]] = int(g[2]) * (-1 if g[1] == "lose" else 1)

totals = []
print json.dumps(hep, indent=4)

for perm in permutations(hep.keys() + ["self"]):
    total = 0
    for i, p in enumerate(perm):
        total += hep[p][perm[(i + 1) % len(perm)]]
        total += hep[perm[(i + 1) % len(perm)]][p]
    totals.append(total)

print min(totals), max(totals)
