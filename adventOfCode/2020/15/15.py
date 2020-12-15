# start 9:25, 1. 9:43, 2. 9:44
from pathlib import Path

from parse import parse


program = []
with Path('input.txt').open() as file:
    numbers = list(map(int, file.readline().strip().split(',')))

last_spoken = {}
last_number = None
turn = 0
for number in numbers:
    if last_number is not None:
        last_spoken[last_number] = turn
    turn += 1
    last_number = number

for limit in [2020, 30000000]:
    while turn < limit:
        if last_number not in last_spoken:
            diff = 0
        else:
            diff = turn - last_spoken[last_number]
        last_spoken[last_number] = turn
        turn += 1
        last_number = diff

    print(last_number)
