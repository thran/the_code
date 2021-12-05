from collections import defaultdict

from tqdm import tqdm

loss = defaultdict(set)
with open('connections.txt') as f:
    for line in tqdm(f):
        n1, n2 = line.strip().split(' - ')
        loss[n1].add(n2)
        loss[n2].add(n1)

while True:
    total = len(loss)
    to_remove = set()
    for los, knows in loss.items():
        if len(knows) < 20 or total - len(knows) - 1 < 20:
            to_remove.add(los)

    for tr in to_remove:
        del loss[tr]

    for los, knows in loss.items():
        loss[los] = knows - to_remove

    print(len(loss))
    if len(loss) == total:
        break
