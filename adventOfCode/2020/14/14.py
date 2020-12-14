# start 8:55, 1. 9:10, 2. 9:22
from itertools import product
from pathlib import Path

from parse import parse


program = []
with Path('input.txt').open() as file:
    for line in file:
        if line.startswith('mask'):
            program.append(line.strip()[7:])
        else:
            result = parse('mem[{:d}] = {:d}', line.strip())
            program.append((result[0], result[1]))

mask = None
memory = {}
for line in program:
    if type(line) is str:
        mask = line
        continue

    address, value = line
    for bit, m in enumerate(mask[::-1]):
        if m == '1':
            value |= (1 << bit)
        if m == '0':
            value &= ~(1 << bit)
    memory[address] = value

print(sum(memory.values()))


mask = None
memory = {}
for line in program:
    if type(line) is str:
        mask = line
        continue

    address, value = line
    floating_bits = []
    for bit, m in enumerate(mask[::-1]):
        if m == 'X':
            floating_bits.append(bit)
        if m == '1':
            address |= (1 << bit)

    for ms in product([False, True], repeat=len(floating_bits)):
        for bit, m in zip(floating_bits, ms):
            if m:
                address |= (1 << bit)
            else:
                address &= ~(1 << bit)
        memory[address] = value

print(sum(memory.values()))
