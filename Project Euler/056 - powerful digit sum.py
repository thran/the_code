m = 0
for a in range(100):
    for b in range(100):
        m = max(m, sum([int(d) for d in str(a**b)]))

print m