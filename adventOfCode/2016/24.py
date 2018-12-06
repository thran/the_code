import permutations


def find_pos(n, map):
    for i, row in enumerate(map):
        if str(n) in row:
            return i, row.index(str(n))


def distance(map, start, end):
    visited = {start}
    current = [start]

    step = 0
    while True:
        step += 1
        new = []
        for x, y in current:
            for dx, dy in [(1, 0), (0, -1),(0, 1),(-1, 0)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) == end:
                    return step
                if map[nx][ny] != '#' and (nx, ny) not in visited:
                    new.append((nx, ny))
                    visited.add((nx, ny))
        current = new

with open('24.txt') as f:
    map = [l.strip('\n') for l in f.readlines()]

i = 0
positions = {}
while find_pos(i, map):
    positions[i] = (find_pos(i, map))
    i += 1

distances = {}
for n, p in positions.items():
    for n2, p2 in positions.items():
        if n < n2:
            distances[(n2, n)] = distances[(n, n2)] = distance(map, p, p2)

for n in positions.keys():
    for n2 in positions.keys():
        print('{:>3} '.format(distances[(n, n2)] if n != n2 else 0), end='')
    print()

to_visit = list(positions.keys())
to_visit.remove(0)

dists = []
for path in permutations.permutations(to_visit):
    current = 0
    d = 0
    for next in path + [0]:
        d += distances[(current, next)]
        current = next
    dists.append(d)

print(min(dists))