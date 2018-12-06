n = 100


def run(losi, i, j):
    l = losi[i]
    losi.remove(l)
    return losi[:j] + [l] + losi[j:]


losi = range(1, n + 1)
last = None
x = 0
while last != losi:
    print(losi[::-1])
    x += 1
    runs = []
    for l in losi:
        i = losi.index(l)
        for l2 in losi[:i][::-1]:
            if l % l2 == 0:
                runs.append((l, l2))
                break
    last = losi
    for l, l2 in runs:
        losi = run(losi, losi.index(l), losi.index(l2))

print(x)
