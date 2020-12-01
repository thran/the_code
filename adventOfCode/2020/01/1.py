from itertools import combinations
from math import prod
from pathlib import Path

numbers = list(map(int, Path('input.txt').open().readlines()))

for count in [2, 3]:
    for ns in combinations(numbers, count):
        if sum(ns) == 2020:
            print(prod(ns))
