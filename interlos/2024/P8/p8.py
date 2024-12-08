import json

import networkx as nx
import numpy as np

# data = json.load(open('psanicka-sample.json'))
data = json.load(open('psanicka.json'))

G = nx.Graph()
plan = np.array(data['pipeMap'])
for i in range(0, plan.shape[0], 2):
    for j in range(1, plan.shape[0], 2):
        G.add_edge(plan[i, j - 1], plan[i, j + 1], weight=int(plan[i, j]))
    if i + 1 == plan.shape[0]:
        continue
    for j in range(0, plan.shape[0], 2):
        G.add_edge(plan[i, j], plan[i + 2, j], weight=int(plan[i + 1, j]))


print(data['routes'])

candidates = set(G.nodes)
intercepts = 0
for route, time in data['routes'].items():
    f, t = route.split('/')
    shortest_distance = nx.shortest_path_length(G, f, t, 'weight')
    if shortest_distance != time:
        path = nx.shortest_path(G, f, t, 'weight')
        candidates &= set(path)
        intercepts += 1

assert len(candidates) == 1
print(f'{list(candidates)[0]}X{intercepts}')
