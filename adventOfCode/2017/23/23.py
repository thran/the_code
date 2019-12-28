from collections import defaultdict

from primes import is_prime


class Robot:
    def __init__(self):
        self.registers = defaultdict(int)
        self.registers['a'] = 1
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

        if self.position == 19:
            print(instruction, self.registers)
        if self.position == 23:
            print(instruction, self.registers)
        if self.position == 31:
            print(instruction, self.registers)

        if instruction[0] == 'set':
            self.registers[instruction[1]] = self.get_value(instruction[2])
        elif instruction[0] == 'add':
            self.registers[instruction[1]] += self.get_value(instruction[2])
        elif instruction[0] == 'sub':
            self.registers[instruction[1]] -= self.get_value(instruction[2])
        elif instruction[0] == 'mul':
            self.registers[instruction[1]] *= self.get_value(instruction[2])
            self.sent += 1
        elif instruction[0] == 'mod':
            self.registers[instruction[1]] %= self.get_value(instruction[2])
        elif instruction[0] == 'jgz':
            if self.get_value(instruction[1]) > 0:
                self.position += self.get_value(instruction[2]) - 1
        elif instruction[0] == 'jnz':
            if self.get_value(instruction[1]) != 0:
                self.position += self.get_value(instruction[2]) - 1
        else:
            assert False
        self.position += 1
        return True

    def run(self):
        sent = []
        while True:
        # for _ in range(20):
            r = self.step()
            if type(r) is int:
                sent.append(r)
            elif r is False or r is None:
                break
        return sent


r = Robot()
# r.run()
print(r.sent)
print(r.registers)

not_primes = 0
primes = 0
for n in range(107900, 124900 + 1, 17):
    print(n)
    if is_prime(n):
        primes += 1
    else:
        not_primes += 1

print(not_primes)
