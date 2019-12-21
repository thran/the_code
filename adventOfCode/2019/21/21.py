from intcode import IntCode

memory = list(map(int, open('input.txt').readlines()[0].split(',')))
robot = IntCode(memory)

instructions1 = [
    'NOT C J',
    'NOT B T',
    'OR T J',
    'NOT A T',
    'OR T J',
    'AND D J',
    'WALK', ''
]

instructions = [
    'NOT C J',
    'NOT B T',
    'OR T J',
    'NOT A T',
    'OR T J',
    'AND D J',

    'NOT E T',
    'NOT T T',
    'OR H T',
    'AND T J',
    'RUN', ''
]

output = robot.run(inputs=map(ord, '\n'.join(instructions)))
print(output[-1])
print(''.join(map(chr, output[:-1])))
