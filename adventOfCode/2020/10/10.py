# start 8:29, 1. 8:37, 2. 8:48
from collections import defaultdict
from pathlib import Path

from utils import memoize

with Path('input.txt').open() as file:
    adapters = list(map(int, file))

device = max(adapters) + 3
adapters = [0] + sorted(adapters) + [device]

current_jolts = 0
diffs = defaultdict(int)
for jolts in adapters[1:]:
    diffs[jolts - current_jolts] += 1
    current_jolts = jolts

print(diffs[1] * diffs[3])


@memoize
def count_arrangements(from_position=0):
    if from_position + 1 == len(adapters):
        return 1

    count = 0
    jolts = adapters[from_position]
    for delta, adapter in enumerate(adapters[from_position + 1:]):
        if adapter > jolts + 3:
            break
        count += count_arrangements(from_position + delta + 1)
    return count


print(count_arrangements())
