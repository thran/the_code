def get_value(memory, index, mode):
    if mode == 0:
        return memory[memory[index]]
    if mode == 1:
        return memory[index]
    assert False, f'invalid mode {mode}'


def intcode(memory, debug=False):
    pointer = 0
    while True:
        instruction = memory[pointer]
        opcode = instruction % 100
        modes = list(map(int, str(instruction)[:-2][::-1])) + [0] * 3
        if opcode == 1:
            assert modes[2] == 0
            memory[memory[pointer + 3]] = get_value(memory, pointer + 1, modes[0]) + get_value(memory, pointer + 2, modes[1])
            pointer += 4
        elif opcode == 2:
            assert modes[2] == 0
            memory[memory[pointer + 3]] = get_value(memory, pointer + 1, modes[0]) * get_value(memory, pointer + 2, modes[1])
            pointer += 4
        elif opcode == 3:
            assert modes[0] == 0
            memory[memory[pointer + 1]] = int(input('Inser value: '))
            pointer += 2
        elif opcode == 4:
            print('output: ', get_value(memory, pointer + 1, modes[0]))
            pointer += 2
        elif opcode == 5:
            if get_value(memory, pointer + 1, modes[0]) != 0:
                pointer = get_value(memory, pointer + 2, modes[1])
            else:
                pointer += 3
        elif opcode == 6:
            if get_value(memory, pointer + 1, modes[0]) == 0:
                pointer = get_value(memory, pointer + 2, modes[1])
            else:
                pointer += 3
        elif opcode == 7:
            value = 1 if get_value(memory, pointer + 1, modes[0]) < get_value(memory, pointer + 2, modes[1]) else 0
            assert modes[2] == 0
            memory[memory[pointer + 3]] = value
            pointer += 4
        elif opcode == 8:
            value = 1 if get_value(memory, pointer + 1, modes[0]) == get_value(memory, pointer + 2, modes[1]) else 0
            assert modes[2] == 0
            memory[memory[pointer + 3]] = value
            pointer += 4
        elif opcode == 99:
            return memory
        else:
            assert False
        if debug:
            print(memory)
