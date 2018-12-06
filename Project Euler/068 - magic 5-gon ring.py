from itertools import permutations


def check(p, gon):
    s = None
    for i in range(gon):
        t = p[i] + p[i + gon] + p[(i + 1) % gon + gon]
        if s is None:
            s = t
        else:
            if s != t:
                return False

    return True

def reorder(p, gon):
    move = 0
    mi = gon * 3
    for i, x in enumerate(p[:gon]):
        if mi > x:
            move = i
            mi = x

    new = [0] * (gon * 2)
    for i, x in enumerate(p[:gon]):
        new[(i - move) % gon] = x
        new[(i - move) % gon + gon] = p[i + gon]

    return new

def to_string(p, gon):
    s = ""
    for i in range(gon):
        s += str(p[i]) + str(p[i + gon]) + str(p[(i + 1) % gon + gon])
    return  s

gon = 5

numbers = range(1, 1 + 2 * gon)

solution = set()
for p in permutations(numbers):
    if check(p, gon):
        p = reorder(p, gon)
        solution.add(to_string(p, gon))

for s in solution:
    print s