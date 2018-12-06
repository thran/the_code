import re

instructions = []

with open("23.txt") as f:
    for line in f.readlines():
        gs = re.match(r'(\w\w\w) (a|b)?((\+|-)\d+)?(, ((\+|-)\w+))?', line).groups()
        if gs[0] == "jmp":
            instructions.append((gs[0], int(gs[2])))
        elif gs[0].startswith("ji"):
            instructions.append((gs[0], gs[1], int(gs[5])))
        else:
            instructions.append((gs[0], gs[1]))
registers = {
    "a": 1,
    "b": 0,
}
position = 0
try:
    while True:
        instruction = instructions[position]
        print position + 1, instruction, registers
        if instruction[0] == "hlf":
            registers[instruction[1]] /= 2
            position += 1
        if instruction[0] == "tpl":
            registers[instruction[1]] *= 3
            position += 1
        if instruction[0] == "inc":
            registers[instruction[1]] += 1
            position += 1
        if instruction[0] == "jmp":
            position += instruction[1]
        if instruction[0] == "jie":
            if registers[instruction[1]] % 2 == 0:
                position += instruction[2]
            else:
                position += 1
        if instruction[0] == "jio":
            if registers[instruction[1]] == 1:
                position += instruction[2]
            else:
                position += 1
except IndexError:
    print registers


