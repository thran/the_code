from tqdm import tqdm


class Buffer:
    def __init__(self):
        self.next = {0: 0}
        self.values = {0: 0}
        self.position = 0
        self.size = 1

    def add(self, value):
        following = self.next[self.position]
        new = self.size
        self.next[self.position] = new
        self.next[new] = following
        self.position = new
        self.size += 1
        self.values[new] = value

    def move(self, steps):
        for _ in range(steps):
            self.position = self.next[self.position]

    def __str__(self):
        r = ''
        c = 0
        for i in range(self.size):
            if c == self.position:
                r += f'({str(self.values[c])}) '
            else:
                r += str(self.values[c]) + ' '
            c = self.next[c]
        return r


shift = 380

buffer = Buffer()
for i in tqdm(range(1, 2017 + 1)):
    steps = shift % buffer.size
    buffer.move(steps)
    buffer.add(i)

print(buffer.next[2017])
print(buffer.next[0])


position = 0
size = 1
after = None
for i in tqdm(range(1, 50000000 + 1)):
    position = (position + shift) % size + 1
    if position == 1:
        after = i
    size += 1

print(after)
