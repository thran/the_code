with open('1.txt') as f:
    input = f.read().split(', ')

print(input)

directions = (1, 0), (0, 1), (-1, 0), (0, -1)
direction, x, y = 0, 0, 0

visited = []

for i in input:
    direction += 1 if i[0] == 'R' else -1
    direction %= 4
    l = int(i[1:])

    for _ in range(l):
        x += directions[direction][0]
        y += directions[direction][1]
        if (x, y) in visited:
            print(abs(x) + abs(y))
            exit()
        visited.append((x, y))


