# start 9:05, 1. 9:16, 2. 10:05
from math import prod
from pathlib import Path

from parse import parse

from utils import extended_gcd

with Path('input.txt').open() as file:
    earliest = int(file.readline().strip())
    buses = [(int(i) if i.isdigit() else i) for i in file.readline().strip().split(',')]


departures = []
for bus in buses:
    if bus == 'x':
        continue
    departure = bus - earliest % bus if earliest % bus else 0
    departures.append((departure, bus))

print(prod(min(departures)))


# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(constructive_proof)
n1 = 1
a1 = 0
for i, n2 in enumerate(buses):
    if n2 == 'x':
        continue
    a2 = - i - 1
    gcd, m1, m2 = extended_gcd(n1, n2)
    assert gcd == 1
    a1 = (a1 * m2 * n2 + a2 * m1 * n1) % (n1 * n2)
    n1 *= n2

print(a1 + 1)
