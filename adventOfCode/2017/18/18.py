from collections import defaultdict


class Robot:
    def __init__(self, id):
        self.registers = defaultdict(int)
        self.registers['p'] = id
        self.position = 0
        self.instructions = []
        with open('input.txt') as f:
            for line in f:
                self.instructions.append(line.strip().split())
        self.queue = []
        self.sent = 0

    def get_value(self, v):
        try:
            return int(v)
        except:
            return self.registers[v]

    def step(self):
        if self.position >= len(self.instructions):
            return
        instruction = self.instructions[self.position]
        if instruction[0] == 'snd':
            self.sent += 1
            self.position += 1
            return self.get_value(instruction[1])
        elif instruction[0] == 'set':
            self.registers[instruction[1]] = self.get_value(instruction[2])
        elif instruction[0] == 'add':
            self.registers[instruction[1]] += self.get_value(instruction[2])
        elif instruction[0] == 'mul':
            self.registers[instruction[1]] *= self.get_value(instruction[2])
        elif instruction[0] == 'mod':
            self.registers[instruction[1]] %= self.get_value(instruction[2])
        elif instruction[0] == 'rcv':
            if self.queue:
                self.registers[instruction[1]] = self.queue.pop(0)
            else:
                return False
        elif instruction[0] == 'jgz':
            if self.get_value(instruction[1]) > 0:
                self.position += self.get_value(instruction[2]) - 1
        else:
            assert False
        self.position += 1
        return True

    def run(self):
        sent = []
        while True:
            r = self.step()
            if type(r) is int:
                sent.append(r)
            elif r is False or r is None:
                break
        return sent


r1 = Robot(0)
r2 = Robot(1)

while True:
    q = r1.run()
    r2.queue += q
    q = r2.run()
    r1.queue += q
    if len(r1.queue) + len(r2.queue) == 0:
        break

print(r1.queue, r2.queue)
print(r1.sent, r2.sent)
