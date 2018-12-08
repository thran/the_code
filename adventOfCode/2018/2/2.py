from collections import Counter
from tqdm import tqdm

if False:
    count2 = 0
    count3 = 0
    with open('input.txt') as f:
        for line in f:
            id = line.strip()
            counts = Counter(id)
            if 2 in counts.values():
                count2 += 1
            if 3 in counts.values():
                count3 +=1


    print(count2, count3, count2 * count3)


def compare(s1, s2):
    difs = 0
    r = []
    for p1, p2 in zip(s1, s2):
        if p1 != p2:
            difs += 1
        else:
            r.append(p1)

    if difs == 1:
        return ''.join(r)
    return False


ids = []
with open('input.txt') as f:
    for line in f:
        id = line.strip()
        ids.append(id)


for i in tqdm(range(len(ids))):
    for j in range(i + 1, len(ids)):
        r = compare(ids[i], ids[j])
        if r:
            print(r)