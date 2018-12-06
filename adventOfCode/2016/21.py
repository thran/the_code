import re

with open('21.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()][::-1]

p = [l for l in 'fbgdceah']

for line in lines:
    if line.startswith('swap position'):
        g = re.search('(\d+) with position (\d+)', line).groups()
        p[int(g[0])], p[int(g[1])] = p[int(g[1])], p[int(g[0])]

    if line.startswith('swap letter'):
        g = re.search('(\w) with letter (\w)', line).groups()
        a, b = p.index(g[0]), p.index(g[1])
        p[a], p[b] = p[b], p[a]

    if line.startswith('rotate'):
        if line.startswith('rotate based on position of letter'):
            g = re.search('rotate based on position of letter (\w)', line).groups()
            i = p.index(g[0])
            if i % 2 == 1:
                r = - (i - 1) // 2 - 1
            elif i == 0:
                r = -1
            else:
                r = len(p) // 2 - 1 - i // 2
        else:
            g = re.search('rotate (left|right) (\d+) step', line).groups()
            if g[0] == 'right':
                r = int(g[1])
            else:
                r = len(p) - int(g[1])
            r = -r

        r %= len(p)
        p = p[-r:] + p[:-r]

    if line.startswith('reverse'):
        g = re.search('(\d+) through (\d+)', line).groups()
        a, b = int(g[0]), int(g[1])
        p = p[:a] + p[a:b + 1][::-1] + p[b + 1:]

    if line.startswith('move'):
        g = re.search('(\d+) to position (\d+)', line).groups()
        a, b = int(g[1]), int(g[0])
        p.insert(b, p.pop(a))

    print(line)
    print(''.join(p))
    print()
