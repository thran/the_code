from itertools import product, count


def mean(x, y):
    return (x + y) / 2


class Map():
    def __init__(self):
        self.rooms = {(0, 0)}
        self.doors = set()

    def walk(self, path):
        x, y = 0, 0
        for step in path:
            ox, oy = x, y
            if step == 'E':
                y += 1
            if step == 'W':
                y -= 1
            if step == 'S':
                x += 1
            if step == 'N':
                x -= 1

            self.doors.add((mean(ox, x), mean(oy, y)))
            self.rooms.add((x, y))

    def get_distances(self):
        distances = {(0,0): 0}
        for i in count(1):
            new = {}
            for (x, y), d in distances.items():
                if d + 1 == i:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), ]:
                        if (x + dx, y + dy) not in distances and (x + dx / 2, y + dy / 2) in self.doors:
                            new[x + dx, y + dy] = i
            if not new:
                break
            distances.update(new)
        return distances

    def __str__(self):
        xs = [x for x, y in self.rooms]
        ys = [y for x, y in self.rooms]
        r = '#' * ((max(ys) - min(ys) + 1) * 2 + 1) + '\n'
        for x in range(min(xs), max(xs) + 1):
            r += '#'
            for y in range(min(ys), max(ys) + 1):
                if (x, y) in self.rooms:
                    r += 'X' if x == y == 0 else '.'
                else:
                    r += '#'
                if (x, y + .5) in self.doors:
                    r += '|'
                else:
                    r += '#'
            r += '\n#'
            for y in range(min(ys), max(ys) + 1):
                if (x + .5, y) in self.doors:
                    r += '-#'
                else:
                    r += '##'
            r += '\n'

        return r


def get_parts(regular):
    stack = 0
    start = None
    splitters = []
    for i, r in enumerate(regular):
        if r == '(':
            stack += 1
            if start is None:
                start = i
        if r == ')':
            stack -= 1
            if stack == 0:
                yield start, i, splitters
                start = None
                splitters = []
        if r == '|' and stack == 1:
            splitters.append(i - start - 1)
    assert stack == 0


def split(regular, splitters):
    last = 0
    for splitter in splitters:
        yield regular[last:splitter]
        last = splitter + 1
    yield regular[last:]


def iter_paths(regular, depth=0):
    if '|' not in regular:
        yield regular
        return
    parts = []
    last = 0
    for start, end, splitters in get_parts(regular):
        parts.append([regular[last:start]])
        ps = []
        for s in split(regular[start + 1:end], splitters):
            if s == '':
                continue
            for t in iter_paths(s, depth + 1):
                ps.append(t)
        parts.append(ps)

        last = end + 1
    parts.append([regular[last:]])

    # print(parts, list(map(len, parts)))
    for ps in product(*parts):
        yield ''.join(ps)


with open('input.txt') as f:
    input = f.readline().strip()[1:-1]

m = Map()
for path in iter_paths(input):
    m.walk(path)

print(m)
distances = m.get_distances()
print(max(distances.values()))
print(len([d for d in distances.values() if d >= 1000]))
