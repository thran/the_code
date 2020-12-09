# start 8:29, 1. 8:37, 2. 8:42
from pathlib import Path
from itertools import combinations


preamble_size = 25
with Path('input.txt').open() as file:
    numbers = list(map(int, file))


for i, n in enumerate(numbers):
    if i < preamble_size:
        continue
    if n not in map(sum, combinations(numbers[i - preamble_size: i], 2)):
        found_number = n
        break

print(found_number)


for start in range(len(numbers)):
    total = 0
    for end in range(start, len(numbers)):
        total += numbers[end]
        if total == found_number:
            print(max(numbers[start:end+1]) + min(numbers[start:end+1]))
            exit()
        if total > found_number:
            break
