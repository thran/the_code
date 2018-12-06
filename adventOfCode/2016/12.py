from collections import defaultdict

with open('12.txt') as f:
    instructions = f.readlines()


registers = defaultdict(lambda: 0)
registers['c'] = 1

i = 0
while i < len(instructions):
    instruction = instructions[i].split()
    if instruction[0] == 'inc':
        registers[instruction[1]] += 1
    if instruction[0] == 'dec':
        registers[instruction[1]] -= 1
    if instruction[0] == 'cpy':
        registers[instruction[2]] = int(instruction[1]) if instruction[1].isdecimal() else registers[instruction[1]]
    if instruction[0] == 'jnz' and (registers[instruction[1]] or instruction[1] == '1'):
        i += int(instruction[2])
    else:
        i +=1

print(registers)
