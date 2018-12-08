class Node:
    def __init__(self):
        self.childern = []
        self.metadata = []

    def read(self, inputs):
        children_to_read = inputs.pop(0)
        metadata_to_read = inputs.pop(0)

        for _ in range(children_to_read):
            node = Node()
            self.childern.append(node)
            node.read(inputs)

        for _ in range(metadata_to_read):
            self.metadata.append(inputs.pop(0))

    def __str__(self):
        return f'N:{len(self.childern)} M:{sum(self.metadata)}'

    def hash(self):
        return sum(self.metadata) + sum([n.hash() for n in self.childern])

    def value(self):
        if not self.childern:
            return sum(self.metadata)
        s = 0
        for m in self.metadata:
            m = m - 1
            if m < 0 or m >= len(self.childern):
                continue
            s += self.childern[m].value()
        return s


with open('input.txt') as f:
    inputs = list(map(int, f.read().strip().split()))


root = Node()
root.read(inputs)

print(inputs, root, root.hash(), root.value())
