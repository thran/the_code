from collections import defaultdict

from utils import memoize

components = []
ports = defaultdict(set)

with open('input.txt') as f:
    for i, line in enumerate(f):
        p1, p2 = map(int, line.strip().split('/'))
        components.append((p1, p2))
        ports[p1].add(i)
        ports[p2].add(i)

print(components)
print(ports)


@memoize
def solve(port=0, used_components=tuple()):
    available = ports[port] - set(used_components)
    if len(available) == 0:
        return 10**6 * len(used_components)

    options = []
    for c in available:
        p1, p2 = components[c]
        p = p1 if port == p2 else p2
        options.append(p1 + p2 + solve(p, used_components + (c, )))
    return max(options)

print(solve())
