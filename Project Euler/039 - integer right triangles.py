import math

hits = [0] * 1001

for a in range(1, 500):
    for b in range(1, 500):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and a + b + c <= 1000:
            hits[int(a + b + c)] += 1


print hits, hits.index(max(hits))