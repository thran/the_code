from permutations import permutations

digits = list("0123456789")

divisors = [2, 3, 5, 7, 11, 13, 17]

s = 0
for p in permutations(digits):
    if p[0] != "0":
        ok = True
        for i, d in enumerate(divisors):
            sub = int("".join(p[i+1: i+4]))
            if sub % d != 0:
                ok = False
                break
        if ok:
            print "".join(p)
            s +=  int("".join(p))

print s