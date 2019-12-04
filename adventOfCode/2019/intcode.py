def intcode(memory, debug=False):
    pointer = 0
    while True:
        instruction = memory[pointer]
        if instruction == 1:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
            pointer += 4
        elif instruction == 2:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
            pointer += 4
        elif instruction == 99:
            return memory
        else:
            assert False
        if debug:
            print(memory)

