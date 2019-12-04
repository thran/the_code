def wire(path, steps_to=None, debug=False):
    x, y = 0, 0
    positions = set()
    steps = 0
    for part in path:
        direction = part[0]
        size = int(part[1:])
        if debug:
            print(direction, size)
        for _ in range(size):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            else:
                assert False
            positions.add((x, y))
            steps += 1
            if steps_to is not None and steps_to == (x, y):
                return steps
    return positions


w1, w2 = open('inupt.txt').readlines()
w1 = w1.split(',')
w2 = w2.split(',')

p1 = wire(w1)

p2 = wire(w2)
print(p1 & p2)
print(min([abs(x) + abs(y) for x, y in p1 & p2]))


distances = [wire(w1, steps_to=target) + wire(w2, steps_to=target) for target in p1 & p2]
print(sorted(distances))
print(min(distances))
