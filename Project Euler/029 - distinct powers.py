g = 100

hits = set()
for a in range(2, g + 1):
    for b in range(2, g + 1):
        hits.add(a**b)

print len(hits)