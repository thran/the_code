from tqdm import tqdm

from intcode import IntCode


class Network:
    def __init__(self):
        memory = list(map(int, open('input.txt').readlines()[0].split(',')))

        count = 50
        self.nodes = {}
        for i in range(count):
            node = IntCode(memory.copy())
            outputs = node.run(inputs=[i], halt_on_missing_input=True)
            self.nodes[node] = node.steps
        self.queues = [[] for _ in range(count)]

        self.nat = None

    def tick(self):
        for queue, (node, steps) in sorted(zip(self.queues, self.nodes.items()), key=lambda x:x[1][1]):
            break

        inputs = None
        if queue:
            x, y, step = queue[0]
            if step < node.steps:
                queue.pop(0)
                inputs = [x, y]
        if inputs is None:
            inputs = [-1]
        output = True
        outputs = []
        while output:
            output = node.run(inputs=inputs, halt_on_output=True, halt_on_missing_input=True)
            outputs.append(output)
            if len(outputs) % 3 == 0:
                address = outputs[0]
                x, y = outputs[1], outputs[2]
                if address == 255:
                    self.nat = x, y
                else:
                    self.queues[address].append((x, y, node.steps))
                outputs = []
        self.nodes[node] = node.steps

    def run(self):
        last = -1
        while True:
            self.tick()
            if sum(map(len, self.queues)) == 0:
                if self.nat and last == self.nat[1]:
                    print('>>>>', last)
                    break
                print(self.nat)
                last = self.nat[1]
                self.queues[0].append((self.nat[0], self.nat[1], 0))


net = Network()
net.run()
