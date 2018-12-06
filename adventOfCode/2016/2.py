with open('2.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

ins = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1),
}

x, y = -2, 0


for line in lines:
    for i in line:
        a, b = ins[i]
        if abs(x + a) + abs(y + b) <= 2:
            x += a
            y += b
    print(x, y)
