from math import log, sqrt

from primes import divisors


def presents(n):
    s = 0
    for divisor in divisors(n):
        if n / divisor <= 50:
            s += divisor
    return s * 11

# print(presents(2*2*2*2*2))
# print list(divisors(42))
# exit()

house = 1
while True:
    house += 1
    print house, house / 10. ** 6
    if presents(house) >= 33100000:
        print house, house / 10. ** 6, presents(house) / 33100000.
        break
