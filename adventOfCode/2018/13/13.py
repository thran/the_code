
class Map:
    def __init__(self):
        self.carts = {}

        with open('input.txt') as f:
            lines = f.readlines()
            lines = [l[:-1] for l in lines]
            self.x = max(len(line) for line in lines)
            self.y = len(lines)

            self.map = []
            for y in range(self.y):
                line = []
                self.map.append(line)
                for x in range(self.x):
                    if x > len(lines[y]) - 1:
                        line.append(' ')
                        continue
                    c = lines[y][x]
                    if c in ['>', '<']:
                        self.carts[(x, y)] = c, 0
                        line.append('-')
                    elif c in ['v', '^']:
                        self.carts[(x, y)] = c, 0
                        line.append('|')
                    else:
                        line.append(c)

    def get_next(self, x, y, d):
        if d == '>':
            return x+1, y, self.map[y][x+1]
        if d == '<':
            return x-1, y, self.map[y][x-1]
        if d == '^':
            return x, y-1, self.map[y-1][x]
        if d == 'v':
            return x, y+1, self.map[y+1][x]

    def step(self):
        # print('step')
        for (x, y), (d, tr) in sorted(self.carts.items(), key=lambda x: (x[0][1], x[0][0])):
            if (x, y) not in self.carts:
                return 
            nx, ny, t = self.get_next(x, y, d)
            if (nx, ny) in self.carts:
                del self.carts[(nx, ny)]
                del self.carts[(x, y)]
                continue

            nd = None
            if t in ['|', '-']:
                nd = d
            if t == '/':
                if d == '>':
                    nd = '^'
                if d == '<':
                    nd = 'v'
                if d == 'v':
                    nd = '<'
                if d == '^':
                    nd = '>'
            if t == '\\':
                if d == '>':
                    nd = 'v'
                if d == '<':
                    nd = '^'
                if d == 'v':
                    nd = '>'
                if d == '^':
                    nd = '<'
            if t == '+':
                if tr % 3 == 0:
                    if d == '>':
                        nd = '^'
                    if d == '<':
                        nd = 'v'
                    if d == 'v':
                        nd = '>'
                    if d == '^':
                        nd = '<'
                if tr % 3 == 1:
                    nd = d
                if tr % 3 == 2:
                    if d == '>':
                        nd = 'v'
                    if d == '<':
                        nd = '^'
                    if d == 'v':
                        nd = '<'
                    if d == '^':
                        nd = '>'
                tr += 1
            del self.carts[(x, y)]
            # print(x, y, d, tr, t)
            # print(nx, ny, nd, tr)
            self.carts[(nx, ny)] = nd, tr

        if len(self.carts) == 1:
            print(self.carts)
            exit()

    def __str__(self):
        s = ''
        for line in self.map:
            s += ''.join(line) + '\n'
        return s


map = Map()
while True:
    # print(map)
    # print(map.carts)
    map.step()
