import hashlib

directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

H = 'UDLR'


def is_open(direction, history, pass_code='edjrjqaa'):
    c = pass_code + history
    d = hashlib.md5(c.encode('utf-8')).hexdigest()[:4]
    return d[direction] in 'bcdef'


states = [
    ((0, 0), '')
]

while len(states) > 0:
    new = []
    for (x, y), history in states:
        for i, (dx, dy) in enumerate(directions):
            if x + dx < 0 or y + dy < 0 or x + dx > 3 or y + dy > 3:
                continue
            if is_open(i, history):
                p = (x + dx), (y + dy)
                if p == (3, 3):
                    print(len(history) + 1)
                else:
                    new.append((p, history + H[i]))
    states = new
