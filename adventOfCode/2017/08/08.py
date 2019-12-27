import sys
from collections import defaultdict

registers = defaultdict(int)


def evaluate(condition):
    register = condition.split()[0]
    return eval(condition.replace(register, str(registers[register])))


m = - (10 ** 100)
with open('input.txt') as f:
    for line in f:
        action, condition = line.strip().split(' if ')
        if evaluate(condition):
            register, action, value = action.split()
            value = int(value)
            if action == 'inc':
                registers[register] += value
            elif action == 'dec':
                registers[register] -= value
            m = max(m, max(registers.values()))
        # print(registers)

print(max(registers.values()), m)
