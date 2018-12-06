from primes import *


def replace_digits(n, what, to):
    return int(str(n).replace(str(what), str(to)))

size = 8

for p in primes():
    found = 1
    l = [p]
    for to_replace in range(10 + 1 - size):
        found = 1
        l = [p]
        if str(to_replace) in str(p):
            for replacement in range(to_replace+1, 10):
                new = replace_digits(p, to_replace, replacement)
                if is_prime(new):
                    found +=1
                    l.append(new)
        if found >= size:
            break

    if found >= size:
        print p, l
        break