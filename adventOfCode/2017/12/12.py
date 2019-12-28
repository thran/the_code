from collections import defaultdict

from utils import memoize

graph = defaultdict(list)

with open('input.txt') as f:
    for line in f:
        node, neighbours = line.strip().split(' <-> ')

        graph[int(node)] = list(map(int, neighbours.split(', ')))


def explore(node):
    visited = {node: None}
    next = {node}
    while next:
        new = set()
        for n in next:
            for x in graph[n]:
                if x in visited:
                    continue
                visited[x] = n
                new.add(x)
        next = new
    return visited


d = explore(0)
print(len(d))


explored = set()
c = 0
while set(graph) - explored:
    n = list(set(graph) - explored)[0]
    explored |= set(explore(n).keys())
    c += 1
print(c)