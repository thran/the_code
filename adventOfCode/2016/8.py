import re

with open('8.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

display = [[' '] * 50 for _ in range(6)]

for line in lines:
    print(line )
    if line.startswith('rect'):
        g = re.search('(\d+)x(\d+)', line).groups()
        for i in range(int(g[0])):
            for j in range(int(g[1])):
                display[j][i] = '#'
    if line.startswith('rotate column'):
        g = re.search('x=(\d+) by (\d+)$', line).groups()
        c = [display[i][int(g[0])] for i in range(len(display))]
        for i in range(len(c)):
            display[i][int(g[0])] = c[(i - int(g[1])) % len(c)]

    if line.startswith('rotate row'):
        g = re.search('y=(\d+) by (\d+)$', line).groups()
        r = display[int(g[0])][:]
        for i in range(len(r)):
            display[int(g[0])][i] = r[(i - int(g[1])) % len(r)]

for i in range(10):
    print('\n'.join([''.join(line[i * 5: (i + 1) * 5]) for line in display]))
    print()

print('\n'.join([''.join(line) for line in display]))

    # print(sum([sum(map(lambda s: 1 if s=='#' else 0, line)) for line in display]))