from collections import Counter

from ciphers import caesar

with open('4.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]


s = 0
for line in lines:
    line = line.split('-')
    name = ''.join(line[:-1])
    check = line[-1].split('[')[-1][:-1]
    number = int(line[-1].split('[')[0])
    counts = dict(Counter(name)).items()
    counts = sorted(counts, key=lambda x: (-x[1], x[0]))
    if ''.join([c[0] for c in counts[:5]]) == check:
        s += number
        name = ' '.join(line[:-1])
        decoded = caesar(name, number)
        if 'north' in decoded:
            print(decoded, number)


