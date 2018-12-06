from permutations import permutations

for n, i in enumerate(permutations(list("0123456789"))):
    if n == 10**6 - 1:
        print n, "".join(i)
        break
