from pathlib import Path

from parse import parse
from collections import Counter

with Path('input.txt').open() as file:
    valids = 0
    valids2 = 0
    for line in file:
        result = parse('{minimum:d}-{maximum:d} {letter}: {password}', line.strip())
        password = result['password']
        counts = Counter(password)
        if result['minimum'] <= counts.get(result['letter'], 0) <= result['maximum']:
            valids += 1
        letters = {password[result['minimum'] - 1], password[result['maximum'] - 1]}
        if result['letter'] in letters and len(letters) > 1:
            valids2 += 1

print(valids)
print(valids2)
