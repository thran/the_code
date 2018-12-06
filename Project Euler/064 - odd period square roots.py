from math import sqrt


def get_period(n):
    b = 1
    a = -int(sqrt(n))
    l = []
    first = -a
    sign = a, b

    done = False
    while sign != (a, b) or not done:
        done = True
        a = -a
        b = (n - a ** 2) / b
        new = 0
        while a > 0 or (a-b) ** 2 < n:
            new += 1
            a -= b
        l.append(new)

    return first, l

hits = 0
for i in range(2, 10**4 + 1):
    if int(sqrt(i)) ** 2 != i:
        _, l = get_period(i)
        if len(l) % 2 == 1:
            hits += 1

print hits