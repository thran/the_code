from collections import defaultdict


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

with open('25.txt') as f:
    instructions = f.readlines()


def generate(input):
    registers = defaultdict(lambda: 0)
    registers['a'] = input

    i = 0
    steps = 0
    while i < len(instructions):
        steps += 1
        inst = instructions[i].split()

        if inst[0] == 'inc':
            registers[inst[1]] += 1
        if inst[0] == 'dec':
            registers[inst[1]] -= 1
        if inst[0] == 'cpy':
            registers[inst[2]] = int(inst[1]) if check_int(inst[1]) else registers[inst[1]]
        if inst[0] == 'tgl':
            d = int(inst[1]) if check_int(inst[1]) else registers[inst[1]]
            if i + d < len(instructions):
                if instructions[i + d].startswith('inc'):
                    instructions[i + d] = instructions[i + d].replace('inc', 'dec')
                elif instructions[i + d].startswith('dec'):
                    instructions[i + d] = instructions[i + d].replace('dec', 'inc')
                elif instructions[i + d].startswith('cpy'):
                    instructions[i + d] = instructions[i + d].replace('cpy', 'jnz')
                elif instructions[i + d].startswith('jnz'):
                    instructions[i + d] = instructions[i + d].replace('jnz', 'cpy')
                elif instructions[i + d].startswith('tgl'):
                    instructions[i + d] = instructions[i + d].replace('tgl', 'inc')
        if inst[0] == 'out':
            yield int(int(inst[1]) if check_int(inst[1]) else registers[inst[1]])
        if inst[0] == 'jnz' and (inst[1] == '1' or registers[inst[1]]):
            i += int(int(inst[2]) if check_int(inst[2]) else registers[inst[2]])
        else:
            i += 1

    print(registers)
    print(registers['a'] + registers['d'] * registers['c'])
    # print(''.join(instructions))

input = 0
while True:
    print(input, end=' ')
    for i, o in enumerate(generate(input)):
        if i % 2 != o:
            print('- not')
            break
    input += 1
