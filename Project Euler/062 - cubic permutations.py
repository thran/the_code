from itertools import permutations


def is_cube(n):
    return round(n**(1/3.)) ** 3 == n


# i = 5
# while True:
#     n = i ** 3
#     hits = 0
#     founds = []
#     for p in permutations(list(str(n))):
#         x = int("".join(p))
#         if x >= n and not x in founds and is_cube(x):
#             hits += 1
#             founds.append(x)
#     print i, founds, hits
#     if hits == 5:
#         print n
#         break
#
#     i += 1


i = 5
while True:
    n = i ** 3
    sn = sorted(str(n))
    hits = 0
    found = [n]
    for j in range(i):
        m = j ** 3
        if sn == sorted(str(m)):
            hits += 1
            found.append(m)
    if hits == 5 - 1:
        break
    i += 1

print found, min(found)