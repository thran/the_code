from collections import defaultdict

from utils import memoize

weights = {}
up = defaultdict(list)
down = {}


with open('input.txt') as f:
    for line in f:
        if ' -> ' in line:
            bottom, top = line.strip().split(' -> ')
        else:
            bottom, top = line.strip(), []

        name, weight = bottom.split()
        weight = int(weight[1:-1])
        if top:
            top = top.split(', ')

        weights[name] = weight
        for t in top:
            up[name].append(t)
            down[t] = name

base = list(set(weights) - set(down))[0]
print(base)


@memoize
def get_weight(disc):
    return weights[disc] + sum([get_weight(d) for d in up[disc]])


current = base
while True:
    sts = defaultdict(list)
    for st in up[current]:
        sts[get_weight(st)].append(st)

    l = sorted(sts.items(), key=lambda x: len(x[1]))
    if len(l) != 2:
        break
    w, best = l[0]
    diff = l[0][0] - l[1][0]
    print(w, best)
    current = best[0]


print(current, weights[current] - diff)
