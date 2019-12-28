def dist(x, y):
    if x > 0:
        if y >= 0:
            return x + y
        return x + max(-y - x, 0)
    else:
        if y <= 0:
            return -x - y
        return -x + max(y + x, 0)


directions = {
    'n': (0, -1),
    's': (0, 1),
    'nw': (-1, 0),
    'sw': (-1, 1),
    'ne': (1, -1),
    'se': (1, 0),
}

inpt = list(open('input.txt').readline().strip().split(','))
x, y = 0, 0
m = 0
for d in inpt:
    dx, dy = directions[d]
    x, y = x + dx, y + dy
    m = max(m, dist(x, y))

print(x, y, dist(x, y), m)
